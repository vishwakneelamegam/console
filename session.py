import constants
import request

class session():
    def getNewSessionKey(self):
        try:
            response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "create_session"}
                )
            if response["response"]:
                return response["sessionId"]
            else:
                return None
        except Exception as e:
            return None
        
