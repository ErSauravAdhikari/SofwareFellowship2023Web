from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Profile updated. Name: {name}'
    return render_template('profile_form.html')

if __name__ == '__main__':
    app.run(debug=True)

