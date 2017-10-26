
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, cook, MenuItem
from addTable import Customer
from addRequestTable import requestInfoRecord

app = Flask(__name__)

engine = create_engine('sqlite:///CookMenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add API endpoint to get list of cook
@app.route('/foodService/cook/JSON')
def cookJSON():
    cookList = session.query(cook).all()
    return jsonify(all_cook=[i.serialize for i in cookList])

# Add API endpoint to get list of menu items
@app.route('/foodService/cook/<int:cook_id>/menu/JSON')
def menuJSON(cook_id):
    menuItems = session.query(MenuItem).filter_by(cook_id = cook.id).all()
    return jsonify(menuItems=[i.serialize for i in menuItems])

@app.route('/')
@app.route('/foodService', methods=['GET', 'POST'])
def requestInfo():
    if request.method == 'POST':
        newRequest = requestInfoRecord(location = request.form['location'],
                               time = request.form['time'])
        session.add(newRequest)
        session.commit()
        return redirect(url_for('findCook'))
    else:
        return render_template('foodService.html')


@app.route('/foodService/cook')
def findCook():
    # it should list all cook
    # allow choose a cook and lead to menu
    cookList = session.query(cook)
    count = cookList.count()
    return render_template('cook.html', cook = cookList, Count = count)


@app.route('/foodService/cook/<int:cook_id>/menu')
def showMenu(cook_id):
    # show menu for chosen cook
    Cook = session.query(cook).filter_by(id = cook_id).one()
    items = session.query(MenuItem).filter_by(cook_id = cook_id).all()
    return render_template('menu.html', Items = items, cook = Cook)



@app.route('/foodService/cook/<int:cook_id>/menu/<int:menu_id>/order', methods=['GET', 'POST'])
def orderPayment(cook_id, menu_id):
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    Cook = session.query(cook).filter_by(id = cook_id).one()

    if request.method == 'POST':
        # add customer info to database
        newCustomer = Customer(name=request.form['name'], location = request.form['location'],
                               time = request.form['time'], card = request.form['card'] )
        session.add(newCustomer)
        session.commit()
        flash("Your order is placed!")
        # direct to payment page
        return redirect(url_for('confirmPayment', customer_id=newCustomer.id, cook_id = cook_id, menu_id = menu_id))
    else:
        return render_template('orderPayment.html', item = item, cook = Cook)


@app.route('/foodService/cook/<int:cook_id>/menu/<int:menu_id>/order/<int:customer_id>/confirm')
def confirmPayment(customer_id, cook_id, menu_id):
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    Cook = session.query(cook).filter_by(id = cook_id).one()
    customer = session.query(Customer).filter_by(id = customer_id).one()
    return render_template('confirmPayment.html', Customer = customer, item = item, cook = Cook)




if __name__ == '__main__':
    app.secret_key = 'super_secure_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
