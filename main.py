import mysql.connector
lucky=mysql.connector.connect(host="localhost",user="root",password="lucky0205",database="adhar")
print(lucky.is_connected())
def openAcc():

    n=input("enter the name: ")
    ac=input("enter the account No:")
    db=input("enter the date of birth: ")
    add=input("enter the adrres: ")
    cn=(input("enter the conctact Number:"))
    ob=int(input("enter the opening balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    mysql1=("insert into account values (%s,%S,%s,%s,%s,%s)")
    mysql2=("insert into amount values(%s,%s,%s)")
    x=mydb.cursor()
    x.execute(mysql1.data1)
    x.execute(mysql2.data2)
    print("data enter successfully..")
    main()
def deposit_amount():
    account=("enter the account you want deposite:")
    ac = input("enter the account No:")
    a="select balance from amount where accNO"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    mysql=("update amount set the balance where accNO=%s")
    d=(t,ac)
    x.execute(mysql,d)
    mydb.commit()
    main()

def WITHDRAW_AMOUNT():
    account = ("enter the account you want withdraw amount:")
    ac = input("enter the account No:")
    a = "select balance from amount where accNO"
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    mysql = ("update amount set the balance where accNO=%s")
    d = (t, ac)
    x.execute(mysql, d)
    mydb.commit()
    main()
def Balance_ENQURIY():
    ac = input("enter the account No:")
    a="select * from amount where accNO=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print(f"balance for account: {ac} is {result[-1]}")
    main()
def DISPLAY_COSTUMER_DETAILS():
    ac = input("enter the account No:")
    a = "select * from amount where accNO=%s"
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()


def CLOSE_ACCOUNT():
    ac = input("enter the account No:")
    mysql = "DELETE FROM amount WHERE accNO = %s"  # Assuming you want to delete from the 'amount' table
    data = (ac,)
    x = mydb.cursor()
    x.execute(mysql, data)
    mydb.commit()
    main()
def main():
    print('''
            1.OPEN BANK ACCOUNT
            2.DEPOSITE AMOUNT
            3.WITHDRAW AMOUNT
            4.Balance ENQURIY
            5.DISPLAY COSTUMER DETAILS
            6.CLOSE AN ACCOUNT ''' )
    choose=int(input("chose the above option from above="))
    if choose==1:
        pass
    elif choose==2:
        pass
    elif choose==3:
        pass
    elif choose==4:
        pass
    elif choose==5:
        pass
    elif choose==6:
        pass




