from datetime import date
from dateutil.relativedelta import relativedelta
from django import template

register = template.Library()


class EligibleNode(template.Node):
    def __init__(self, birthday):
        self.birthday = template.Variable(birthday)

    def render(self, context):
        birthday = self.birthday.resolve(context)

        td = relativedelta(date.today(), birthday)

        return td.years > 13 and 'allowed' or 'blocked'


@register.tag
def eligible(parser, token):
    try:
        tag_name, birthday = token.split_contents()
    except ValueError: # pragma: no cover
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])

    return EligibleNode(birthday)
