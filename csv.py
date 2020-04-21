import csv


def openfile():
    ifile = str(input("Enter filename: (No extensions)"))
    ifile = ifile+'.csv'
    f = open(ifile, "a")
    for x in f:
        print(x)


class lineobject:
    def __init__(self, pname, pprice, pqty, pdate):
        self.objname = pname
        self.objprice = pprice
        self.objqty = pqty
        self.objdate = pdate

    def linecheck(self):
        print(self.objname+self.objprice+self.objqty+self.objdate)


def inputname():
    pname = "text"
    pname = input("Enter the product name: ")
    return pname


def inputprice():
    pprice = "text"
    while True:
        pprice = input("Enter the product price: ")
        try:
            pval = float(pprice)
            break
        except ValueError:
            print("Invalid Input.")
    return pprice


def inputqty():
    pqty = "text"
    while True:
        pqty = input("Enter the product quantity: ")
        try:
            pval = int(pqty)
            break
        except ValueError:
            print("Invalid Input.")
    return pqty


def inputdate():
    pdcount = 1
    condition = False
    while pdcount == 1:
        if condition == False:
            pinput = input("What month did you purchase the item(s) (MM): ")
            try:
                pval = int(pinput)
                pmonth = pval
                if pmonth >= 1 and pmonth <= 12:
                    pdcount = pdcount + 1
                    condition = True
                    break;
                else:
                    print("Please enter a valid month")
                    condition = False
            except ValueError:
                print("Invalid Input.")
        break;
    while pdcount == 2:
        if condition == True:
            pinput = input("What day did you purchase the item(s) (DD): ")
            try:
                pval = 

d = inputdate()