import braintree
from flask import render_template, flash, redirect, request, Flask, session, url_for
from backend import app, db
from forms import *
from models import *
from sqlalchemy.orm import sessionmaker


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    '9v9w9tvh96vhb5bv',
    'tjgt3k6tyy72pzr4',
    'e67ed6187177d8aa39a35d5e55dd4eb6'
)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    GroceryForm = GrocerySignupForm()
    FoodbankForm = FoodbankSignupForm()
    return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm);


@app.route('/GrocerySignup', methods=['GET', 'POST'])
def GrocerySignup():
    FoodbankForm = FoodbankSignupForm()
    GroceryForm = GrocerySignupForm()
   
    if request.method == 'POST':
        if GroceryForm.validate() == False:
            return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm, signup_error="bad")
        else:   
            newuser = GroceryUser(GroceryForm.username.data, GroceryForm.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['username'] = newuser.username
            return redirect(url_for('store'))
   
    elif request.method == 'GET':
        return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm)


@app.route('/FoodbankSignup', methods=['GET', 'POST'])
def FoodbankSignup():
    FoodbankForm = FoodbankSignupForm()
    GroceryForm = GrocerySignupForm()
   
    if request.method == 'POST':
        if FoodbankForm.validate() == False:
            return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm, signup_error="bad")
        else:   
            newuser = FoodbankUser(FoodbankForm.username.data, FoodbankForm.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['username'] = newuser.username

            return redirect(url_for('kitchen'))
   
    elif request.method == 'GET':
        return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm)


@app.route('/GroceryLogin', methods=['GET', 'POST'])
def GroceryLogin():
    FoodbankForm = FoodbankSigninForm()
    GroceryForm = GrocerySigninForm()
   
    if request.method == 'POST':
        if GroceryForm.validate() == False:
            return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm, signup_error="bad")
        else:   
            session['username'] = GroceryForm.username.data

            return redirect(url_for('store'))
   
    elif request.method == 'GET':
        return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm)



@app.route('/FoodbankLogin', methods=['GET', 'POST'])
def FoodbankLogin():
    FoodbankForm = FoodbankSigninForm()
    GroceryForm = GrocerySigninForm()
   
    if request.method == 'POST':
        if FoodbankForm.validate() == False:
            return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm, signup_error="bad")
        else:   
            session['username'] = FoodbankForm.username.data

            return redirect(url_for('kitchen'))
   
    elif request.method == 'GET':
        return render_template('index.html', GroceryForm=GroceryForm, FoodbankForm=FoodbankForm)


@app.route('/addProduct', methods=['POST'])
def addProduct():
    if request.method == 'POST':
        product = models.Product( item_number=request.form["item_number"],
                                  expiration=request.form["expiration"],
                                  quantity=request.form["quantity"],
                                  name=request.form["name"],
                                  price=0,
                                  sale=False,
                                  grocery=FoodbankUser.query.filter_by(username = session['username']).first())
        db.session.add(product)
        db.session.commit()
    return redirect(url_for('store'))

@app.route('/listProduct', methods=['POST'])
def listProduct():
    if request.method == 'POST':
        print request.form["tableoption"] + "bla bla"
        Session = sessionmaker()
        product = Product.query.filter_by(id=request.form["tableoption"])
        if request.form['submit'] == "sell":
            product.price=request.form['sellingPrice']
            print product.price
        else:
            product.price=0
        product.sale=True
        #product.commit()
        #db.session.query(Product).filter_by(id=request.form["tableoption"]).update({'price': product.price, 'sale': True})
        #product.update({'price': product.price, 'sale': True})
        db.session.commit()
    return redirect(url_for('store'))


@app.route('/logout')
@app.route('/signout')
def signout():
 
  if 'username' not in session:
    return redirect(url_for('index'))
     
  session.pop('username', None)
  return redirect(url_for('index'))


@app.route('/store.html')
@app.route('/store')
def store():
    user = GroceryUser.query.filter_by(username = session['username']).first()

    if user is None:
        return redirect(url_for('index'))
    else:
        goods = user.products.filter(Product.sale == False)
        return render_template('store.html',goods=goods)


@app.route('/kitchen.html')
@app.route('/kitchen')
def kitchen():
    user = FoodbankUser.query.filter_by(username = session['username']).first()
 
    if user is None:
        return redirect(url_for('index'))
    else:
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
