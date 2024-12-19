"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from yatl.helpers import A

# added from documentation
#from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.form import Form
#from pydal.validators import *

from py4web import URL, abort, action, redirect, request

from .common import (T, auth, authenticated, cache, db, flash, logger, session,
                     unauthenticated)

# declaring basic user group
is_basic_user = Condition(lambda: 'basic' in groups.get(auth.user_id))
is_manager = Condition(lambda: 'manager' in groups.get(auth.user_id))
is_ameer = Condition(lambda: 'ameer' in groups.get(auth.user_id))
is_tech = Condition(lambda: 'tech' in groups.get(auth.user_id))

@action("tajneed")
@action.uses("generic.html", db, auth)
def tajneed():
	user = auth.get_user()
	form = Form(db.tajneed)
	if form.accepted:
	    flash.set = "Form Accepted"
	return dict(user = user, form= form)

@action("index")
@action.uses("generic.html", auth.user)
def index():
	user = auth.get_user()
	if user.group == "basic":
		redirect(URL("basic_user"))
	return dict(user=user)

@action("basic_user")
@action.uses("report.html", auth.user, is_basic_user)
def basic_user():
	user = auth.get_user()
	tajneed_data = db(db.tajneed).select().as_list()
	return dict(user= user, tajneed_data=tajneed_data)
	
