class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


# The diamond problem

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone


# use of super
# with Different sets of arguments
#  We have to design our base class parameter lists so that they accept keyword arguments
# for any argument that is not required by every subclass implementation.

# We've changed all arguments to keyword arguments by giving them an empty string
# as a default value. We've also ensured that a **kwargs parameter is included to
# capture any additional parameters that our particular method doesn't know what to
# do with. It passes these parameters up to the next class with the super call.
#
# If you aren't familiar with the **kwargs syntax, it basically collects any
# keyword arguments passed into the method that were not explicitly
# listed in the parameter list.

# class Contact:
#     all_contacts = []
#
#     def __init__(self, name='', email='', **kwargs):
#         super().__init__(**kwargs)
#         self.name = name
#         self.email = email
#         self.all_contacts.append(self)
#
#
# class AddressHolder:
#     def __init__(self, street='', city='', state='', code='', **kwargs):
#         super().__init__(**kwargs)
#         self.street = street
#         self.city = city
#         self.state = state
#         self.code = code
#
#
# class Friend(Contact, AddressHolder):
#     def __init__(self, phone='', **kwargs):
#         super().__init__(**kwargs)
#         self.phone = phone
