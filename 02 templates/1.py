from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Variables
    name = "John Doe"
    age = 17
    
    # Conditionals
    is_adult = age > 17 # True / False
    
    # Rendering the template
    return render_template('index.html', name=name, age=age, is_adult=is_adult)


@app.route('/fruits')
def fruits():
    # List of items
    fruits = ['Apple', 'Banana', 'Orange', 'Mango']
    
    # Rendering the template
    return render_template('fruits.html', fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)
