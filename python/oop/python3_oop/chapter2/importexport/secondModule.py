import firstModule

print("Second Module's Name: {}".format(__name__))
# First Module's Name: firstModule
# Second Module's Name: __main__
#
# Second Module's Name: __main__
#  if __name__ == '__main__': in firstModule
# Example mean python interpreter sets few special variable like __name__ and then executes code remaining
# if no if __name__ == '__main__':
# both would override just like shown in first example
# else __name__ == '__main__' would only available for executing module rather than imported module
