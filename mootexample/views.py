"""

    Moot.it forum integration with Django and Python

    var sso_config = {


   key: 'testapikey',


   message: message,


   timestamp: timestamp,


   signature: SHA1('testapisecretkey' + ' ' + message + ' ' + timestamp)


}


"""

import base64
import json
import time
import hashlib
import math
import os

from django.shortcuts import render_to_response

from django.template import RequestContext

# Moot.it credentials
API_KEY = os.environ.get("MOOT_IP_API_KEY")
API_SECRET = os.environ.get("MOOT_IP_API_SECRET")


def create_moot_config(request):
    """ Create Moot.it configuration object """

    # Map Django users to Moot.it users
    if request.user.is_anonymous():
        user = None
        displayname = None
        is_admin = False
        email = "noreply@example.com"
    else:
        user = request.user.username
        displayname = request.user.username
        is_admin = request.user.is_staff
        email = "noreply@example.com"

    # user config
    config = dict(id=user, displayname=displayname, avatar=None, is_admin=is_admin, email=email)

    message = base64.b64encode(json.dumps(config))
    timestamp = str(math.floor(time.time()))

    signature = hashlib.sha1(API_SECRET + ' ' + message + ' ' + timestamp).hexdigest()

    # single sign on config
    sso_config = dict(key=API_KEY, timestamp=timestamp, message=message, signature=signature)

    return json.dumps(sso_config), locals()


def forum(request):
    """ Render main page with forums JavaScript embed """

    sso_config, used_params = create_moot_config(request)

    # Debugging data for Courtney
    id = used_params["user"]
    displayname = used_params["displayname"]
    is_admin = used_params["is_admin"]
    email = used_params["email"]

    resp = render_to_response("forum.html",
                              locals(),
                              context_instance=RequestContext(request))
    return resp
