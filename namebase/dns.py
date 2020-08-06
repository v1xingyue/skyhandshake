# coding=utf-8

import namebase.utils as nu
from namebase.config import access_key, secret_key
import logging


def getNsServer(name):
    r = nu.Request(nu.authHeaders(access_key, secret_key))
    resp = r.get("/dns/domains/"+name + "/nameserver")
    return resp


def markTXT(name, prefix, value, ttl=1800):
    logging.info("mark txt record : %s ", prefix)
    r = nu.Request(nu.authHeaders(access_key, secret_key))
    params = {
        "records": [
             {
                 "type": "TXT",
                 "host": prefix,
                 "value": value,
                 "ttl": ttl,
             }
        ],
        "deleteRecords": []
    }
    path = "/dns/domains/" + name+"/nameserver"
    resp = r.put(path, params)
    return resp
