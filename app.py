from flask import Flask, render_template, request, redirect, url_for 
from CoffeMachine import CoffeMachine
from CoffeCorner import CoffeeCorner


app = Flask(__name__)
cm=CoffeMachine("coffee machine 1", "Plane 1")
cm.CreateCoffeMenu()
cc = CoffeeCorner("Corner 1","room 1")

@app.route("/") 
def Welcome():
    return "<p> Welcome to virtual coffee machine. </p>"


@app.route("/CoffeeMachine")
def CoffeeMachine(): 
    return render_template('CoffeeMachine.html', pageMenu = cm.GetCoffeeMenu())

@app.route("/CoffeeCorner")
def CoffeeCorner():
    pc = cc.GetChatList()
    po = cc.GetOrderList()
    return render_template('CoffeeCorner.html', pageMenu = cm.GetCoffeeMenu(), pageCon = pc, pageOrd = po)    

@app.route("/CoffeeCornerBS")
def CoffeeCornerBS():
    return render_template('CoffeeCornerBS.html')

@app.route("/AddComment", methods=['POST'])
def AddComment():
    print(request.form['fname'], request.form['comment'])
    cc.AddToChatList(request.form['fname'], request.form['comment'])
    return redirect(url_for('CoffeeCorner'))

@app.route("/AddCoffee", methods=['POST'])
def AddCoffee():
    cname = request.form['Cname']
    print(cname)
    cm.AddToCoffeeMenu(cname)
    return redirect(url_for('CoffeeCorner'))

@app.route("/EmptyMenu", methods=['POST'])
def EmptyMenu():
    cm.EmptyCoffeeMenu()
    return redirect(url_for('CoffeeCorner'))


@app.route("/AddOrder", methods=['POST'])
def AddOrder():
    name = request.form['fname']
    coffee= request.form['coffee']
    print (name, coffee)
    cc.AddOrder(name,coffee)
    return redirect(url_for('CoffeeCorner'))

if __name__ == '__main__':
    app.run()

