from flask import Flask,request
import os 
app= Flask(__name__)

@app.route("/tri")
def t():
    if request.method=='GET':
        os.system('cls')
        return "tr"

app.run(debug=True)