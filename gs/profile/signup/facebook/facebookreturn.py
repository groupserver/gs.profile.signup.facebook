# coding=utf-8
from Products.CustomUserFolder.interfaces import IGSUserInfo
from Products.GSProfile.utils import login, create_user_from_email
from Products.GSProfile.profileaudit import *
from gs.auth.oauth.client.facebook import decode_parameters, FacebookAuth
from gs.group.base.page import GroupPage
from gs.option import ComponentOptions
from gs.profile.email.verify.emailverificationuser import EmailVerificationUser

import logging
log = logging.getLogger('gs.profile.signup.facebook')


class GSFacebookRegistrationReturn(GroupPage):
    '''View object for the GroupServer Facebook Registration Return page'''
    def __init__(self, context, request):
        super(GSFacebookRegistrationReturn, self).__init__(context, request)
        self.user_data = {}

        self.facebook_auth()
        user = None

        if self.user_data and ('email' in self.user_data):
            log.info("Signup from facebook user: %s" % self.user_data['email'])
            try:
                user = self.create_user()
            except:
                log.info("User %s already existed." % self.user_data['email'])
                uri = u"/request_registration.html?email=%s" %\
                    self.user_data['email']
        else:
            log.info("Signup from facebook user had no email")
            uri = u"/request_registration.html?email="

        if user:
            state = None
            if 'state' in self.request.form:
                state = decode_parameters(self.request.form['state'])
            if state:
                uri = u'/p/%s/fb_register_password.html?%s' %\
                        (user.getId(), state)
            else:
                uri = u'/p/%s/fb_register_password.html' % user.getId()

        self.request.response.redirect(uri)

    def facebook_auth(self):
        redirect_uri = '%s/facebook_register_return.html' % self.siteInfo.url

        log.info('Attempting facebook oauth')

        if 'code' in self.request:
            code = self.request['code']
        else:
            # TODO: Do something if auth fails or is rejected
            pass

        options = ComponentOptions(self.context, "gs.profile.signup.facebook")
        app_id = options.get("app_id")
        app_secret = options.get("app_secret")
        assert (app_id and app_secret),\
            "Both app_id and app_secret must be specified"
        fba = FacebookAuth(redirect_uri, app_id, app_secret)
        request = {'code': code}
        fba.complete_auth(request)
        log.info('Completed facebook auth')
        self.user_data = fba.data()
        log.info('Received user data from facebook: %s' % self.user_data)

    def create_user(self):
        email = self.user_data['email']
        user = create_user_from_email(self.context, email)
        first_name = self.user_data['first_name']
        last_name = self.user_data['last_name']
        fn = '%s %s' % (first_name, last_name)
        user.manage_changeProperties(fn=fn, givenName=first_name,
                                        familyName=last_name)

        userInfo = IGSUserInfo(user)
        login(self.context, user)
        vid = 'AssumedTrue%s' % email.replace('@', 'at')
        eu = EmailVerificationUser(self.context, userInfo, email)
        eu.add_verification_id(vid)
        eu.verify_email(vid)

        return user
