class Voter:
    def __init__(self,name,age,iitID):
        self.name=name
        self.age=age
        self.iitID=iitID

    def validation(self):
        return (self.age >= 18) and (self.name !="") and (self.iitID !="")