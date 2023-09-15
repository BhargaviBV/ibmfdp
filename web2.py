# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:52:17 2023

@author: H-GST-CSE-B503-08
"""

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template,request,session
#import ibm_db
#print(ibm_db.active(conn))

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host='0.0.0.0',debog=True)
