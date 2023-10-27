import constants
import request
import os

class logs():
    def add(self, sessionId, log):
        try:
            if isinstance(log, str) and isinstance(sessionId, str):
                response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "add_log", "sessionId" : sessionId, "log" : log}
                )
                if response["response"]:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

os.system('clear')        
logObj = logs()
sessionId = input("Provide your session id : ")
eventLoop = True
try:
    while eventLoop:
        userLog = input("Log : ")
        userLog = userLog.strip()
        if len(userLog) > 0:
            if userLog == "exit":
                eventLoop = False
                break
            response = logObj.add(sessionId, userLog)
            if response:
                pass
            else:
                eventLoop = False
    print("Terminated")
except KeyboardInterrupt:
    print("Terminated")