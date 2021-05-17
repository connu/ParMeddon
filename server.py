from flask import Flask,render_template,url_for,redirect, request, jsonify
from flask.helpers import flash
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g
import os

import json

app = Flask(__name__)

tasks_count_for_the_specific_user = 0


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///users.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


#check if anything has been deleted
    

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password =  db.Column(db.String(250), unique=False, nullable=False)
    username =  db.Column(db.String(250), unique=True, nullable=False)

    tasks = db.relationship('Tasks', backref='author')
    notes = db.relationship('Notes', backref='user')



class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False, unique=False)
    date = db.Column(db.String(100), nullable=False, unique=False)
    tags = db.Column(db.String(100), nullable=False, unique=False)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(2000), nullable=True, unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


@app.route('/delete', methods=["POST","GET"])
def delete():
    if request.method == "POST":
        task = request.form['javascript_data']


        db_tasks = db.session.query(Tasks).filter_by(text=task).first()
        if db_tasks:
            db.session.delete(db_tasks)
            db.session.commit()
        else:
            pass
        return 'deleted'

    return 'deleted'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated is False:
            flash('You Must Be Logged In')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['POST', 'GET'])
def home():
    if 'email'  and 'username' and 'password' in request.args:         
            password = generate_password_hash(request.args['password'], method='pbkdf2:sha256',salt_length=8)

            new_user = Users(
                email=request.args['email'],
                password=password,
                username=request.args['username']
            )
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('dashboard'))
          
    return render_template('index.html', is_authenticated=current_user.is_authenticated)

@app.route('/login', methods=['POST','GET'])
def login(): 
    if 'email' and 'password' in request.args: 
        login_usern = db.session.query(Users).filter_by(email=request.args['email']).first()
        if not login_usern:
            flash('Wrong Credentials')
            return redirect(url_for('login'))
        elif check_password_hash(login_usern.password, request.args['password']):
            login_user(login_usern)
            return redirect(url_for('dashboard'))
        
        elif check_password_hash(login_usern.password, request.args['password']):
            flash('Wrong Credentials')
            return redirect(url_for('login'))
            

    return render_template('login.html', is_authenticated=current_user.is_authenticated)



@app.route('/home', methods=["GET","POST"])
@login_required
def dashboard():   
    g.user = current_user.get_id()
    all_tasks = db.session.query(Tasks).filter_by(author_id=g.user).all()

    user = db.session.query(Users).filter_by(id=g.user).first()
    return render_template('dash.html', tasks=all_tasks, user=user, count=tasks_count_for_the_specific_user)


@app.route('/convince')
@login_required
def convince():
    return "Coming Soon! || Go Back To <a href='/home'>DashBoard?</a>"


#responsible for the database delete cards


@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html')
    
@app.route('/create', methods=['POST','GET'])
@login_required
def task():

    if 'task' and 'tags' and 'date' in request.args:
        
        
        date = request.args['date'].split('-')

        # month name
        datetime_object = datetime.strptime(date[1], "%m")
        month_name = datetime_object.strftime("%b")


        date_production = f'{month_name} {date[2]}th {date[0]}'

        #getting the tags

        tags = request.args['tags']

        g.user = current_user.get_id()
        username = db.session.query(Users).filter_by(id=g.user).first()

        new_task = Tasks(
            text=request.args['task'],
            date= date_production,
            tags=tags,
            author=username
            )
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('dashboard'))
       
    return render_template('newtask.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug='true')




