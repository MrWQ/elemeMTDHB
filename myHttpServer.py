from http.server import HTTPServer, BaseHTTPRequestHandler
import json,MySQL

data = {'result': 'hello'}
host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    def do_POST(self):
        # att = Resquest.__getattribute__('1')
        # att = self.rfile('1')
        # print(att)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write('000'.encode())
        # 获取db对象
        db = MySQL.creatDBObject()
        cookieObj = MySQL.selectCookieObjectById(db, 1)
        self.wfile.write(cookieObj.cookie.encode())
        # self.wfile.write(att.encode())


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()