from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)

db = MySQL(app)

@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        user = User(0,request.form['user'],request.form['password'])
        print(user.username)
        print(user.password)
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return render_template('inicio.html')
            else:
                return redirect(url_for('fallido'))
        else:
            return redirect(url_for('fallido'))
    else:
        return render_template('inicio.html')
    
@app.route('/fallido')
def fallido():
    return render_template('fallido.html')
    
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()