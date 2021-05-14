from flask import Flask,render_template,url_for,redirect, request
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from functools import wraps



app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password =  db.Column(db.String(250), unique=False, nullable=False)
    username =  db.Column(db.String(250), unique=True, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated is False:
            return 'You Must Be Logged In'
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['POST', 'GET'])
def home():

    if 'email'  and 'username' and 'password' in request.args:
        new_user = Users(
            email=request.args['email'],
            password=request.args['password'],
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

        if str(request.args['password']) == login_usern.password:
            login_user(login_usern)
            return redirect(url_for('dashboard'))

        else:
            return 'wrong password'

    return render_template('login.html', is_authenticated=current_user.is_authenticated)

@app.route('/home')
@login_required
def dashboard():
    return render_template('dash.html')



if __name__ == "__main__":
    app.run(debug="true")

