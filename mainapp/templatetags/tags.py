from django import template

register = template.Library()


@register.filter()
def mymedia(image):
    if image:
        return f'/media/{image}'

    return '#'
