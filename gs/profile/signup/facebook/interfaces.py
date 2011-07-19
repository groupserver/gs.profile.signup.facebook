from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface

class IGSProfileSignupFacebookOptions(zope.interface.Interface):
    app_id = zope.schema.Text()
    
class GSPSFOFactory(GSOptionConverterFactory):
    interface = IGSProfileSignupFacebookOptions