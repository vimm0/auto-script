class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


# >>> c1 = Contact("John A", "johna@example.net")
# >>> c2 = Contact("John B", "johnb@example.net")
# >>> c3 = Contact("Jenna C", "jennac@example.net")
# >>> [c.name for c in Contact.all_contacts.search('John')]
# ['John A', 'John B']
# >>>
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
    # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass

# >>> e = EmailableContact("John Smith", "jsmith@example.net")
# >>> Contact.all_contacts
# [<__main__.EmailableContact object at 0xb7205fac>]
# >>> e.send_mail("Hello, test e-mail here")
# Sending mail to jsmith@example.net
