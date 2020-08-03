# coding=utf-8

import namebase.utils as nu
import json
from namebase.config import access_key, secret_key


def status(name):
    r = nu.Request(nu.authHeaders(access_key, secret_key))
    resp = r.get("/dns/domains/"+name)
    print(resp)


def getNsServer(name):
    r = nu.Request(nu.authHeaders(access_key, secret_key))
    resp = r.get("/dns/domains/"+name + "/nameserver")
    return resp


def markTXT(name, prefix, value):
    r = nu.Request(nu.authHeaders(access_key, secret_key))
    resp = r.setTxt(name, prefix, value)
    print(resp.content, resp.status_code)
