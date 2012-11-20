from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=127)

	def __unicode__(self):
		return self.name

	def balance(self):
		amount = Bill.objects.filter(person=self).aggregate(models.Sum('amount'))['amount__sum']
		if amount is None:
			return 0
		return amount

	def pays(self, amount, persons):
		Bill.objects.create(person=self, amount=amount)
		amount /= (float) (-len(persons))
		for person in persons:
			person = Person.objects.get(name=person)
			Bill.objects.create(person=person, amount=amount)
			
class Bill(models.Model):
	person = models.ForeignKey(Person)
	amount = models.FloatField()
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.person.name + ' ' + str(self.amount) + ' ' + str(self.date)
