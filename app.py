# Building URL dynamically
# Variable Rule
# Jinja 2 Template Engine

'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''


from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class,
which will be our WSGI (Web Server Gateway Interface) application.
'''
#WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h2>Home Page</h2>'
# redirecting to a HTML page
@app.route("/index")
def index():
    return render_template('index.html')

# GET and POST request
@app.route("/form", methods = ['GET','POST'])
def form(): 
    if request.method =='POST':
        name = request.form['textbox'] # 'textbox' :id of the textbox in HTML template
        # name = 'hello'
        return f'Marks :{name}'
    return render_template('form.html')

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res='Passed'
    else:
        res = 'Failed'
    data = {'result': res, 'score': score}
    return render_template('result.html', results=data) #for condition

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        marks = float(request.form['textbox'])
    else:
        return render_template('form.html') 
    return redirect(url_for('success',score=marks))

if __name__=='__main__':
    app.run(debug= True)