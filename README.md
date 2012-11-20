Billbalance
===========

Billbalance is a website that helped my girlfriend and I keep track of who payed what and who owes who again.
We are still using the website actively since the day I introduced to her.

I'm using [Bootstrap v2.2.1](http://twitter.github.com/bootstrap/) for css since I'm far from a designer.

This project is quite small and can become a very big project. 
But I'm not planning to make this a big project since it does everything I need at the moment.
Suggestions are always welcome.


How it works
------------

When someone wants to update billbalance, he or she goes to http://example.com/billbalance/,
selects who payed,
for who and how much,
and finishes by pressing the Insert button.


Settings
--------

Django 1.4 or up is required. Django 1.3 should be fine.

* Download code
* Copy sample-settings.py to settings.py and change the STATICFILES_DIRS and TEMPLATE_DIRS variables
* In the admin panel create Person objects for everyone you want to add
* Make sure you have an account that belongs to the group 'billbalance'

If you get the error "You don't have the permission to be here",
make sure the user's account is added to the group "billbalance".
It's a weird security way, so suggestions for this are always welcome.


