# coding=utf-8
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from Products.CustomUserFolder.userinfo import GSUserInfo
from gs.content.form.form import SiteForm
from gs.profile.email.base.emailuser import EmailUser
from gs.profile.password.interfaces import IGSPasswordUser
from gs.profile.signup.interfaces import IGSSetPasswordRegister

import gs.profile.signup.setpassword

class FBSetPasswordForm(gs.profile.signup.setpassword.SetPasswordForm):
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