from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
import algosdk

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    content = request.get_json(silent=True)

    pl=content['payload']['platform']
    msg_dict=content['payload']

    msg=json.dumps(msg_dict)
    pk=content['payload']['pk']
    sig=content['sig']


    if pl=="Ethereum":
        eth_msg=eth_account.messages.encode_defunct(text=msg)

        pk2=eth_account.Account.recover_message(eth_msg,signature=sig)

        if pk ==pk2:

            result=True 
        else:
            result=False


    elif pl=="Algorand":

        if algosdk.util.verify_bytes(msg.encode('utf-8'),sig,pk):
            result=True
        else:
            result=False
    #Check if signature is valid
    # result = True #Should only be true if signature validates
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
