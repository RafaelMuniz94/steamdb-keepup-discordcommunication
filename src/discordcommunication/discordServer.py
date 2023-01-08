from flask import Flask, request,jsonify
import json
import requests

app = Flask(__name__)

url = ""

@app.route('/',methods=['GET'])
def getOK():
    return "p",200

@app.route('/send',methods=['POST'])
def EnviaPayloadDiscord():
    try:
        content = request.json
        
        js = {
            "appid":content["appid"],
            "Quantidade": content["count"],
            "Data": content["date"]
        }
    
        payload = {
                "content" : json.dumps(js),
                "username" : "GamesInfo"
                }
        payload["embeds"] = [
    {
        "description" : content["newsitems"][0]["news_date"],
        "url": content["newsitems"][0]["url"],
        "title" : content["newsitems"][0]["title"]
    }
]

        response = requests.post(url=url,json =payload)
        return jsonify(response)
    except Exception as error:
        print(error)
        return error
    ##client = requests.post()

# if __name__ == '__main__':
app.run(host="0.0.0.0",port=5001, debug=True)