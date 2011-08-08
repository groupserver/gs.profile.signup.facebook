from gs.auth.oauth.client.facebook import auth_url, encode_parameters
from gs.option import ComponentOptions

class FacebookSignup(object):
    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.redirect_uri = 'http://test.forums.e-democracy.org/facebook_register_return.html'
        self.scope = 'email'
        options = ComponentOptions(self.context, "gs.profile.signup.facebook")
        self.app_id = options.get("app_id")
        self.state = encode_parameters(self.request.form)
        self.auth_url = auth_url(redirect_uri='http://test.forums.e-democracy.org/facebook_register_return.html',
                                 client_id=self.app_id)

        self.show = self.app_id and True or False