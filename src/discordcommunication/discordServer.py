from flask import Flask, request,jsonify,Response
from Services.PayloadMappingService import PayloadMappingService
import httpx
from Utils.configuration import Configuration


app = Flask(__name__)
config = Configuration()


@app.route('/send',methods=['POST'])
async def EnviaPayloadDiscord():
    try:
        content = request.json

        payload = PayloadMappingService(config).Map(content)

        responses = []
        
        for news in payload:
            response = await httpx.AsyncClient().post(url=config.webhook_url, json = news)
            if response.text != "":
                responses.append(response.text)

        if len(responses) > 0:
            jsonResponses =  jsonify(responses)
            return Response(jsonResponses,status=200,mimetype='application/json')
        else:
            return Response(status=200,mimetype='application/json')
    except Exception as error:
        print(error)
        return Response("Ocorreu um erro!",status=500,mimetype='application/json')
    ##client = requests.post()



app.run(host=config.host,port=config.port, debug=config.debug)