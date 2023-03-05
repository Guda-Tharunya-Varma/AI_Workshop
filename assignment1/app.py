from flask import Flask, request, jsonify
from storageutils import MySQLManager


CONFIG = {
    "database": {
        "gnits": {
            "user": "aiworkshop",
            "password": "Gnits@123",
            "host": "185.217.126.61",
            "database": "studentworks"
        }
    }
}

app = Flask(__name__)


def show_album(album_name):
    query = 'select * from music where album_name = "{}";'.format(album_name)
    res=[]
    try:
        res = MySQLManager.execute_query(query,None,**CONFIG['database']['gnits'])
    except Exception as error:
        print(error)
    return res

@app.route('/api/showalbum_details', methods=['GET', 'POST'])
def run1():
    if request.method == 'GET':
        return jsonify("this api is for showing album_details")
    else:
        input_json = request.json
        req = input_json['album_name']
        output = show_album(req)
        return jsonify(output)
 
 
def show_songs(duration):
    query = 'select * from music where duration = "{}";'.format(duration)
    res=[]
    try:
        res = MySQLManager.execute_query(query,None,**CONFIG['database']['gnits'])
    except Exception as error:
        print(error)
    return res   


@app.route('/api/showsongs_of_duration', methods=['GET', 'POST'])
def run2():
    if request.method == 'GET':
        return jsonify("this api is for showing songs based on the duration time")
    else:
        input_json = request.json
        req = input_json['duration']
        output = show_songs(req)
        return jsonify(output)
    
    
def show_count(playlist):
    query = 'select count(*) as "no_of_songs" from music where playlist = "{}";'.format(playlist)
    res=[]
    try:
        res = MySQLManager.execute_query(query,None,**CONFIG['database']['gnits'])
    except Exception as error:
        print(error)
    return res   


@app.route('/api/showno_of_songs', methods=['GET', 'POST'])
def run3():
    if request.method == 'GET':
        return jsonify("this api is for showing  number of songs in playlist")
    else:
        input_json = request.json
        req = input_json['playlist']
        output = show_count(req)
        return jsonify(output)
    
        
if __name__ == '__main__':
    app.run("0.0.0.0", port=5555)