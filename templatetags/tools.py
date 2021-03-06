from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from toolbox.tools import is_local
from toolbox.models import ResponsiveImage

register = template.Library()


@register.tag(name="IsLocal")
def is_local():
    return is_local(settings.FQDN)


@register.inclusion_tag('toolbox/responsive_image.html')
def render_responsive_image(image: ResponsiveImage, alt: str):
    return {
        'xl': {'image': image.xl, 'size': 1200},
        'lg': {'image': image.lg, 'size': 992},
        'md': {'image': image.md, 'size': 768},
        'sm': {'image': image.sm, 'size': 576},
        'xs': {'image': image.xs, 'size': 320},
        'alt': alt,
    }


@register.inclusion_tag('toolbox/form_errors.html')
def render_form_errors(errors: list):
    return {
        'errors': errors,
    }


@register.filter('getOrDefault')
@stringfilter
def get_or_default(value, default=''):
    return value if value else default
