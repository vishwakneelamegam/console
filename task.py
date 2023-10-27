import constants
import request
import session
import brain
import json
import os
import time

class tasks():
    def add(self, sessionId, tasks):
        try:
            if isinstance(tasks, list) and isinstance(sessionId, str):
                response = request.httpRequestPost(
                constants.brainApi, 
                constants.route, 
                request.makeHeader(), 
                {"event" : "add_task", "sessionId" : sessionId, "tasks" : tasks}
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
sessionObj = session.session()
sessionId = sessionObj.getNewSessionKey()
print("Session ID : {id}".format(id=sessionId))
taskFile = input("Provide the task file name : ")
if not os.path.exists(taskFile):
    print("Task file {name} not available".format(name=taskFile))
    exit()
with open(taskFile, 'r') as file:
    data = json.load(file)
taskObj = tasks()
taskList = data
response = taskObj.add(sessionId, [text["text"] for text in taskList["steps"]])
if response:
    print("Task Added")
    try:
        while True:
            brainObj = brain.brain()
            brain2Status = brainObj.runLogCorrelator(sessionId)
            brain3Status = brainObj.runTaskValidator(sessionId)
            os.system('clear')
            print("Session ID : {id}".format(id=sessionId))
            print("Brain Two Has Done Job : {status}".format(status=brain2Status))
            print("Brain Three Has Done Job : {status}".format(status=brain2Status))
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("Terminated")
else:
    print("Task Not Added")