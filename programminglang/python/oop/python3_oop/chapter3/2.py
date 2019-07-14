class Contact:
    all_contacts = []  # class variables

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {} order to {}".format(order, self.name))

# >>> c = Contact("Some Body", "somebody@example.net")
# >>> s = Supplier("Sup Plier", "supplier@example.net")
# >>> print(c.name, c.email, s.name, s.email)
# Some Body somebody@example.net Sup Plier supplier@example.net
# >>> c.all_contacts
# [<__main__.Contact object at 0x7f27cfc61198>, <__main__.Supplier object at 0x7f27cfc611d0>]
# >>> c.order("Ineed pliers")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Contact' object has no attribute 'order'
# >>> s.order("I need pliers")
# If this were a real system we would send I need pliers order to Sup Plier
