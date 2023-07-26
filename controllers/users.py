from services.users import get_user_details_by_email
from flask import make_response

def is_valid_creds(email, password):
   user = get_user_details_by_email(email)
   if(user is None):
      return True
   else:
    return True
