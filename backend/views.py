import braintree
from flask import render_template, flash, redirect, request, Flask
from backend import app

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    '9v9w9tvh96vhb5bv',
    'tjgt3k6tyy72pzr4',
    'e67ed6187177d8aa39a35d5e55dd4eb6'
)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


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
