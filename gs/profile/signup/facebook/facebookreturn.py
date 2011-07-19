# coding=utf-8
from Products.Five import BrowserView
from zope.component import createObject
from gs.auth.oauth.client.facebook import FacebookAuth
from Products.GSProfile.utils import login, create_user_from_email
from Products.GSProfile.profileaudit import *
from Products.CustomUserFolder.interfaces import IGSUserInfo
from gs.profile.email.verify.emailverificationuser import EmailVerificationUser
from gs.auth.oauth.client.facebook import decode_parameters

import logging
log = logging.getLogger('gs.profile.signup.facebook')

# TODO: obviously these shouldn't be hard coded here
app_id='139144879494776'
app_secret='8190ec7c0375638b0a612f2f92901445'

class GSFacebookRegistrationReturn(BrowserView):
    '''View object for the GroupServer Facebook Registration Return page'''
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.user_data = {}
        
        self.siteInfo = createObject('groupserver.SiteInfo', context)
        self.groupInfo = createObject('groupserver.GroupInfo', context)
        self.facebook_auth()
        user = None
        
        if self.user_data and self.user_data.has_key('email'):
            log.info("Signup from facebook user: %s" % self.user_data['email'])
            try:
                user = self.create_user()
            except:
                pass
        else:
            # TODO: redirect to usual registration process, we have no verified email
            log.info("Signup from facebook user had no email")

        if user:
            state = None
            if self.request.form.has_key('state'):
                state = decode_parameters(self.request.form['state'])
            if state:
                uri = '/p/%s/fb_register_password.html?%s' % (user.getId(),state)
            else:
                uri = '/p/%s/fb_register_password.html' % user.getId()
                
            self.request.response.redirect(uri)

    def facebook_auth(self):
        redirect_uri='http://test.forums.e-democracy.org/facebook_register_return.html'

        if self.request.has_key('code'):
            code = self.request['code']
        else:
            # TODO: Do something if auth fails or is rejected
            pass
        
        fba = FacebookAuth(redirect_uri,app_id,app_secret)
        request = {'code': code}
        fba.complete_auth(request)
        self.user_data = fba.data()
        
    def create_user(self):
        email = self.user_data['email']
        user = create_user_from_email(self.context, email)
        first_name = self.user_data['first_name']
        last_name = self.user_data['last_name']
        fn = '%s %s' % (first_name, last_name)
        user.manage_changeProperties(fn=fn,givenName=first_name,familyName=last_name)
        
        userInfo = IGSUserInfo(user)
        login(self.context, user)
        vid = 'AssumedTrue%s' % email.replace('@', 'at')
        eu = EmailVerificationUser(self.context, userInfo, email)
        eu.add_verification_id(vid)
        eu.verify_email(vid)
        
        return user