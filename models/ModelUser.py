from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, user, password FROM users WHERE user = '{}'".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password))
                print(user.password)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)