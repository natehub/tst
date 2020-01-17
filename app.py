import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_file, jsonify, session
import datetime
import requests
from io import BytesIO
import json
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
'''
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username='CALCULATING_CARL',
        password='12345',
        hostname='all.thedata.com',
        port='1521',
        database='everything',
    )
)

data = pd.read_sql("SELECT * FROM …", engine)


import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

oracle_connection_string = (
    'oracle+cx_oracle://{username}:{password}@' +
    cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
)

engine = create_engine(
    oracle_connection_string.format(
        username='CALCULATING_CARL',
        password='12345',
        hostname='all.thedata.com',
        port='1521',
        service_name='every.piece.ofdata',
    )
)

data = pd.read_sql("SELECT * FROM …", engine)
'''

@app.route('/home')
def serve_homepage():
    return render_template('homepage.html')

@app.route('/tiles/<string:z>/<string:x>/<string:y>.png', methods=['GET'])
def get_tiles(z,x,y):
    URL = "http://b.tile.stamen.com/toner/"+z+"/"+x+"/"+y+".png"
    r = requests.get(url = URL, stream=False) 
    return send_file(BytesIO(r.content), attachment_filename='map_tile.png', mimetype='image/png')

'''
@app.route('/pic_one/<string:ids>', methods=['GET'])
def get_one_row(ids):
 
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM  projects where id = {id}".format(id=ids))
    all_data = cursor.fetchall()
    columnname = []
    for row in cursor.description:
        columnname.append(row[0])
    print(all_data)
    datasend = jsonify(columnname=all_data)
    return datasend
'''

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form.get('password') == 'password' and request.form.get('email') == 'admin':
        session['logged_in'] = True
        return render_template('uploadpage.html')
    
    else:
        return render_template('login.html', login=0)

@app.route('/loginpage')
def login():
    if not session.get('logged_in'):
	    
        return render_template('login.html', login=1)
    elif session.get('logged_in') == False:
        return render_template('login.html', login=1)
    else:
        return render_template('uploadpage.html')

@app.errorhandler(404)
def not_found(e):
    result = '404'
    return result


#if __name__ == '__main__':
    
    #app.secret_key = os.urandom(12)
    #app.run(host='localhost', ssl_context=("cert.pem", "key.pem"), debug = True)

    #app.run(host="0.0.0.0", port=8080, debug=False, threaded=True)
    