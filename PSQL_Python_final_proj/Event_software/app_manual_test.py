from User import User
from Database import Database
import os
import json
from Purchases import Purchases
from Event import Event


### This is a manual test file for the app to make sure it works ###

DBNAME = "Event_planner_db"
DBHOST = "localhost"
DBUSER = "postgres"
DBPASS = "Hopeless14"

Database.initialise(database = DBNAME, host = DBHOST, user = DBUSER, password = DBPASS )  # initialize db or it will be set to none and getconn() will throw attri error, see db method


# # test user
# user = User('nicholashopewell@gmail.com', '705-772-6544', 'Nicholas', 'Hopewell', 'P', None)
#
# user.save_to_db()
# user_from_db = User.load_from_db_by_email('nicholashopewell@gmail.com')
#
# if user:  # if user is not None (if user exists)
#     pass
# else:
#     user = User('nicholashopewell@gmail.com', '705-772-6544', 'Nicholas', 'Hopewell', 'P', None)
#     # change the above to a menu of options
#
# print(user_from_db)
#
#
#
# # test event
# event= Event("Board game night", "Baker's Cafe", "66 Baker Street N. Peterborough, ON.", '2018-08-05', '16:30:00',
#              20.00, 2, 4455)
#
# event.save_to_db()
# event_from_db = Event.load_from_db_by_name("Board game night")
#
# print(event_from_db)
#
#
#
# # test event company
# purchase = Purchases(1, 4455)
#
# purchase.save_to_db()
# purchase_from_db = Purchases.load_from_db_by_id(1)
#
# print(purchase_from_db)
#
#
# # user = events_page_post()
# # user.save_to_db()




def menu():

    # options
    user_input = input("Please enter one of the following:\n"
                       "'e' to enter new client, event, or purchase information,\n"
                       "'r' to retrieve event, client, or purchase information, \n"
                       "'d' to delete client or event information, \n"
                       "'q' to quit and exit")

    while user_input != 'q':
        if user_input == "e":
            user_selection = input("Please enter one of the following:\n"
                                   "'c' to enter a new client, \n"
                                   "'e' to enter a new event \n")
            if user_selection == 'c':
                email = input("Please enter clients email: ")
                phone_number = input("Please enter clients phone number: ")
                first_name = input("Please enter clients first name: ")
                last_name = input("Please enter clients last name: ")
                membership_level = input("Please enter clients membership level: ")

                user = User(email, phone_number, first_name, last_name, membership_level, None)
                user.save_to_db()

                print("Client information below has successfully been added: \n")
                print(user)
                pass

            elif user_selection == 'e':
                event_name = input("Please enter event name: ")
                company_name = input("Please enter event company name: ")
                location = input("Please enter event location: ")
                date = input("Please enter event date: ")
                time = input("Please enter event time: ")
                price = input("Please enter event price: ")
                party_size = input("Please enter party size: ")
                id = input("Please enter event id: ")

                event = Event(event_name, company_name, location, date, time, price, party_size, id)
                event.save_to_db()

                print("Event information below has successfully been added: \n")
                print(event)

        elif user_input == "r":
            user_selection_retrieve = input("Please enter one of the following:\n"
                                   "'c' to retrieve an existing client, \n"
                                   "'e' to retrieve an existing event \n")

            if user_selection_retrieve == 'c':
                email = input("Please enter clients email: ")
                user_from_db = User.load_from_db_by_email(email)
                print("Client Information:\n")
                print(user_from_db)

            elif user_selection_retrieve == 'e':
                event_name = input("Please enter event name: ")
                event_from_db = Event.load_from_db_by_name(event_name)
                print("Event Information:\n")
                print(event_from_db)

        elif user_input == "d":
            user_selection_retrieve = input("Please enter one of the following:\n"
                                            "'c' to remove an existing client, \n"
                                            "'e' to remove an existing event \n")

            if user_selection_retrieve == 'c':
                email = input("Please enter clients email: ")
                User.delete_user_from_db(email)

            elif user_selection_retrieve == 'e':
                event_name = input("Please enter event name: ")
                Event.delete_event_from_db(event_name)



        user_input = input("Please enter one of the following:\n"
                           "'e' to enter new client, event, or purchase information,\n"
                           "'r' to retrieve event, client, or purchase information, \n"
                           "'d' to delete client or event information, \n"
                           "'q' to quit and exit")



menu()






