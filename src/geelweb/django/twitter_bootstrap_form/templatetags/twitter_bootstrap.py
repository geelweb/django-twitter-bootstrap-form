from django import template
from django.template import Context
from django.template.loader import get_template

register = template.Library()

@register.filter
def twitter_bootstrap(element, layout="default"):
    """
    valid layouts are:
    - default
    - search
    - inline
    - horizontal
    """
    element_type = element.__class__.__name__.lower()

    if layout not in ["default", "search", "inline", "horizontal"]:
        layout = "default"

    if element_type == 'boundfield':
        pass
    else:

        if layout == "default":
            field_template_file = "field.html"
        else:
            field_template_file = "%s_field.html" % layout

        template = get_template("twitter_bootstrap_form/form.html")
        context = Context({
            'form': element,
            'layout': layout,
            'field_template': "twitter_bootstrap_form/%s" % field_template_file})

    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"

