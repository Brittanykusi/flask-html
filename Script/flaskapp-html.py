from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world, WWW!'

@app.route('/')
def homepage():
    return render_template('p1_homepage.html')

@app.route('/login1')
def login1():
    return render_template('p2_login1.html')
    # import to note that it is going to look for the .html files in a folder called templates

@app.route('/patient_landing')
def patient_landing():
    return render_template('p3_patient_landing_page.html')
    # import to note that it is going to look for the .html files in a folder called templates
    
@app.route('/login2')
def login2():
    return render_template('p4_login2.html')

@app.route('/schedule_appointment')
def schedule_appointment():
    return render_template('p5_schedule_appointment.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

