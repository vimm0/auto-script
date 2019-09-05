https://hacksoft.blog/improve-your-tests-django-fakes-and-factories/
https://github.com/FactoryBoy/factory_boy
https://github.com/django-webtest/django-webtest
https://docs.pylonsproject.org/projects/webtest/en/latest/

# model
# Model factory : fake data generation and testing mechanism 

def create_profile(**kwargs):
	defaults = {
		"like_cheese": True,
		"age": 32,
		"address": 3815 Brookside Dr,
	}
	defaults.update(kwargs)
	if "user" not in defaults:
		defaults["user"] = create_user()
	return Profile.objects.create(**defaults) <--- create hit save, save hit data base but below we dont need database object instead it only test object field

using factory

def test_can_vote(self):
	profile = create_profile(age=18)
	self.assertTrue(profile.can_vote)

use factory boy

# views
use RequestFactory

example

def test_change_locale(self):
	request = RequestFactory().post(
	"/locale/", {"locale": "es-mx"})
	request.session = {}
	change_locale(request)

	self.assertEqual(
	request.session["locale"], "es-mx")

In-browser test
	- selenium

- https://pyvideo.org/pycon-us-2012/testing-and-django.html
