import cherrypy
from cherrypy.lib.static import serve_file
import sys
import socket
import json


def sub(mat1,mat2,port1,name):
    data={"matricules": [mat1,mat2],"port": port1,"name": name}
    host = '127.0.0.1'
    port = 3001
    s = socket.socket()
    s.connect((host,port))
    msg = json.dumps(data).encode('utf8')
    total = 0
    while total < len(msg):
        sent = s.send(msg[total:])
        total += sent

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8001
    
    sub("18253","18322",port,"Sartor")