

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

import subprocess
import json, sys, os, re
from flask import  Flask
from flask import request
from flask import redirect, url_for, jsonify
from pprint import pprint
import traceback

app = Flask(__name__)

def check_data(data):
    if(len(data)!=2):
        return None
    if('id' not in data):
        return None
    if('question' not in data):
        return None
    return data

def anazitisi(idd, question):
    ddd = {
        "questions": [
            {
                "body"      : question,
                "id"        : idd,
                "documents" : []
            }
        ]
    }
    #################
    with open('/home/dpappas/sample.json', 'w') as fp:
        json.dump(ddd, fp)
        fp.close()
    #################
    command = ['sh', '/home/dpappas/runrun.sh',]
    print(' '.join(command))
    res = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
    #################
    return {}

@app.route('/jpdrmm/search', methods=['GET', 'POST'])
def data_searching():
    try:
        app.logger.debug("JSON received...")
        app.logger.debug(request.json)
        if request.json:
            mydata = request.json
            pprint(mydata)
            mydata = check_data(mydata)
            if(mydata is None):
                ret = {'success': 0, 'message': 'False request'}
                app.logger.debug(ret)
                return jsonify(ret)
            else:
                ret = anazitisi(mydata['id'], mydata['question'])
                ret['request'] = mydata
                return jsonify(ret)
        else:
            ret = {'success': 0, 'message': 'request should be json formated'}
            app.logger.debug(ret)
            return jsonify(ret)
    except Exception as e:
        app.logger.debug(str(e))
        traceback.print_exc()
        ret = {'success': 0, 'message': str(e)+'\n'+traceback.format_exc()}
        app.logger.debug(ret)
        return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9250, debug=True, threaded=True)


'''
rm -rf /home/dpappas/sample_bm25_retrieval.txt /home/dpappas/sample.json /home/dpappas/sample_galago_queries.json
'''
