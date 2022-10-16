import tom_resources as lang


def talk_to_me():
    print("Hello, I am Tom, your digital assistant, how are you today ?")
    goodbye = False
    while not goodbye:
        statement = input("> ")
        print(type(statement), statement)
        if statement == "goodbye":
            goodbye = True

if __name__ == "__main__":
    talk_to_me()

