from django import template

register = template.Library()


@register.filter()
def mymedia(image):
    if image:
        return f'/media/{image}'

    return '#'


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()