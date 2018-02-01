from datetime import datetime
from django.template.defaultfilters import timesince
from django import template
from django.utils.safestring import mark_safe
import pytz
import markdown2

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

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)

    return mark_safe(html_body)
