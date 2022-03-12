import sqlite3

db = "sql.db"


class Database:
    def get_user_50(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user ORDER BY id LIMIT 50")
        a = cursor.fetchall()
        connection.close()
        return a
    def get_user_by_id(self,user_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM user WHERE user_id = {user_id}")
            a = cursor.fetchone()
            connection.close()
            return a
        except Exception as e:
            print(e)
    def get_today_app_(self,date):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM application WHERE created_date LIKE '%{date}%'")
            a = cursor.fetchall()
            connection.close()
            return a
        except Exception as e:
            print(e)

    def update_user_fullname(self,chat_id,fullname):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"UPDATE user SET fullname={fullname} WHERE user_id={chat_id}")
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return False

    def update_user_language(self,chat_id,lang):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"UPDATE user SET language='{lang}' WHERE user_id={chat_id}")
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False
    def update_user_phone_number(self,chat_id,phone):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"UPDATE user SET phone='{phone}' WHERE user_id={chat_id}")
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)
            return False
    def get_all_serviec(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM service")
            b = cursor.fetchall()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False
    def get_all_service_by_id(self,id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM service WHERE id={id}")
            b = cursor.fetchone()
            connection.close()
            if b is None:
                b = [1,'Service not found']
            return b
        except Exception as e:
            print(e)
            return False
    def get_id(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT user_id FROM user")
            b = cursor.fetchall()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False

    def add_user_to_database(self,lang,phone, fullname, userID, username):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO user(fullname,username,phone,language,user_id) VALUES("{fullname}","{username}","{phone}","{lang}",{userID})')
            connection.commit()
            connection.close()
        except Exception:
            pass

    def insert_application_data(self, job, service_type, adress, parametr, condition, application_time, created_date,userid):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO application(job, service_type, adress, parametr, condition, application_time, created_date,userid)"""
                           f"""VALUES("{job}",{service_type},"{adress}","{parametr}","{condition}","{application_time}","{created_date}",{userid})""")
            connection.commit()
            d = cursor.execute(f"SELECT id FROM application WHERE (userid = {userid} AND application_time='{application_time}')")
            a = d.fetchone()
            connection.close()
            return a
        except Exception as e:
            print(e)
            return False
    def add_photo_to_database(self,url,appeal_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO images(url,appeal_id) VALUES("{url}",{appeal_id})')
            connection.commit()
            connection.close()
        except Exception:
            pass
    def get_admin(self):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admin")
        a = cursor.fetchall()
        connection.close()
        return a

    def get_one_admin(self,chat_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM admin WHERE chat_id={chat_id}")
            a = cursor.fetchone()
            connection.close()
            return a
        except  Exception  as e:
            pass

    def add_admin(self,userID,username,date):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO admin(chat_id,date,username) VALUES({userID},"{date}","{username}")')
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)

    def add_service(self,uz_latn,uz_cyrl,ru,userID,date):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO service(name_uz_latn,name_uz_cyrl,name_ru,user_id,created_date) VALUES("{uz_latn}","{uz_cyrl}","{ru}",{userID},"{date}")')
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(e)

    def delete_service(self, id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM service WHERE id={id}")
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return e

    def delete_admin(self, chat_id):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM admin WHERE chat_id={chat_id}")
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            return e
    def get_all_serviec_COUNT(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(id) FROM service")
            b = cursor.fetchone()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False
    def get_all_application_COUNT(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(id) FROM application")
            b = cursor.fetchone()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False
    def get_all_admin_COUNT(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(id) FROM admin")
            b = cursor.fetchone()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False
    def get_all_user_COUNT(self):
        try:
            connection = sqlite3.connect(db)
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(id) FROM user")
            b = cursor.fetchone()
            connection.close()
            return b
        except Exception as e:
            print(e)
            return False