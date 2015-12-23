from django import template

register = template.Library()


class BizzFuzzNode(template.Node):
    def __init__(self, random_number):
        self.random_number = template.Variable(random_number)

    def render(self, context):
        random_number = self.random_number.resolve(context)

        out = ''
        if random_number % 3 == 0:
            out += 'Bizz'
        if random_number % 5 == 0:
            out += 'Fuzz'
        if out == '':
            out = random_number

        return out


@register.tag
def bizzfuzz(parser, token):
    try:
        tag_name, random_number = token.split_contents()
    except ValueError: # pragma: no cover
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])

    return BizzFuzzNode(random_number)
