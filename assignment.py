
def register():
    name=input("enter your name: ")
    age=int(input("enter your age:"))
    year=int(input("enter your birth year: "))
    print(f"hello {name} !")
    print(f"you are {age} years old.")
    print(f"you was born in {year}")

register()


def calculate():
    num1=input("enter 1st: ")
    num2=input("enter 2nd: ")
    print('sum is : 'num1+num2)
    print('difference is : 'num1-num2)
    print('mutlipying : 'num1*num2)
    print('dividing : 'num1/num2)
calculate()


users = [('Nathan','2313'),('Geez','pass231'),('Abebe','092313133'),('Miki','pl3s34D0ntH4ckM3')]
new_users=dict(users)
print(new_users)


i = 0
while i < 5:
    usr_name = input('Enter username: ')
    passwd = input('Enter password: ')
 #every letter should match including capital and small letter
    if usr_name in new_users and new_users[usr_name] == passwd:
        print("Welcome to GTST Company!!!")
        break
    else:
        print("Incorrect login!!!")
    i += 1
else:
    print("Sorry u are limited!")


