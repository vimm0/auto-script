# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
def run():
    print("First Module's Name: {}".format(__name__))


if __name__ == '__main__':
    run()
    print("Run directly")
else:
    print("Run from import")
