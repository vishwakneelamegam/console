import constants
import request
import os
import time

class guide():
    def get(self, sessionId):
        try:
            if isinstance(sessionId, str):
                response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "snap_shot", "sessionId" : sessionId}
                )
                return "\n\n".join(["{no}. {text}".format(no=(no + 1),text=data["guidance"]) for no, data in enumerate(response["response"])])
            else:
                return "No guidance received"
        except Exception as e:
            return "Exception occurred"

os.system('clear')
sessionId = input("Provide your session id : ")
try:      
    while True:
        guideObj = guide()
        guidance = guideObj.get(sessionId)
        print(guidance)
        time.sleep(10)
        os.system('clear')
except KeyboardInterrupt:
    print("Terminated")
    