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
from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface


class IGSProfileSignupFacebook(zope.interface.Interface):
    app_id = zope.schema.TextLine(
                title=u"Application ID as supplied by Facebook",
                required=True)
    app_secret = zope.schema.TextLine(
                title=u"Application Secret as supplied by Facebook",
                required=True)


class GSPSFOFactory(GSOptionConverterFactory):
    interface = IGSProfileSignupFacebook