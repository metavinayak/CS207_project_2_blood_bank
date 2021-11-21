from flask import Blueprint, render_template, flash,redirect,url_for,request
from flask_login import login_required, current_user
from __init__ import create_app, db
import sqlite3

main = Blueprint('main', __name__)

@main.route('/home',methods = ["GET","POST"]) # home page that return 'home'
def home():
    if current_user.is_authenticated:
        msg=None
        if request.method == 'POST':            
            try:
                hname = request.form["HospitalName"]  
                grp = request.form["bloodGroup"]  
                date = request.form["DateTime"]  
                with sqlite3.connect("hospital_data.sqlite") as con:  
                    cur = con.cursor()
                    # name, available, date
                    if('All' in grp):
                        msg=cur.execute(f'SELECT * FROM hospital WHERE name LIKE "%{hname}%"').fetchall()
                    else:
                        msg=cur.execute(f'SELECT * FROM hospital WHERE ((name LIKE "%{hname}%") AND ((available LIKE "%{grp}%") OR (available LIKE "%All%")))').fetchall()

                    if not len(msg)>=1: msg=("Empty query result",) 
            except:    
                msg = ("Error occured in try",)    
        return render_template('index.html', name=current_user.name,loggedin=True,msg=msg)
    else:
        return render_template('index.html', name='',loggedin=False)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(host="0.0.0.0") 