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
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.profile.password.interfaces import IGSPasswordUser
from gs.profile.signup.base.setpassword import SetPasswordForm


class FBSetPasswordForm(SetPasswordForm):
    pageTemplateFileName = 'browser/templates/setpassword.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    @form.action(label=u'Set', failure='handle_set_action_failure')
    def handle_set(self, action, data):
        assert self.context
        assert self.form_fields
        assert action
        assert data

        pu = IGSPasswordUser(self.userInfo)
        pu.set_password(data['password1'])

        userInfo = createObject('groupserver.LoggedInUser', self.context)
        uri = '%s/fb_register_profile.html' % userInfo.url
        cf = str(data.get('came_from'))
        if cf == 'None':
            cf = ''
        gid = str(data.get('groupId'))
        if gid == 'None':
            gid = ''
        uri = '%s?form.joinable_groups:list=%s&form.came_from=%s' %\
            (uri, gid, cf)

        return self.request.response.redirect(uri)
