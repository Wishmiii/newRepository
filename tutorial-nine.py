import votermanager
def main():
    name=input("What is your name? ")
    age=input("What is your age? ")
    iitNumber=input("What is your IIT number?")
    votermanager.addVoter(name,age,iitNumber)

    y = votermanager.addVoter(0)

    print('Your Name',y.name)
    print("Your Age",y.age)
    print("Yout IIT no",iitNumber)