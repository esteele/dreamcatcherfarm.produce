from five import grok
from zope import schema

from plone.directives import form, dexterity
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget


class IProduce(form.Schema):

    body = schema.Text(
            title=u"Body text",
            required=False,
            default=u"Body text goes here"
        )
    form.widget(body=WysiwygFieldWidget)


class Produce(dexterity.Item):
    grok.implements(IProduce)
