from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *
from models import *

def getdef(dictionary, key, default=None):
    if dictionary.has_key(key):
        return dictionary[key]
    return default

def getdeflist(dictionary, key, default=None):
    if dictionary.has_key(key):
        return dictionary.getlist(key)
    return default

@csrf_exempt
@login_required(login_url='/login/')
def index(request):
    errorlist = []
    group = Group.objects.get_or_create(name='billbalance')
    if request.user.groups.filter(name='billbalance').count() == 0:
        errorlist.append('You don\'t have the permission to be here')
        return render_to_response('billbalance.html', {
            'errorlist':errorlist,
        })
    updated = False
    person = getdef(request.POST, 'person')
    amount = 0
    try:
        amount = int(getdef(request.POST, 'amount', 0))
    except:
        errorlist.append('Invalid amount')
    persons = getdeflist(request.POST, 'persons')
    if person and persons is None:
        errorlist.append('No persons selected')
    if person is not None and amount > 0 and persons is not None:
        try:
            person = Person.objects.get(name=person)
            person.pays(amount, persons)
            request.session['person'] = person
            updated = True
        except Exception as e:
            errorlist.append(str(e))
    else:
        person = getdef(request.session, 'person')
    return render_to_response('billbalance.html', {
        'errorlist': errorlist,
        'selected_person': person,
        'bills': Bill.objects.order_by('-id')[0:20],
        'person_list': Person.objects.all(),
        'updated': updated,
    })
