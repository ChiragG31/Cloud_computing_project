from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'



@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    print(number_1 , number_2)
    operation = request.form.get('operation')
    result = 0
    check=0
    if(number_1 == ''):
    	flash(f'Please Enter Number 1')
    	check=1
    elif(number_2 == ''):
    	flash(f'Please Enter Number 2')
    	check=1
    elif operation == 'add':
        result = requests.get("http://add:5051/add/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'minus':
        result =  requests.get("http://subtract:5052/subtract/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'multiply':
        result = requests.get("http://multiply:5053/multiply/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'divide':
    	result = requests.get("http://divide:5054/divide/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'mod':
    	result = requests.get("http://mod:5055/mod/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'lt':
    	result = requests.get("http://lt:5056/lt/"+str(number_1)+"/"+str(number_2)).text
    elif operation == 'gt':
    	result = requests.get("http://gt:5057/gt/"+str(number_1)+"/"+str(number_2)).text
    
            

    if( check==0 ):
    	flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
