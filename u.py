# coding=utf-8

import tornado.web
import siaskynet as skynet
import hashlib
from namebase.dns import status, markTXT, getNsServer
import mimetypes

rootName = "vml"


# f 为相对路径
def updateSkyHandshake(f):
    skylink = skynet.Skynet.upload_file(f)
    print(skylink)
    pathHash = hashlib.md5(f.encode()).hexdigest()
    print(pathHash)
    markTXT(rootName, pathHash, skylink)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        f = self.request.path[1:]
        pathHash = hashlib.md5(f.encode()).hexdigest()
        print("pathHash", pathHash)
        records = getNsServer(rootName).get("records")
        for r in records:
            print(r.get("host"))
            if r.get("host") == pathHash:
                # return self.write("hello find " + pathHash)
                resp = skynet.Skynet.download_file_request(r.get("value"))
                mimeTypes = mimetypes.guess_type(f, strict=True)
                if mimeTypes[0] != None:
                    self.set_header("Content-type", mimeTypes[0])
                return self.write(resp.content)

        self.write("Hello, world " + pathHash)


def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])


def skyServer():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    updateSkyHandshake("19622.jpg")
    updateSkyHandshake("index.html")
    updateSkyHandshake("a.css")
    updateSkyHandshake("a.js")
    print("start skyserver")
    skyServer()
