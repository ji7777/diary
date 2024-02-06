import snowflake.connector
import random,smtplib
from datetime import date
from email.mime.text import MIMEText
conn=snowflake.connector.connect(user='JISHIL',
                                 password='Podamyre@123',
                                 account='lu78023.ap-southeast-1',
                                 warehouse='COMPUTE_WH',
                                 database='diary',
                                 schema='diary')
class login:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def authenticate(self):
        y='select * from login where username=%s and password=%s'
        try:
            cur=conn.cursor()
            cur.execute(y,(self.username,self.password))
            re=cur.fetchone()
            if re is not None:
                print(re)
                return "ok"
            else:
                print(re)
                return "not ok"
        except Exception as e:
            print("error",e)
        

    def reg(self):
        y='select * from login where username=%s'
        cur.execute(y,(self.username))
        re=cur.fetchone()
        if re is not None:
            print("user already exist")
            return 0
        else:
            w='insert into login values(%s,%s)'
            print('user added')
            cur.execute(w,(self.username,self.password))
            conn.commit()
            return 1
    def __exit__():
        cur.close()
        conn.close()
cur=conn.cursor()
class diaryclass(login):
    def __init__(self, username, password,content):
        super().__init__(username, password)
        self.content=content
    def addpages(self):
        d=date.today().strftime("%d %B %Y")
        cur.execute('insert into diary values(%s,%s,%s)',(self.username,self.content,d))
        conn.commit()
    def return_pages(self):
        
        cur.execute("select datee,pages from diary where username=%s",(self.username))
        r=cur.fetchall()
        return r
def sendotp(to):
    d=random.randint(1000,9999)
    fromm='enikkchuttum@gmail.com'
    subject='OTP for Signup MY DIARY'
    message=f'Your OTP is {d}.'
    a=smtplib.SMTP('smtp.gmail.com',587)
    a.connect("smtp.gmail.com",587)
    a.ehlo()
    a.starttls()
    a.ehlo()
    a.login('enikkchuttum@gmail.com','sbwltvkrxvdmgrju')
    a.sendmail(fromm,to,message)
    a.quit()
    return d
