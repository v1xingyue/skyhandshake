# coding=utf-8


import tornado.web
import mimetypes
import logging
from namebase.dns import markTXT, getNsServer
from skynettool.file import downloadFileResp

port = 8080
skyCache = 60
namebaseCache = 60


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        f = self.request.path[1:]
        if f == "":
            f = "index.html"
        mimeTypes = mimetypes.guess_type(f, strict=True)
        if mimeTypes[0] != None:
            self.set_header("Content-type", mimeTypes[0])

        skyResp = downloadFileResp(f, skyCache, namebaseCache)
        if skyResp != None:
            return self.write(skyResp.content)

        self.write(self.request.path+" 404 ")

    # curl -X PUT -T a.js http://localhost:8080/info
    def put(self):
        f = self.request.path[1:]
        if f == "":
            f = "index.html"
        logging.info("put url : %s ", f)
        bodyBytes = self.request.body
        print(bodyBytes)
        self.write("ok")


def skyServer(skyCache=60, namebaseCache=60):
    app = tornado.web.Application([
        (r"/.*", MainHandler),
    ])
    logging.info("start server : %d ", port)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
