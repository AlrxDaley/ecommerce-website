from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def clac_subtotal(price, quantity):
    return price * quantity