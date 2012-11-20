from django.contrib import admin
from models import *

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'balance',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Bill)
