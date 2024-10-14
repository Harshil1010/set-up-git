class banking:
    def __init__(self,name,age,ac_no,available_bal):
        self.name=name
        self.age=age
        self.ac_no=ac_no
        self.available_bal=available_bal

    def credit(self,money):
        if self.available_bal>=money :
            self.available_bal -= money

            print("Current Available Ballance in your account is : ",self.available_bal)
        
        else:
            print("insufficient ballance")

    def debit(self,money):
        self.available_bal+=money

        print("Current Available Ballance in your account is : ",self.available_bal)

obj1=banking("Harshil",23,123456789, 3000)
obj1.credit(4000)
obj1.debit(5000)
obj1.credit(4000)