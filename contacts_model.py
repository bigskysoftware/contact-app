import json
from operator import attrgetter


# ========================================================
# Contact Model
# ========================================================
class Contact:
    # mock contacts database
    db = []

    def __init__(self, id, first, last, phone, email):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def update(self, first, last, phone, email):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.save()

    def save(self):
        if self.id is None:
            if len(Contact.db) == 0:
                max_id = 1
            else:
                max_id = max(Contact.db, key=lambda contact: contact.id).id
            self.id = max_id + 1
            Contact.db.append(self)
        Contact.save_db()

    def delete(self):
        Contact.db.remove(self)
        Contact.save_db()


    @staticmethod
    def all():
        return Contact.db


    @staticmethod
    def search(str):
        result = []
        for c in Contact.db:
            if str in c.first or str in c.last or str in c.email or str in c.phone:
                result.append(c)
        return result


    @staticmethod
    def load_db():
        with open('contacts.json', 'r') as contacts_file:
            contacts = json.loads(contacts_file.read())
            Contact.db.clear()
            for c in contacts:
                Contact.db.append(Contact(c['id'], c['first'], c['last'], c['phone'], c['email']))


    @staticmethod
    def save_db():
        out_arr = []
        for c in Contact.db:
            out_arr.append(c.__dict__)
        print(out_arr)
        json_str = json.dumps(out_arr)
        f = open("contacts.json", "w")
        f.write(json_str)
        f.close()


    @staticmethod
    def find(id):
        id = int(id)
        c = next(filter(lambda c: c.id == id, Contact.db), None)
        return c
