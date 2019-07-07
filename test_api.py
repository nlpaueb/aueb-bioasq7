

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
    res = subprocess.Popen(
        [
            'python3.6',
            '/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/queries2galago.py',
            '/home/dpappas/sample.json',
            '/home/dpappas/sample_galago_queries.json',
            '/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/stopwords.pkl',
        ],
        stdout=subprocess.PIPE,
        shell=False
    )
    #################
    res = subprocess.Popen(
        [
            'echo',
            'nlp.aueb.group!',
            '|'
            'sudo',
            '-S',
            '/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/galago-3.10-bin/bin/galago',
            'batch-search',
            '--index=/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/galago-3.10-bin/bin/pubmed_only_abstract_galago_index',
            '--verbose=False',
            '--requested=100',
            '--scorer=bm25',
            '--defaultTextPart=postings.krovetz',
            '--mode=threaded',
            '/home/dpappas/sample_galago_queries.json',
            '>',
            '/home/dpappas/sample_bm25_retrieval.txt',
        ],
        stdout=subprocess.PIPE,
        shell=False
    )
    #################
    #################
    #################
    '''
    '''





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

