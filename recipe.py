import json
import http.client

azureOpenAiapiKey = "728f738051f74ba887d358e3672bff96"

temperature = 0

tokens = 10000

jsonContentType = "application/json"

api = "sailors-ai.openai.azure.com"

route = "/openai/deployments/gpt3516k/chat/completions?api-version=2023-05-15"

def makeParameter(messages):
     try:
        return {"messages" : messages,"temperature" : temperature,"max_tokens" : tokens}
     except Exception as e:
         return {}

def makeHeader(contentType, key):
    try:
        header = {}
        header["api-key"] = key
        header["Content-Type"] = contentType 
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
    
def getDataFromJson(data):
    try:
        if "choices" in data:
            if isinstance(data["choices"], list):
                if len(data["choices"]) > 0:
                    if isinstance(data["choices"][0], dict) and "message" in data["choices"][0]:
                        return data["choices"][0]["message"]
                else:
                    return None
            else:
                return None
        else:
            return None
    except Exception as e:
        return None

def recipe(name):
    try:
        header = makeHeader(jsonContentType, azureOpenAiapiKey)
        parameter = makeParameter([{"role" : "system", "content" : """
                                    Your role is to provide recipe for a food asked by the user json format({"steps" : [{"no" : 1, "text" : "Here comes the step 1"}, {"no" : n, "text" : "here comes the step N"}]}).
                                    Note : There must be only 10 steps for a recipe.
                                    """
                                    },
                                   {"role" : "user", "content" : """
                                    Write recipe for {name} 
                                    Output : """.format(name=name)
                                    }
                                   ])
        response = httpRequestPost(api, route, header, parameter)
        data = getDataFromJson(response)
        return json.loads(data["content"])
    except Exception as e:
        return {}

name = input("Provide the recipe name :")    
response = recipe(name)
recipeName = '{name}.json'.format(name=name)
with open(recipeName, 'a') as file:
    json.dump(response, file, indent=4)
print("Recipe has been saved as {name}.json".format(name=name))