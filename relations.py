#Simple conditional statements
def family(relation):
    if relation=="father":
        print("Luke's father is Darth Vader")
    elif relation=="sister":
        print("Luke's sister is Leia")
    elif relation=="brother in law":
        print("Luke's brother in law is Han")
    elif relation=="droid":
        print("Luke's droid is R2D2")
    else:
        print("incorrect relation")

print("Enter the relation you want to know about:")
user_input= input()
family(user_input)