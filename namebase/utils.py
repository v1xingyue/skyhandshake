# coding=utf-8

import base64
import requests
import json
DEFAULT_API_VERSION = "/v0"


def encode_credentials(access_key: str, secret_key: str) -> str:
    return (base64.b64encode('{}:{}'.format(access_key, secret_key).encode("utf-8"))).decode("utf-8")


def authHeaders(access_key, secret_key):
    return {
        "Authorization": "Basic {}".format(encode_credentials(access_key, secret_key)),
        "Accept": 'application/json',
        "Content-Type": 'application/json'
    }


class Request(object):

    url = "https://www.namebase.io/api" + DEFAULT_API_VERSION

    def __init__(self,  headers, timeout=30, api_base_url=""):
        if api_base_url != "":
            self.url = api_base_url
        self.timeout = timeout
        self.headers = headers

    def get(self, path, params=None):
        """Perform GET request"""
        r = requests.get(url=self.url + path, params=params, timeout=self.timeout,
                         headers=self.headers)
        r.raise_for_status()
        return r.json()

    def post(self, path, data=None, json_data=None, params=None):
        """Perform POST request"""
        r = requests.post(url=self.url + path, data=data, json=json_data, params=params, timeout=self.timeout,
                          headers=self.headers)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return json.loads(e.response.content)
        return r.json()

    def delete(self, path, json_data=None, params=None):
        """Perform DELETE request"""
        r = requests.delete(url=self.url + path, params=params, json=json_data, timeout=self.timeout,
                            headers=self.headers)
        r.raise_for_status()
        return r.json()

    def put(self, path, params):
        r = requests.put(url=self.url + path, json=params,
                         timeout=3, headers=self.headers)
        r.raise_for_status()
        return r.json()

    # def status(self):
    #     r = requests.get(url=self.url + "/info", headers=self.headers)
    #     r.raise_for_status()
    #     return r.json()

    # def setTxt(self, name, prefix, txt):
    #     params = {
    #         "records": [
    #             {
    #                 "type": "TXT",
    #                 "host": prefix,
    #                 "value": txt,
    #                 "ttl": 3600,
    #             }
    #         ],
    #         "deleteRecords": []
    #     }

    #     print(json.dumps(params))

    #     u = self.url + "/dns/domains/" + name+"/nameserver"
    #     print(u)
    #     r = requests.put(url=u, headers=self.headers, json=params, timeout=3)

    #     return r
