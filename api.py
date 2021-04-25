import http.client
import mimetypes
import json
from codecs import encode
class API:
    def __init__(self, file="api_key/key.json") -> None:
        with open(file, "r") as f:
            api_data = json.loads(f.read())
        self.api_key = api_data[0]["x-api-key"]
        self.uid = api_data[0]["userId"]
        self.tid = api_data[1]["teamId"]   
    def locate_me(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
        'x-api-key': self.api_key,
        'userid': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/rl/gw.php?type=location&teamId=1265", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return json.loads(data.decode("utf-8"))
    def enter_world(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=type;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode("enter"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=worldId;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode("0"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=teamId;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode(self.tid))
        dataList.append(encode('--'+boundary+'--'))
        dataList.append(encode(''))
        body = b'\r\n'.join(dataList)
        payload = body
        headers = {
        'x-api-key': self.api_key,
        'userid': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/rl/gw.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return json.loads(data.decode("utf-8"))
    def get_runs(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
        'x-api-key': self.api_key,
        'userid': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/rl/score.php?type=runs&teamId=1265&count=10", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    def get_score(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
        'x-api-key': self.api_key,
        'userid': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/rl/score.php?type=score&teamId=1265", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
    def make_move(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=type;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode("move"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=teamId;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode(self.tid))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=move;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode("N"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=worldId;'))
        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))
        dataList.append(encode("0"))
        dataList.append(encode('--'+boundary+'--'))
        dataList.append(encode(''))
        body = b'\r\n'.join(dataList)
        payload = body
        headers = {
        'x-api-key': self.api_key,
        'userid': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/rl/gw.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))