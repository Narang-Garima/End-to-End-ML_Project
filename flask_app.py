# Flask App Routing

from flask import Flask, render_template, request, url_for,redirect

app = Flask(__name__) #entry point of the application

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route('/about', methods=['GET'])
def about():
    return "<h1>About Us</h1><p>This is the about page.</p>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return f"<h1>Success! Your score is {score}.</h1>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"<h1>Fail! Your score is {score}.</h1>"

@app.route('/form', methods=['GET' ,'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('form.html')
    else:
    
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        total = num1 + num2
        #return render_template('result.html', results=total)
        # Redirect based on condition
        if total > 50:
            return redirect(url_for('success', score=int(total)))
        else:
            return redirect(url_for('fail', score=int(total)))


if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode that way we can see errors in the browser




