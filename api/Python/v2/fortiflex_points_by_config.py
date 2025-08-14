"""
    FortiFlex API
    John McDonough (@movinalot)
    Fortinet

    Scanned by FortiDevSec
"""

# pylint: disable=too-many-arguments, line-too-long

import json
import os
import sys
import logging
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# FortiCloud and FortiFlex API Endpoints
FORTIFLEX_API_BASE_URI = "https://support.fortinet.com/ES/api/fortiflex/v2/"
FORTICARE_AUTH_URI = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"

COMMON_HEADERS = {"Content-type": "application/json", "Accept": "application/json"}


def requests_post(resource_url, json_body, headers):
    """Requests Post"""

    logging.debug(resource_url)
    logging.debug(json_body)
    logging.debug(headers)

    try:
        result = requests.post(
            resource_url, json=json_body, headers=headers, timeout=20
        )
    except requests.exceptions.RequestException as error:
        raise SystemExit(error) from error
    if result.ok:
        return_value = json.loads(result.content)
    else:
        logging.debug(result)
        logging.debug(result.content)
        return_value = None
    return return_value


def get_token(username, password, client_id, grant_type):
    """Get Authentication Token"""

    # logging.debug(username, password, client_id, grant_type)
    logging.debug("--> Retieving FortiFlex API Token...")

    body = {
        "username": username,
        "password": password,
        "client_id": client_id,
        "grant_type": grant_type,
    }

    results = requests_post(FORTICARE_AUTH_URI, body, COMMON_HEADERS)
    return results


def programs_list(access_token):
    """Retrieve FortiFlex Programs List - V2"""

    logging.debug(access_token)
    logging.debug("--> Retrieving FortiFlex Programs...")

    uri = FORTIFLEX_API_BASE_URI + "programs/list"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {}

    results = requests_post(uri, body, headers)
    return results


def configs_list(access_token, program_serial_number, account_id=None):
    """List FortiFlex Configurations - V2"""
    logging.debug("--> List FortiFlex Configurations...")

    uri = FORTIFLEX_API_BASE_URI + "configs/list"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "programSerialNumber": program_serial_number,
    }

    # accountId is optional
    if account_id:
        body["accountId"] = account_id

    results = requests_post(uri, body, headers)
    return results


def entitlements_points(
    access_token,
    program_serial_number,
    start_date,
    end_date,
    config_id=None,
    serial_number=None,
    account_id=None,
):
    """Get FortiFlex Entitlements Points - V2"""
    logging.debug("--> Get FortiFlex Entitlements Points...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/points"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "programSerialNumber": program_serial_number,
        "startDate": start_date,
        "endDate": end_date,
    }

    # config_id alone will retrieve all entitlement point consumption for the config
    # config_id and serial_number will retrieve that entitlement's point consumption
    # account_id and config_id is the same as just config_id
    # account_id alone will retrieve all entitlement point consumption for the account

    if config_id:
        body["configId"] = config_id

    if serial_number:
        body["serialNumber"] = serial_number

    if account_id:
        body["accountId"] = account_id

    results = requests_post(uri, body, headers)
    return results


if __name__ == "__main__":
    # Set credentials in environment or locally
    FORTIFLEX_ACCESS_USERNAME = os.getenv(
        "FORTIFLEX_ACCESS_USERNAME", "api-username-goes-here"
    )
    FORTIFLEX_ACCESS_PASSWORD = os.getenv(
        "FORTIFLEX_ACCESS_PASSWORD", "api-password-goes-here"
    )
    API_CLIENT_ID = os.getenv("API_CLIENT_ID", "flexvm")
    API_GRANT_TYPE = os.getenv("API_GRANT_TYPE", "password")

    #### Get FortiCloud API Token ####
    ##################################
    api_token = get_token(
        FORTIFLEX_ACCESS_USERNAME,
        FORTIFLEX_ACCESS_PASSWORD,
        API_CLIENT_ID,
        API_GRANT_TYPE,
    )
    if api_token:
        api_access_token = api_token["access_token"]
        LOG_MESSAGE = f"API access_token: {api_access_token}"
        logging.debug(LOG_MESSAGE)
        api_access_token = api_token["access_token"]
    else:
        sys.exit("error retrieving api access token")

    ##### Retrieve Point Consumption ####
    #####################################

    # config_id alone will retrieve all entitlement point consumption for the config
    # config_id and serial_number will retrieve that entitlement's point consumption
    # account_id and config_id is the same as just config_id
    # account_id alone will retrieve all entitlement point consumption for the account

    entitlements_points = entitlements_points(
        api_access_token,
        "ELAVMR0000000241",
        "1900-01-01",
        "2025-08-12",
        config_id=679,
        #serial_number="FGVMELTM22000195",
        #account_id="1127201",
    )
    if entitlements_points:
        print(json.dumps(entitlements_points))
