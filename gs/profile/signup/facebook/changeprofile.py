# coding=utf-8
from zope.component import createObject
from zope.formlib import form
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm
from Products.Five.browser.pagetemplatefile \
    import ZopeTwoPageTemplateFile
from Products.CustomUserFolder.interfaces import IGSUserInfo
from Products.XWFCore.XWFUtils import get_the_actual_instance_from_zope
from Products.GSProfile import interfaces
from Products.GSProfile.profileaudit import *
from Products.GSProfile.edit_profile import EditProfileForm,\
    select_widget, wym_editor_widget, multi_check_box_widget
from Products.GSProfile.utils import profile_interface_name, \
    profile_interface, enforce_schema
from gs.group.member.join.interfaces import IGSJoiningUser
from gs.group.member.invite.inviter import Inviter
from gs.profile.email.base.emailuser import EmailUser
import gs.profile.signup.changeprofile

class FBChangeProfileForm(gs.profile.signup.changeprofile.ChangeProfileForm):
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
    