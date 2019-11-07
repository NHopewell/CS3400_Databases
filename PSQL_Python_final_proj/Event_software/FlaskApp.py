from flask import Flask, render_template, request, session
import requests
from User import User
from Database import CursorFromConnectionFromPool

app = Flask(__name__)  # app constains Flask object with one passed param


''' Below is a Python decorator, it says, when we access the '/clients' end
    point, what should be returned'''


@app.route('/Clients')  # setting what will happen when we access the home page
def clients_page():
    return render_template("clients_f.html")


@app.route('/Events')  # setting what will happen when we access the home page
def events_page():
    return render_template("events_f.html")


@app.route('/Clients', methods = "POST")  # setting what will happen when we access the home page
def events_page_post():
    client = []
    client_dict = {
                    'client_email': request.form['email'],
                    'client_pnum': request.form['pnum'],
                    'client_first_name': request.form['fname'],
                    'client_last_name': request.form['lname'],
                    'client_membership': request.form.get('MembershipLevel')
                  }
    for key, value in client_dict.items():
        client.append(value)

    with CursorFromConnectionFromPool() as cursor:
        cursor.execute('INSERT INTO client (client_email, client_pnumber, first_name, last_name, '
                       'membership_level)'
                       'VALUES (%s, %s, %s, %s, %s)',
                       (client[0], client[1], client[2], client[3], client[4]))



    #return User(client_email, client_pnum, client_first_name, client_last_name, client_membership, client_membership )


if __name__=='__main__':
    app.run(debug=True)




#app.run(port = 5998)