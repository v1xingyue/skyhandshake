# coding=utf-8

import logging
import siaskynet as skynet
import hashlib
from namebase.dns import markTXT, getNsServer
from collections import namedtuple
import time

rootName = "vml"
cacheItem = namedtuple("cacheItem", ["expire", "data"])
nbCacheMap = {}
skyCacheMap = {}


# f 为相对路径
def uploadSkyHandshake(f):
    logging.info("update %s to skynet ", f)
    skylink = skynet.Skynet.upload_file(f)
    logging.info("skylink : %s", skylink)
    pathHash = hashlib.md5(f.encode()).hexdigest()
    logging.info("path hash : %s ", pathHash)
    markTXT(rootName, pathHash, skylink)


def downloadFileResp(f, skyCache=30, namebaseCache=30):
    logging.info("download file : %s ", f)
    pathHash = hashlib.md5(f.encode()).hexdigest()
    logging.info("pathHash %s ", pathHash)

    nsCache = nbCacheMap.get("namebase.record", None)
    records = []
    if nsCache != None and nsCache.expire >= time.time():
        logging.info("use namebase cache")
        records = nsCache.data
    else:
        records = getNsServer(rootName).get("records")
        nbCacheMap["namebase.record"] = cacheItem(
            time.time() + namebaseCache,
            records
        )

    for r in records:
        if r.get("host") == pathHash:
            link = r.get("value")
            respCache = skyCacheMap.get(link, None)
            if respCache != None and respCache.expire >= int(time.time()):
                logging.info("use skynet cache")
                return respCache.data
            else:
                resp = skynet.Skynet.download_file_request(r.get("value"))
                skyCacheMap[link] = cacheItem(time.time() + skyCache, resp)
            return resp
    return None
