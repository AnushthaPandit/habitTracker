import dbconnection

def get_user_details_by_email(email=""):
    conn = dbconnection()
    user = conn.execute("SELECT * FROM users WHERE email = ?",(email,)).fetchone()
    conn.close()
    return user