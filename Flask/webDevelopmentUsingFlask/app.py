from flask import Flask,render_template,request,redirect,session # type: ignore
from db import Database
from api import API
from functools import wraps
app=Flask(__name__)
app.secret_key = "abc123"
dbo=Database()
api=API()
@app.route('/')
def index():
    """ templates naam se hi folder hona chahiye aur jo bhi html page hai vo templates folder ke ander apna aap search kr lega toh koi path dene ki jarurat ni h"""
    return render_template('login.html') 

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('useremail')
    password=request.form.get('userpassword')
    if dbo.check_data(email,password)==1:
        session['user']=email
        return redirect('/dashboard')
    elif dbo.check_data(email,password)==0:
        return render_template('login.html',error='Password is incorrect login again')
    else:
        return render_template('login.html',error='email not exixts kindly register')
    
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/ner')
@login_required
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
@login_required
def perform_ner():
    text=request.form.get('text')
    entity=request.form.get('entity')
    try:
        result=api.perform_ner(text,entity)
        return render_template('ner.html',response=result)
    except:
        return render_template('ner.html',error='too many load on server kindly try again')
    
@app.route('/perform_sentiment',methods=['post'])
@login_required
def perform_sentiment():
    text=request.form.get('text')
    try:
        result=api.perform_sentiment(text)
        return render_template('sentiment.html',response=result)
    except:
        return render_template('sentiment.html',error='too many load on server kindly try again')


@app.route('/sentiment')
@login_required
def sentiment():
    return render_template('sentiment.html')

@app.route('/emotion')
@login_required
def emotion():
    return render_template('emotion.html')

@app.route('/perform_emotion',methods=['post'])
@login_required
def perform_emotion():
    text=request.form.get('text')
    try:
        result=api.perform_emotion(text)
        return render_template('emotion.html',response=result)
    except:
        return render_template('emotion.html',error='too many load on server kindly try again')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('username')
    email=request.form.get('useremail')
    password=request.form.get('userpassword')
    if dbo.add_data(name,email,password) :
        return render_template('login.html',message='Rgistration successfull kindly proceed')
    else:
        return render_template('registration.html',message='user already exist')
    


app.run(debug=True) #debug is true means agar koi bhi change krenge toh direct reflect hoga
