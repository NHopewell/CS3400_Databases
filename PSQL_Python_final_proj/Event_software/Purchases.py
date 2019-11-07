from Database import CursorFromConnectionFromPool


class Purchases:
    # properties of Purchases() objects
    def __init__(self, client_id, event_id, id = None):
        self.id = id
        self.client_id = client_id
        self.event_id = event_id

    # display when printing
    def __repr__(self):
        return (f"<Purchase ID: {self.id}\nClient ID: {self.client_id}\nEvent ID: {self.event_id}>")


    # save Purchase to purchases table in db
    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO purchases(client_id, event_id)'
                           'VALUES (%s, %s)',
                           (self.client_id, self.event_id))


    # load purchase from  purchase table based on purchase id
    @classmethod
    def load_from_db_by_id(cls, id):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM purchases WHERE id = %s', (id,))  # expects a tupple
            company_data = cursor.fetchone()
            return cls(id=company_data[0], client_id=company_data[1], event_id=company_data[2])