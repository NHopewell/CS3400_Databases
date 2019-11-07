from Database import CursorFromConnectionFromPool


class Event:
    # properties of Event() objects
    def __init__(self, event_name, company_name, location, date, time, price, party_size, id):
        self.event_name = event_name
        self.company_name = company_name
        self.location = location
        self.date = date
        self.time = time
        self.price = price
        self.party_size = party_size
        self.id = id

    # display when printing
    def __repr__(self):
        return (f"<Event: {self.event_name}\nHosted by: {self.company_name}\nLocation: {self.location}"
                f"\nDate: {self.date} \nTime: {self.time}")


    # saves event information to the event table in the database
    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO event(event_name, company_name, event_location, event_date, event_time, '
                           'price, party_size, eid)'
                           'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                           (self.event_name, self.company_name, self.location, self.date, self.time,
                            self.price, self.party_size, self.id))


    # loads event information from event table of database via event name
    @classmethod
    def load_from_db_by_name(cls, name):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM event WHERE event_name = %s',
                           (name,))  #  expects a tupple
            event_data = cursor.fetchone()
            if event_data:
                return cls(event_name=event_data[1], company_name=event_data[2],  location = event_data[3],
                           date = event_data[4], time= event_data[5], price= event_data[6],
                           party_size=event_data[7], id= event_data[0])
            else:
                print("Event does not currently exist in the database.")

        # remove a user from the clients table in the database via their email address

    # delete event from events table of database via event name
    @classmethod
    def delete_event_from_db(clas, event_name):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('DELETE FROM event WHERE event_name = %s', (event_name,))
            print(f"Event '{event_name}' has successfully been removed.")
