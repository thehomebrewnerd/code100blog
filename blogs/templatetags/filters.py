from datetime import datetime
from django.template.defaultfilters import timesince
from django import template
import pytz

register = template.Library()


@register.filter('ago')
def ago(date_time):
    diff = abs(date_time - datetime.utcnow().replace(tzinfo=pytz.utc))
    if diff.days <= 0:
        span = timesince(date_time)
        span = span.split(",")[0] # just the most significant digit
        return "{} ago".format(span)
    else:
        if diff.days <= 1:
            label = 'day'
        else:
            label = 'days'
        return "{} {} ago".format(diff.days, label)
