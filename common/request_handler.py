import requests
import logging

from urllib3 import request

from  config.setting import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestHandler:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self,method,url,**kwargs):
        full_url = config.BASE_URL + url if url.startswith('/') else url
        kwargs.setdefault('timeout',config.TIMEOUTE)
        try:
            response = self.session.request(method,full_url,**kwargs)
            logger.info(f'Request: {method} {full_url} | Status: {response.status_code}')
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f'Request failed：{method}{full_url}|Error: {e}')
            raise
    def get(self,url,**kwargs):
        return self.send_request('GET',url,**kwargs)

    def post(self,url,**kwargs):
        return self.send_request('POST',url,**kwargs)

request = RequestHandler()