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
import sys

from django.shortcuts import render_to_response

from django.template import RequestContext

# Moot.it credentials
API_KEY = os.environ.get("MOOT_IT_API_KEY")
API_SECRET = os.environ.get("MOOT_IT_API_SECRET")
FORUM_URL = os.environ.get("MOOT_IT_FORUM_URL")

if not API_KEY:
    sys.exit("Please give API key on the command line")


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
    config = dict(user=dict(id=user, displayname=displayname, avatar="http://foobar", is_admin=is_admin, email=email))
    print "Config %s" % json.dumps(config)

    message = base64.b64encode(json.dumps(config))
    timestamp = str(int(math.floor(time.time())))

    print "User %s" % user
    print "Message %s" % message
    print "Timestamp %s" % timestamp

    signature = hashlib.sha1(API_SECRET + ' ' + message + ' ' + timestamp).hexdigest()
    print "Signature %s" % signature

    # single sign on config
    sso_config = dict(key=API_KEY, timestamp=timestamp, message=message, signature=signature)

    config = json.dumps(sso_config)
    print "sso_config %s" % config

    return config


def forum(request):
    """ Render main page with forums JavaScript embed """

    sso_config = create_moot_config(request)

    forum_url = FORUM_URL

    # Debugging data for Courtney
    resp = render_to_response("forum.html",
                              locals(),
                              context_instance=RequestContext(request))
    return resp
