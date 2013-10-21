# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
###############################################################################
from zope.component import createObject
from gs.auth.oauth.client.facebook import auth_url, encode_parameters
from gs.option import ComponentOptions


class FacebookSignup(object):
    def __init__(self, context, request, view, manager):
        self.siteInfo = createObject('groupserver.SiteInfo', context)
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        u = '{0}/facebook_register_return.html'
        self.redirect_uri = u.format(self.siteInfo.url)
        self.scope = 'email'
        options = ComponentOptions(self.context, "gs.profile.signup.facebook")
        self.app_id = options.get("app_id")
        self.state = encode_parameters(self.request.form)
        self.auth_url = auth_url(redirect_uri=u.format(self.siteInfo.url),
                                 client_id=self.app_id)

        self.show = self.app_id and True or False
