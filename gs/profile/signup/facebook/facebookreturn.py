# coding=utf-8
from Products.Five import BrowserView
from zope.component import createObject

class GSFacebookRegistrationReturn(BrowserView):
    '''View object for the GroupServer Facebook Registration Return page'''
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.siteInfo = createObject('groupserver.SiteInfo', context)
        self.groupInfo = createObject('groupserver.GroupInfo', context)

