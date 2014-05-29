from django import template
from django.template import Context
from django.template.loader import get_template

from widget_tweaks.templatetags.widget_tweaks import append_attr

from geelweb.django.twitter_bootstrap_form import settings

register = template.Library()

@register.filter
def twitter_bootstrap(element, args=""):
    """
    valid layouts are:
    - default
    - search
    - inline
    - horizontal

    {{ form|twitter_bootstrap:"default" }}
    {{ form|twitter_bootstrap:"horizontal" }}
    {{ form|twitter_bootstrap:"horizontal,[xs,sm,md,lg],[1-12],[1-12]" }}
    """
    element_type = element.__class__.__name__.lower()

    args_list = [arg.strip() for arg in args.split(',')]

    layout = (len(args_list) and args_list[0]) or "default"
    size = (len(args_list) > 1 and args_list[1]) or "sm"
    label_cols = (len(args_list) > 2 and args_list[2]) or "2"
    input_cols = (len(args_list) > 3 and args_list[3]) or str(12 - int(label_cols))

    lbl_size_class = "col-%s-%s" % (size, label_cols)
    lbl_size_offset_class = "col-%s-offset-%s" % (size, label_cols)
    ipt_size_class = "col-%s-%s" % (size, input_cols)

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
            'lbl_size_class': lbl_size_class,
            'lbl_size_offset_class': lbl_size_offset_class,
            'ipt_size_class': ipt_size_class,
            'required_suffix': settings.BOOTSTRAP_REQUIRED_SUFFIX,
            'field_template': "twitter_bootstrap_form/%s" % field_template_file})

    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"

@register.filter
def is_file(field):
    return field.field.widget.__class__.__name__.lower() == "clearablefileinput"


@register.filter
def add_class(field, css_class):
    return append_attr(field, 'class:' + css_class)
