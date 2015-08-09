import braintree
from flask import render_template, flash, redirect, request, Flask, session, url_for
from backend import app, db
from forms import SignupForm, SigninForm
from models import *


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    '9v9w9tvh96vhb5bv',
    'tjgt3k6tyy72pzr4',
    'e67ed6187177d8aa39a35d5e55dd4eb6'
)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate(form.userType) == False:
            return render_template('index.html', form=form, signup_error="bad")
        else:
            newuser = ""
            if form.userType == "grocery":
                newuser = GroceryUser(form.username.data, form.password.data)
            else:
                newuser = FoodbankUser(form.username.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['username'] = newuser.username

            return redirect(url_for('store'))
   
    elif request.method == 'GET':
        return render_template('index.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:   
            newuser = User(form.username.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['username'] = newuser.username

            return redirect(url_for('profile'))
   
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            return redirect(url_for('profile'))
                 
    elif request.method == 'GET':
        return render_template('signin.html', form=form)

@app.route('/profile')
def profile():
 
    if 'username' not in session:
        return redirect(url_for('signin'))
 
    user = User.query.filter_by(username = session['username']).first()
 
    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html')

@app.route('/store.html')
@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/kitchen.html')
@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')


@app.route('/payments')
def payments():
    return render_template('payments.html',
                           clientToken=braintree.ClientToken.generate() )


@app.route('/checkout', methods=["POST"])
def checkout():
    print "hello"
    print "\n amount is " + request.form['amount']
    nonce = request.form["payment_method_nonce"]
    result = braintree.Transaction.sale({
        "amount": request.form["amount"],
        "payment_method_nonce": nonce
    })

    if result.is_success:
        return "<h1>Success! Transaction ID {0}</h1>".format(result.transaction.id)
    else:
        return "<h1>Error: {0}</h1>".format(result.message)
