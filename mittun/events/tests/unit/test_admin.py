from django.test import TestCase
from django.contrib import admin

from mittun.events.models import Location, Event
from events.admin import LocationAdmin


class AdminTestCase(TestCase):

    def test_should_register_location_model(self):
        self.assertIn(Location, admin.site._registry)

    def test_should_register_location_model_with_LocationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Location], LocationAdmin)

    def test_should_register_event_model(self):
        self.assertIn(Event, admin.site._registry)
