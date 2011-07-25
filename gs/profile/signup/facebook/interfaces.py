from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface

class IGSProfileSignupFacebook(zope.interface.Interface):
    app_id = zope.schema.TextLine(title=u"Application ID as supplied by Facebook",
                                  required=True)
    app_secret = zope.schema.TextLine(title=u"Application Secret as supplied by Facebook",
                                  required=True)
    
class GSPSFOFactory(GSOptionConverterFactory):
    interface = IGSProfileSignupFacebook