import votermanager
def main():
    name=input("Name: ")
    age=input("Age: ")
    iitID=input("IIT NO: ")

    y = votermanager.addVoter(name,age,iitID)

    print("Your Name: ", name)
    print("Your Age: ", age)
    print("Your IIT no: ", iitID)

main()