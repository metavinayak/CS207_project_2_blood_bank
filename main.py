from flask import Blueprint, render_template, flash,redirect,url_for
from flask_login import login_required, current_user
from __init__ import create_app, db

main = Blueprint('main', __name__)

@main.route('/home') # home page that return 'home'
def home():
    if current_user.is_authenticated:
        return render_template('home.html', name=current_user.name,loggedin=True)
    else:
        return render_template('home.html', name='',loggedin=False)


app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode