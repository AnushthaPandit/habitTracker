import dbconnection

def insert_habit(title="", duration=0, user_id=0):
    conn = dbconnection()
    habit = conn.execute("insert into habits (title, duration, user_id) values (?, ?, ?) RETURNING id",(title, duration, user_id)).fetchone()
    conn.commit()
    conn.close()
    (id, ) = habit if habit else None
    return id

def upadte_habit(title="", duration=0, habit_id=0):
    conn = dbconnection()
    conn.execute("UPDATE habits SET title = ?, duration = ? WHERE id = ?",(title, duration, habit_id))
    conn.commit()
    conn.close()
    return True

def get_habits_by_user_id(user_id=0):
    conn = dbconnection()
    habits = conn.execute("select * from habits where user_id=?",(user_id,)).fetchall()
    conn.commit()
    conn.close()
    return habits


def delete_habit_by_id(id=0):
    conn = dbconnection()
    conn.execute("delete from habits where id=?",(id,))
    conn.commit()
    conn.close()
    return True

def get_habit_by_id(id=0):
    conn = dbconnection()
    habit = conn.execute("SELECT * FROM habits WHERE id = ?",(id,)).fetchone()
    conn.close()
    return habit