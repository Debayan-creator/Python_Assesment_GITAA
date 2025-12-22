class Statistics:
    def __init__(self, lst):
        self.lst = lst
        
    def count(self):
        return len(self.lst)
        
    def Sum(self):
        sum = 0
        for i in range(0,len(self.lst)):
            sum = sum+self.lst[i]
        return sum
        
    def Maxi(self):
        return max(self.lst)
    
    def describe(self):
        return {
            "Count":variable.count(),
            "Sum":variable.Sum(),
            "Max":variable.Maxi()
        }

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

variable = Statistics(ages)
print("Describe", variable.describe())

class PersonAccount():
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first = first_name
        self.last = last_name
        self.incomes = incomes
        self.expenses = expenses
    
    def totalincome(self):
        return self.incomes
    def expense(self):
        return self.expenses
    def acc_info(self):
        return self.first, self.last, self.incomes
    def add_income(self, amount):
        if amount>0:
            self.incomes=self.incomes+amount
        

emp1=PersonAccount("Deb","Roy", 456867, 78553)

print("Total Income",emp1.totalincome())
print("Total Expense",emp1.expense())   

print("Account info")
fname, lname, income = emp1.acc_info()
print("Acc holder name {} {} having income {}".format(fname, lname, income))

emp1.add_income(3000)

print("New balance", emp1.totalincome())

 
