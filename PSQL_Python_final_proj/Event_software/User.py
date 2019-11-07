from Database import CursorFromConnectionFromPool


class User:
    # properties of User() objects
    def __init__(self, email, phone_number, first_name, last_name, membership_level, id = None):
        self.email = email
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.membership_level = membership_level
        self.id = id


    # display when printing
    def __repr__(self):
        return(f"<User: {self.first_name} {self.last_name}\nEmail: {self.email}\n")


    # saves a users information into clients table in database
    def save_to_db(self):
        '''dont need commit() and connect() using with instead
           at the end of the with statement, psycopg will automatically commit and close it
           get a connection if one is available from the connection pool within database.py'''
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO client (client_email, client_pnumber, first_name, last_name, '
                           'membership_level)'
                           'VALUES (%s, %s, %s, %s, %s)',
                           (self.email, self.phone_number, self.first_name, self.last_name,
                            self.membership_level))  # closes and commits again


    @classmethod
    # loads a user from the clients table in the database via their email address
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM client WHERE client_email = %s', (email, )) # NOTICE COMMA AFTER PARAMETER HERE - expects a tupple
            user_data = cursor.fetchone()
            if user_data:  # if user exists in db (same as 'if user_data is not None:')
                return cls(email = user_data[1], phone_number= user_data[2], first_name= user_data[3],
                           last_name = user_data[4], membership_level= user_data[5],
                           id = user_data[0])   # in the db, id is first colunm
            else:
                print("User email does not currently exist in the database.")

            # return new object of type user, using data in the db row (fetchone = fetch one row)
            # else, return None by default (python will always return None by default)


    # remove a user from the clients table in the database via their email address
    @classmethod
    def delete_user_from_db(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('DELETE FROM client WHERE client_email = %s', (email, ))
            print(f"User with that email address '{email}' has been successfully removed.")
