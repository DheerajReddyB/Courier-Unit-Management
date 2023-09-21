from prettytable import PrettyTable
import datetime
import mysql.connector as mys
conn=mys.connect(host='localhost',user='root',passwd='15061917',database='couriermanagement')
cur=conn.cursor()

e = datetime.datetime.now()
Name=[]
Name1=[]
Phno1=[]
Phno=[]
MailId=[]
Pass=[]
Role=[]
Address=[]
Type=[]
Weight=[]
SerialNumber=[]
Company=[]
Bill=[]
dict={'Name':Name,'Phone Number':Phno,'Mail Id':MailId,'Password':Pass}
update=''
update1=''
a=1
while a!=0:
    print("Welcome to Courier Management System")
    print("************************************")
    print("*          1.Login                 *")
    print("*      2.Create An Account         *")
    print("*           0.Exit                 *")
    print("************************************")
    a = int(input("Enter your Option:- "))

    if(a==1):
        MAIL=input("Mail Id:- ")
        PASS=input("Password:- ")
        Index=MailId.index(MAIL)
        if(MAIL!=MailId[Index] or PASS!=Pass[Index]):
            print()
            print("***************************")
            print("-------Wrong Details-------")
            print("--------Try Again----------")
            print("***************************")
            print()
            print()

        for i in range(0,len(MailId)):
            ex=1
            while ex!=0:
                if (MAIL == MailId[i] and PASS == Pass[i]):
                    log = MAIL[MAIL.index(".") + 1:]

                    if (log == 'customer@gmail.com'):
                        print()
                        print("Thanks For Signing Up ")
                        print("             and Welcome To Our Page")
                        print("************************************")
                        print("     1.Courier Your Package         ")
                        print("       2.Check the Package          ")
                        print("************************************")
                        b = int(input("Enter your option:- "))
                        ex=0
                        if (b == 1):
                            print("Enter your Package Details")
                            NAME = input("Enter your Name:- ")
                            PHNO = input("Enter your Phone Number:- ")
                            ADDRESS = input("Enter the address to be delivered:- ")
                            TYPE = input("Enter Package Type:- ")
                            WEIGHT = float(input("Enter Package Weight(in Kg):- "))
                            SRNO = input("Enter Package Serial Number:- ")
                            company=''
                            x = slice(2)
                            typeofthepackage = SRNO[x]
                            if (typeofthepackage == 'AM'):
                                company = 'Amazon'
                            elif (typeofthepackage == 'FK'):
                                company = 'FlipKart'
                            elif (typeofthepackage == 'MS'):
                                company = 'Meesho'
                            elif (typeofthepackage == 'LK'):
                                company = 'Lenskart'
                            elif (typeofthepackage == 'DC'):
                                company = 'Decathlon'
                            else:
                                print("ERROR!")
                            print("**************************************")
                            Name1.append(NAME)
                            Phno1.append(PHNO)
                            Address.append(ADDRESS)
                            Type.append(TYPE)
                            Weight.append(WEIGHT)
                            Company.append(company)
                            SerialNumber.append(SRNO)
                            bill = WEIGHT * 200
                            Bill.append(bill)
                            print("Your expected to reach the package on %s/%s/%s" % (
                            e.day + 1, e.month, e.year) + " by %s:%s" % (e.hour, e.minute))
                            print("Bill Amount:- ", bill)
                            print()
                            print()
                            data = (
                            len(Name1), NAME, PHNO, ADDRESS, TYPE, WEIGHT, SRNO, company,
                            bill)
                            query = """insert into FINAL values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                            cur.execute(query, data)
                            conn.commit()

                        elif (b == 2):
                            print("********Update On Your Package********")
                            print("Dear ", NAME)
                            print("==============================================================================")
                            if (update == 'Y'):
                                print("Your Package has been packed")
                                print("              is ready to be Shipped")
                            elif (update == 'N'):
                                print("Your Package has not yet packed")
                                print("              still in the process of Packing")
                            else:
                                print("Services has been Offline")
                                print("             Will be Resumed Soon")
                            print("===============================================================================")
                            if (update1 == 'Y'):
                                print("Your Package has been already Delivered")
                                print("              Thank You                ")
                                print("In Case if the Package is not yet Recived. Please do contact the Office")
                            elif (update1 == 'N'):
                                print("Your Package has not yet Delivered")
                                print("              still on its way to Reach You")
                            else:
                                print("Services has been Offline")
                                print("             Will be on its way Soon")
                            print("================================================================================")
                            print()
                            print()
                            break

                    elif (log == 'admin@gmail.com'):
                        print("Welcome to the Dashboard")
                        print("       Do Check the Package to be Packed")
                        print("*************************************************************")
                        print("     1.Check The Package and Approve for verification        ")
                        print("              2.Check the Log In Details                     ")
                        print("                     0.EXIT                                  ")
                        print("*************************************************************")
                        z = int(input("Enter your option:- "))
                        if (z==1):
                            print("*****************************************************************************************************************************")
                            myTable = PrettyTable(
                            ["IndexNo", "Name", "PhoneNumber", "Address", "PackageType", "Weight", "SerialNumber",
                              "Company", "BillAmount"])
                            for i in range(0, len(Weight)):
                                myTable.add_row(
                                    [i + 1, Name1[i] ,Phno1[i] , Address[i], Type[i], Weight[i], SerialNumber[i], Company[i],
                                    Bill[i]])
                            print(myTable)
                            print("*****************************************************************************************************************************")
                            print()
                            print()
                            print("================================================")
                            update = input("Update about The package to be Packed(Y/N):- ")
                            print("================================================")
                            while (update != 'Y'):
                                update = input("Update about The package to be Packed(Y/N):- ")
                                print("================================================")
                            print()
                            print()
                        elif (z==2):
                            query2 = """select * from mail"""
                            cur.execute(query2)
                            rec=cur.fetchall()
                            print("|=============================================================================|")
                            for r in rec:
                                print(r)
                            print("|=============================================================================|")
                        elif (z==0):
                            break

                    elif (log == 'delivery@gmail.com'):
                        print("Welcome to the Dashboard")
                        print("       Do Check the Package to be delivered")
                        print("*******************************************")
                        myTable = PrettyTable(
                            ["IndexNo", "Name", "PhoneNumber", "Address", "PackageType", "Weight", "SerialNumber",
                             "Comapny", "BillAmount"])
                        for i in range(0, len(Weight)):
                            myTable.add_row(
                                [i + 1, Name1[i], Phno1[i], Address[i], Type[i], Weight[i], SerialNumber[i], Company[i],
                                 Bill[i]])
                        print(myTable)
                        print()
                        print()
                        print("================================================")
                        update1 = input("Update about The package to be delivered(Y/N):- ")
                        print("================================================")
                        while (update1 != 'Y'):
                            update1 = input("Update about The package to be delivered(Y/N):- ")
                            print("================================================")
                        print()
                        print()
                        ex=0
                    else:
                        print()
                        ex=0
                else:
                    print()
                    ex=0





    elif(a==2):
        print("-----------CREATE AN ACCOUNT------------")
        name=input("Enter Your Name:- ")
        phno=int(input("Enter Your Phone Number:- "))
        mailId=input("Enter A Mail Id to create(.customer/.admin/.delivery):- ")
        log = mailId[mailId.index(".") + 1:]
        if (log=='admin@gmail.com'):
            log1="ADMIN"
        elif (log=='delivery@gmail.com'):
            log1='DELIVERY PERSON'
        elif (log=='customer@gmail.com'):
            log1='CUSTOMER'

        if(log=='admin@gmail.com' or log=='delivery@gmail.com'):
            secretcode=input("Enter the Authorized code to Create Account as Admin or Delivery Person:- ")
        else:
            secretcode='15061917'
        Passw=input("Enter a New Password:- ")
        conpass=input("Enter a Password to Confirm:- ")
        if(Passw==conpass and secretcode=='15061917'):
            print()
            print("****************************")
            print("Account Created Successfully")
            print("****************************")
            print()
            print()
            Name.append(name)
            Phno.append(phno)
            MailId.append(mailId)
            Pass.append(Passw)
            Role.append(log1)
            data1 = (len(Name),mailId, Passw, log1, name, phno)
            query1 = """insert into MAIL values(%s,%s, %s, %s, %s, %s)"""
            cur.execute(query1, data1)
            conn.commit()

        else:
            print()
            if(secretcode!='15061917'):
                print("***********************")
                print("Wrong Authorized Code!!")
                print("***********************")
                print()

            if Passw!=conpass:
                print("******************************")
                print("Wrong Confirm Password Entered")
                print("Try Again!!")
                print("******************************")
                print()
                print()

if(update=='Y' and update1=='Y'):
    Name.clear()
    Phno.clear()
    Address.clear()
    Type.clear()
    Weight.clear()
    SerialNumber.clear()
    Company.clear()
    Bill.clear()

#create table FINAL(SrNo int,Name varchar(20),PhoneNumber varchar(10),Address varchar(69),Type varchar(10),Weight int,SerialNumber varchar(10),Company varchar(10),Bill int);
# create table MAIL(SrNo int,MailID varchar(69),Password varchar(20),Role varchar(20),Name varchar(20),PhoneNo varchar(20));