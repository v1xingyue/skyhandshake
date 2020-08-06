# coding=utf-8

import logging
from skynettool.file import uploadSkyHandshake
from server import skyServer

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S'
    )
    uploadSkyHandshake("index.html")
    uploadSkyHandshake("a.js")
    uploadSkyHandshake("a.css")
    uploadSkyHandshake("img.jpg")
    logging.info("start skyserver")
    skyServer()
