from services.users import get_user_details_by_email

def is_valid_creds(email, password):
   user = get_user_details_by_email(email)
   if(user is None):
      return False
   else:
    if(user["email"] == email and user['pass']==password):
      return True
    else:
      return False
