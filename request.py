import http.client
import json

def makeHeader():
    try:
        header = {}
        header["Content-Type"] = "application/json" 
        return header
    except Exception as e:
        return {}

def httpRequestPost(api, route, header, data):
    try:
        connect = http.client.HTTPSConnection(api)
        connect.request('POST',route,json.dumps(data),header)
        response = connect.getresponse()
        jsonResponse = json.loads(response.read().decode())
        return jsonResponse
    except Exception as e:
        return {}