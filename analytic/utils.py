# _*_ coding: utf-8 _*_
from rest_framework_mongoengine import serializers

from mongoengine import DateTimeField
from django.core.exceptions import ValidationError
import datetime
import calendar
from pytz import utc # pip install pytz

class UnixEpochDateTimeField(DateTimeField):

    def to_representation(self, value):
        """
        to_representation method is responsible for turning the
        Python object into a simple, serializable value.
        Here: return epoch time for a datetime object or `None`
        """
        return self.datetime_to_epoch(value)

    def to_internal_value(self, value):
        return self.epoch_to_datetime(value)

    @staticmethod
    def datetime_to_epoch(value):
        try:
            return int(calendar.timegm(value.utctimetuple()))
        except (AttributeError, TypeError):
            return None

    @staticmethod
    def epoch_to_datetime(value):
        try:
            return datetime.datetime.utcfromtimestamp(int(value)).replace(tzinfo=utc)
        except (ValueError, TypeError):
            raise ValidationError('%s is not a valid value' % value)



