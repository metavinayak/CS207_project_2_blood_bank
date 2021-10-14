from flask import Flask,render_template

app=Flask(__name__)

HOST='localhost'
PORT='5000'
app.config['SECRET_KEY']='26def34403daf181a933ef3f8fa0bfd4f5e4415a604d7eda055cae72ebc670dd'

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT,debug=True)
    #app.run(host='localhost')