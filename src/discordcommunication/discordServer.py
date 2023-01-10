from flask import Flask, request,jsonify
from Services.PayloadMappingService import PayloadMappingService
#import requests
import httpx
from Utils.configuration import Configuration
import json


app = Flask(__name__)
config = Configuration()


@app.route('/send',methods=['POST'])
async def EnviaPayloadDiscord():
    try:
        content = request.json

        payload = PayloadMappingService(config).Map(content)
        
        for news in payload:
            news = json.dumps(news,ensure_ascii=False)
            print(news)
            print(type(news))
            print('+++++++++++')
            response = await httpx.AsyncClient().post(url=config.webhook_url, json = news)
            print(response.json())
        
        return "ok"
    except Exception as error:
        print(error)
        return error
    ##client = requests.post()



app.run(host=config.host,port=config.port, debug=config.debug)