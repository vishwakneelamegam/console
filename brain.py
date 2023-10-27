import constants
import request

class brain():
    def runLogCorrelator(self, sessionId):
        try:
            if isinstance(sessionId, str):
                response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "correlate_log", "sessionId" : sessionId}
                )
                if response["response"]:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False
    def runTaskValidator(self, sessionId):
        try:
            if isinstance(sessionId, str):
                response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "task_validate", "sessionId" : sessionId}
                )
                if response["response"]:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False