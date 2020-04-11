from flask import Flask, request, jsonify, Response
import threading
import hashlib
import hmac
import sys
import os

import conf

app = Flask(__name__)

def verify_hmac_hash(data, signature):
    mac = hmac.new(conf.SECRET, msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest('sha1=' + mac.hexdigest(), signature)

@app.route("/update", methods=["POST"])
def start_update():
    signature = request.headers.get('X-Hub-Signature')
    data = request.data
    if not verify_hmac_hash(data, signature):
        return Response(status=403)
    update_thread = threading.Thread(target=conf.update)
    update_thread.daemon = True
    update_thread.start()
    return jsonify(success=True)