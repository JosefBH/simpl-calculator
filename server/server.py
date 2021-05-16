from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/addition', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        print(request.form)
        return render_template('error.html', err="! Something went wrong !") 
    else:
        try:
            number1 = request.form['number1']
            number2 = request.form['number2']
            result = float(number1) + float(number2)
            print(result)
            return render_template('result.html', result=result)

        except expression as identifier:
            print(identifier)
            return render_template('error.html', err="! Invalid Input !")

@app.route('/result/substraction', methods=['GET', 'POST'])
def substraction():
    if request.method == 'GET':
        print(request.form)
        return render_template('error.html', err="! Something went wrong !") 
    else:
        try:
            number1 = request.form['number1']
            number2 = request.form['number2']
            result = float(number1) - float(number2)
            print(result)
            return render_template('result.html', result=result)

        except expression as identifier:
            print(identifier)
            return render_template('error.html', err="! Invalid Input !")

@app.route('/result/multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'GET':
        print(request.form)
        return render_template('error.html', err="! Something went wrong !") 
    else:
        try:
            number1 = request.form['number1']
            number2 = request.form['number2']
            result = float(number1) * float(number2)
            print(result)
            return render_template('result.html', result=result)

        except expression as identifier:
            print(identifier)
            return render_template('error.html', err="! Invalid Input !")

@app.route('/result/division', methods=['GET', 'POST'])
def division():
    if request.method == 'GET':
        print(request.form)
        return render_template('error.html', err="! Something went wrong !") 
    else:
        try:
            number1 = request.form['number1']
            number2 = request.form['number2']
            result = float(number1) / float(number2)
            print(result)
            return render_template('result.html', result=result)

        except expression as identifier:
            print(identifier)
            return render_template('error.html', err="! Invalid Input !")


if __name__ == "__main__":
    app.run(debug=True, host="simpl-calculator.herokuapp.com")    
