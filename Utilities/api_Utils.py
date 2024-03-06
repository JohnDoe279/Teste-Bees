import logging
import requests
from Utilities import configReader
from Utilities.log_Util import Logger

log = Logger(__name__, logging.INFO)


class API_Utils:
    api_url = configReader.readConfig("api info", "api_url")
    # global response

    def get_api(self):
        api_base_url = self.api_url
        log.logger.info("API Url: " + str(api_base_url))
        return api_base_url

    def get_request(self, endpoint):
        url = self.api_url + endpoint
        response = requests.get(url)
        log.logger.info("Response " + str(response.status_code))
        log.logger.info("Payload:" + str(response.json()))
        return response
