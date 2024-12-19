"""
This file defines the database models
"""

from pydal.validators import *

from .common import Field, db

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

# expose db here
db.define_table("tajneed",
    Field("total_number_of_members", "integer", requires=IS_NOT_EMPTY()),
    Field("number_of_men", "integer", requires=IS_NOT_EMPTY()),
    Field("number_of_women", "integer", requires=IS_NOT_EMPTY()),
    Field("number_of_ansar", "integer", requires=IS_NOT_EMPTY()),
    Field("Number_of_khuddam", "integer" ,requires=IS_NOT_EMPTY()),
    Field("number_of_atfal", "integer", requires=IS_NOT_EMPTY()),
    Field("number_of_lajna", "integer", requires=IS_NOT_EMPTY()),
    Field("date_of_submission", "date", requires=IS_NOT_EMPTY())
)
db.define_table('tabliq',
	Field("topic", "text", requires=IS_NOT_EMPTY()),
	Field("location", "text", requires=IS_NOT_EMPTY()),
	Field("number_present", "integer", requires=IS_NOT_EMPTY()),
	Field("number_of_converts", "integer", requires=IS_NOT_EMPTY()),
	Field("")
)
db.commit()
