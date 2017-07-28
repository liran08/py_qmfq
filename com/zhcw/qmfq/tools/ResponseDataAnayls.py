
import json

def getBodyDatafromResponseData(resp):
    js = resp.json()
    data = json.loads(json.dumps(js["message"]))
    body = json.loads(json.dumps(data["body"]))
    return body

def cmpResponse(invRes,actlRes):
    if invRes.toString() == actlRes.toString():
        return True
    else:
        return False

