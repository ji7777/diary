from flask import Flask,render_template,request,redirect,session
import datetime,random,time
from login import login,sendotp,diaryclass
date1=datetime.date.today().strftime("%d %B %Y")
app=Flask(__name__,template_folder='template',static_folder='static')
app.secret_key = 'your_secret_key_here'
@app.route('/')
def home():
    
    return render_template('homepage.html',titl='myapp')
@app.route('/signup')
def signup():
    return render_template('signup.html',titl='sign up')


@app.route('/diary')
def diary():
    return render_template('diarywriting.html',date=date1)
@app.route('/login',methods=['GET','POST'])
def check():
    usr=request.form.get('usr')
    pw=request.form.get('pwd')
    
    print(usr,pw)
    d=login(usr,pw)
    h=d.authenticate()
    if h=="ok":
        session["user"]=usr
        session["pwd"]=pw
        print(session["user"],session["pwd"])
        return redirect('/diary')
    else:
        return redirect('/signup')
@app.route('/otp')
def otp():
    s=session["user"]
    print(s)
    d=sendotp(session["user"])
    return render_template('otp.html',rand=d,user=s)
@app.route('/otp',methods=['post'])
def otpv():
    userop=request.form['otp']
    d=request.form['otph']
    print(userop)
    if d==userop:
        print('success')
        return redirect('/')
    else:
        return '<alert>something went wrong</alert>'
@app.route('/signup',methods=['GET','POST'])
def valid():
    usr=request.form.get('usr')
    pw=request.form.get('pwd')
    print(usr,pw)
    f=login(usr,pw)
    g=f.reg()
    if g==0:
        return redirect('/')
    else:
        session["user"]=usr
        session["pwd"]=pw
        return redirect('/otp')
@app.route('/diary',methods=['POST'])
def addpages():
    c=request.form.get('diary')
    session["c"]=c
    x=diaryclass(session["user"],session["pwd"],c)
    x.addpages()
    return redirect('diary')
@app.route('/view')
def see():
    c='hsdsjjf'
    y=diaryclass(session["user"],session["pwd"],c)
    a=y.return_pages()
    print(a)
    return render_template('allpages.html',a=a)
@app.route('/logout')
def logout():
    if "user" in session:
        session.pop("user",None)
        session.pop("pwd",None)
        return render_template('logout.html')
    else:
        return redirect('home')
@app.route('/profile')
def new():
    a=session["user"]
    return render_template('profile.html',a=a)
if __name__=="__main__":
    app.secret_key='jishilrajm'
    app.run(debug=True,)