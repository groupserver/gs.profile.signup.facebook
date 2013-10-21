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
from zope.formlib import form
from Products.Five.browser.pagetemplatefile \
    import ZopeTwoPageTemplateFile
from Products.GSProfile.profileaudit import *
from gs.profile.signup.base.changeprofile import ChangeProfileForm


class FBChangeProfileForm(ChangeProfileForm):
    pageTemplateFileName = 'browser/templates/fb-changeprofile.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    @form.action(label=u'Finish', failure='handle_set_action_failure')
    def handle_set(self, action, data):
        self.auditer = ProfileAuditer(self.context)
        self.actual_handle_set(action, data)\

        cf = str(data.pop('came_from'))
        if cf == 'None':
            cf = ''
        if self.user_has_verified_email:
            uri = str(data.get('came_from'))
            if uri == 'None':
                uri = '/'
            uri = '%s?welcome=fb_signup' % uri
        else:
            email = self.emailUser.get_addresses()[0]
            uri = 'verify_wait.html?form.email=%s&form.came_from=%s' %\
              (email, cf)

        return self.request.RESPONSE.redirect(uri)
