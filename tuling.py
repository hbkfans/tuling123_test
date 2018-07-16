#coding=UTF-8

import requests


class MyTulingRobot(object):

    def __init__(self):
        # one free tuling123 robot
        self.api_key = "9de908868304414d8bea19fa3a47e6e5"
        self.proxy = {}

    def set_proxy(self, proxy_type, proxy):
        if proxy_type not in ["http", "https"]:
            raise "error proxy_type %s.." % proxy_type
        self.proxy[proxy_type] = proxy

    def post_data(self, url, data):
        response = requests.post(url=url, data=data,
                                 proxies=self.proxy)
        return response.content.decode("utf-8")

    def request_qa_list(self):
        api_url = r"http://www.tuling123.com/v1/kb/select"
        qa_list_data = {
            "apikey": self.api_key,
            "data": {
                "pages": {
                    "pageNumber": 1,
                    "pageSize": 10,
                    "searchBy": "question"
                }
            },
        }
        return self.post_data(api_url, qa_list_data)

    def talk(self, info):
        api_url = r"http://www.tuling123.com/openapi/api"
        request_data = {
            "key": self.api_key,
            "info": info,
            "user-id": "292538"
        }
        return self.post_data(api_url, request_data)

    def teach(self, question, answer):
        api_url = r"http://www.tuling123.com/v1/kb/import"
        teach_data = {
            "apikey": self.api_key,
            "data": {
                "list": [{"question": question, "answer": answer}]
            },
        }
        return self.post_data(api_url, teach_data)
