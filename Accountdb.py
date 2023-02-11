import mysql.connector as sql
class Account:
    def __init__(self):
        self.conn=sql.connect(user="root",password="Vedant@4352",database="bank",auth_plugin='mysql_native_password')
        print("Connected...")
    def __del__(self):
        self.conn.close()
        print("Connectioon Closed...")
    def openAccount(self,name,OB,ACNO,dob,pnum,addr):
        stmt="insert into account(name,OB,ACNO,DOB,PHONE,ADDRESS) value(%s,%s,%s,%s,%s,%s)"
        self.cur=self.conn.cursor()
        self.cur.execute(stmt,[name,OB,ACNO,dob,pnum,addr])
        self.conn.commit()
        stmt2="select * from account order by ACNO DESC "
        cur2=self.conn.cursor()
        cur2.execute(stmt2)
        res=cur2.fetchone()
        if self.cur.rowcount==1:
            return res[0]
        else:
            print("Failed...")
    def deposit(self,acc,amt):
        stmt="UPDATE account SET OB=OB+%s WHERE ACNO=%s"
        cur=self.conn.cursor()
        cur.execute(stmt,[amt,acc])
        self.conn.commit()
        if cur.rowcount==1:
            return True
        else:
            return False
    def withdraw(self,acc,amt):
        stmt="select * from account where ACNO=%s"
        cur=self.conn.cursor()
        cur.execute(stmt,[acc])
        res=cur.fetchone()
        bal=int(res[5])
        if bal>=amt:
            stmt1 = "UPDATE account SET OB=OB-%s WHERE ACNO=%s"
            cur1=self.conn.cursor()
            cur1.execute(stmt1,[amt,acc])
            self.conn.commit()
            if cur1.rowcount==1:
                return True
        else:
            return False
    def search(self,acc):
        stmt="select * from account where ACNO=%s"
        cur=self.conn.cursor()
        cur.execute(stmt,[acc])
        res=cur.fetchone()
        return res

    def listAccount(self):
        stmt="select * from account"
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchall()
        return res
