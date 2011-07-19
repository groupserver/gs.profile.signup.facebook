from gs.auth.oauth.client.facebook import auth_url, encode_parameters

class FacebookSignup(object):
    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.redirect_uri = 'http://test.forums.e-democracy.org/facebook_register_return.html'
        self.scope = 'email'
        self.client_id = '139144879494776'
        self.state = encode_parameters(self.request.form)
        self.auth_url = auth_url(redirect_uri='http://test.forums.e-democracy.org/facebook_register_return.html',
                                 client_id='139144879494776')
    