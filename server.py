import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# WebPage Mapping

# Root Page Rendering
@app.route('/')
def root():
    return render_template('index.html')

# Dinamic Page Randering
@app.route('/<string:page_name>')
def html_page(page_name: str):
    return render_template(page_name)

# How to react to the data a client sends to the Server.

'''
Flask use a global request object.

These objects are proxies to objects that are local toa  SPECIFIC context.

When Flask starts its internal request handling it figures out that the current thread is the active
context and binds the current application and the WSGI environments to that context (thread).

 It does that in an intelligent way so that one application can invoke 
 another application without breaking.

 Flask use the Request Object to interact with the GET POST PUT sent between 
 the client and the server.




'''

# Endpoint to perform an action
# In HTML contact there is a button that is waiting for an action usign POST.
# This endpoint is that action
# <form action="submit_form" method="post" class="reveal-content">
# The information sent goes into the Payload.

@app.route('/submit_form', methods = ['GET', 'POST'])
def submit_form():
    
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data.values())
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong'
    
# Writing to a CSV Database.
# We can store the data sent by the client
# This function is called in the submit_form.

def write_to_csv(data: dict):
    with open('./db/database.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data.values())
        
