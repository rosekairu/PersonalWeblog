from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def split(value, arg):
    return value.split(arg)


@register.filter
@stringfilter
def insert_image(value, image_path):
    if image_path:
        # Replace a specific placeholder (e.g., "{{ image_here }}") in the content with the image HTML code
        value = value.replace("{{ image_here }}", '<img src="{}" alt="Image Description">'.format(image_path))
    return value

