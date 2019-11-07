from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from User import User
from Database import CursorFromConnectionFromPool
from Database import Database

DBNAME = "Event_planner_db"
DBHOST = "localhost"
DBUSER = "postgres"
DBPASS = "Hopeless14"

# settings
app = Flask(__name__)
app.secret_key = "Hopeless14"

Database.initialise(database = DBNAME, host = DBHOST, user = DBUSER, password = DBPASS )

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/Event_planner_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class return_user(db.Model):
    email = db.     Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(200), unique=False)
    last_name = db.Column(db.String(200), unique=False)
    membership_level = db.Column(db.String(100), unique=False)
    id = db.Column(db.Integer(), primary_key=True)

    def __init__(self, email, phone_number, first_name, last_name, membership_level):
        self.email = email
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.membership_level = membership_level




        #self.id = id


# Declaring Flask WTF-Form
class PostForm(FlaskForm):
    email = StringField('Title', validators=[DataRequired()])
    phone_number = StringField('Phone_Number', validators=[DataRequired()])
    first_name = StringField('First_Name', validators=[DataRequired()])
    last_name = StringField('Last_name', validators=[DataRequired()])
    membership_level = StringField('Membership_Level', validators=[DataRequired()])


@app.route('/Client', methods=['GET', 'POST'])
def add_post():
    postform = PostForm()
    if request.method == 'POST':
        pf = return_user(
            postform.email.data,
            postform.phone_number.data,
            postform.first_name.data,
            postform.last_name.data,
            postform.membership_level.data
        )
        new_client= User(pf.email, pf.phone_number, pf.first_name, pf.last_name, pf.membership_level)
        new_client.save_to_db()
        # with CursorFromConnectionFromPool() as cursor:
        #     cursor.execute('INSERT INTO client (client_email, client_pnumber, first_name, last_name, '
        #                    'membership_level)'
        #                    'VALUES (%s, %s, %s, %s, %s)',
        #                    (pf.email, pf.phone_number, pf.first_name, pf.last_name, pf.membership_level))
        return redirect(url_for('showbio'
                        ))
    return render_template('clients.html', postform = postform)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# @app.route('/Client', methods=['POST', 'GET'])
# def client_data_form():
#     if request.method == "POST":
#         email = request.form['InputEmail']
#         phone_number = request.form['InputPhoneNum']
#         first_name = request.form['InputFirstName']
#         last_name = request.form['InputLastName']
#         membership_level =  request.form['MembershipLevel']
#         return redirect(url_for('showbio',
#                                 first_name = first_name,
#                                 last_name = last_name,
#                                 email = email,
#                                 phone_number = phone_number))
#     return render_template("clients.html")
#
#
@app.route('/showbio', methods=['GET'])
def showbio():
    email = request.args.get('InputEmail')
    phone_number = request.args.get('InputPhoneNum')
    first_name = request.args.get('InputFirstName')
    last_name = request.args.get('InputLastName')
    return render_template('bio_form.html',
                                first_name = first_name,
                                last_name = last_name,
                                email = email,
                                phone_number = phone_number)






if __name__ =="__main__":
    app.run(debug=True, port=8080)

