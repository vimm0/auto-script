# class User:
#     _persist_methods = ['get', 'save', 'delete']
#
#     def __init__(self, persister):
#         self._persister = persister
#
#     def __getattr__(self, attribute):
#         if attribute in self._persist_methods:
#             return getattr(self._persister, attribute)
#
#
# user = User(persister={'gh': 123})
# print(user.get('gh'))


# class ContentFilter(object):
#     def __init__(self, filters=None):
#         self._filters = list()
#         if filters is not None:
#             self._filters += filters
#
#     def filter(self, content):
#         for filter in self._filters:
#             content = filter(content)
#         return content
#
#
# content = " lfalksdjfaks l kfasdkflasd  laskdfjl offensive_filter"
# filter = ContentFilter([
#     'offensive_filter',
#     'ads_filter',
#     'porno_video_filter'])
# filtered_content = filter.filter(content)


# import os
#
#
# class RenameFileCommand(object):
#     def __init__(self, from_name, to_name):
#         self._from = from_name
#         self._to = to_name
#
#     def execute(self):
#         os.rename(self._from, self._to)
#         print(f'from {self._from} to {self._to}')
#
#     def undo(self):
#         os.rename(self._to, self._from)
#         print(f'from {self._from} to {self._to}')
#
#
# class History(object):
#     def __init__(self):
#         self._commands = list()
#
#     def execute(self, command):
#         self._commands.append(command)
#         print(self._commands)
#         command.execute()
#
#     def undo(self):
#         self._commands.pop().undo()
#         # print(self._commands)
#
#
# history = History()
# history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
# history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
# history.undo()
# history.undo()

#
# class Logger(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_logger'):
#             cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
#         return cls._logger
#
# logger = Logger()

# class Command:
#
#     def __init__(self, authenticate=None, authorize=None):
#         self.authenticate = authenticate or self._not_authenticated
#         self.authorize = authorize or self._not_authorized
#
#     def execute(self, user, action):
#         self.authenticate(user)
#         self.authorize(user, action)
#         return action()
#
# if in_sudo_mode:
#     command = Command(always_authenticated, always_authorized)
# else:
#     command = Command(config.authenticate, config.authorize)
# command.execute(current_user, delete_user_action)
# command = Command()
#
# if in_sudo_mode:
#     command.authenticate = always_authenticated
#     command.authorize = always_authorized
# else:
#     command.authenticate = config.authenticate
#     command.authorize = config.authorize
# command.execute(current_user, delete_user_action)

# class Car(object):
#
#     def __init__(self):
#         self._tyres = [Tyre('front_left'),
#                              Tyre('front_right'),
#                              Tyre('rear_left'),
#                              Tyre('rear_right'), ]
#         self._tank = Tank(70)
#
#     def tyres_pressure(self):
#         return [tyre.pressure for tyre in self._tyres]
#
#     def fuel_level(self):
#         return self._tank.level

# import socket
#
# class SocketWriter(object):
#
#     def __init__(self, ip, port):
#         self._socket = socket.socket(socket.AF_INET,
#                                      socket.SOCK_DGRAM)
#         self._ip = ip
#         self._port = port
#
#     def write(self, message):
#         self._socket.send(message, (self._ip, self._port))
#
# def log(message, destination):
#     destination.write('[{}] - {}'.format(datetime.now(), message))
#
# upd_logger = SocketWriter('1.2.3.4', '9999')
# log('Something happened', udp_destination)
