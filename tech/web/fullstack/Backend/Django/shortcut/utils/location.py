from django.db import models
from django.conf import settings
from django import forms

"""
USAGE:
    location = LocationField(blank=True, max_length=255)

"""


class LocationPickerWidget(forms.TextInput):
    class Media:
        """
        Place assets to static folder
        """
        css = {
            'all': (
                'map/location_picker.css',
            )
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js',
            'https://maps.googleapis.com/maps/api/js?v=3&key=' + settings.MAPS_API_KEY,  # set api in settings
            'map/jquery.location_picker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        if attrs is None:
            attrs = {}
        attrs['class'] = 'location_picker'
        super(LocationPickerWidget, self).__init__(attrs=attrs)


class LocationField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'max_length': 255})
        super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)
