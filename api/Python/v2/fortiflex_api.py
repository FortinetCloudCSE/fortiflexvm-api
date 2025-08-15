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

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Product Types
FGT_VM_BUNDLE = 1                           # FortiGate Virtual Machine - Service Bundle
FMG_VM = 2                                  # FortiManager Virtual Machine
FWB_VM = 3                                  # FortiWeb Virtual Machine - Service Bundle
FGT_VM_LCS = 4                              # FortiGate Virtual Machine - A La Carte Services
FC_EMS_OP = 5                               # FortiClient EMS On-Prem
FAZ_VM = 7                                  # FortiAnalyzer Virtual Machine
FPC_VM = 8                                  # FortiPortal Virtual Machine
FAD_VM = 9                                  # FortiADC Virtual Machine
FORTISOAR_VM = 10                           # FortiSOAR Virtual Machine
FORTIMAIL_VM = 11                           # FortiMail Virtual Machine
FORTINAC_VM = 12                            # FortiNAC Virtual Machine
FGT_HW = 101                                # FortiGate Hardware
FAP_HW = 102                                # FortiAP
FSW_HW = 103                                # FortiSwitch
FWBC_PRIVATE = 202                          # FortiWeb Cloud - Private
FWBC_PUBLIC = 203                           # FortiWeb Cloud - Public
FC_EMS_CLOUD = 204                          # FortiClient EMS Cloud
FORTISASE = 205                             # FortiSASE
FORTIEDR = 206                              # FortiEDR
FORTINDR_CLOUD = 207                        # FortiNDR Cloud
FORTIRECON = 208                            # FortiRecon
SEIM_CLOUD = 209                            # FortiSIEM Cloud
FORTIAPPSEC = 211                           # FortiAppSec
FORTIDLP = 212                              # FortiDLP

# Product Parameters                        # Valid Values

###########################################
# FortiGate VM - Service Bundle           #
###########################################
FGT_VM_BUNDLE_CPU_SIZE = 1                  # 1 - 96 inclusive
FGT_VM_BUNDLE_SVC_PKG = 2                   # "FC" = FortiCare
                                            # "UTP" = UTP
                                            # "ENT" = Enterprise
                                            # "ATP" = ATP
                                            # "UTM" = UTM (no longer available)
FGT_VM_BUNDLE_VDOM_NUM = 10                 # 0 - 500 inclusive
FGT_VM_BUNDLE_FORITI_GUARD_SERVICES = 43    # "FGTAVDB" = Advanced Malware Protection
                                            # "FGTFAIS" =  AI-Based In-line Sandbox
                                            # "FGTISSS" = FortiGuard OT Security Service
                                            # "FGTDLDB" = FortiGuard DLP
                                            # "FGTFGSA" = FortiGuard Attack Surface Security Service
                                            # "FGTFCSS" = FortiConverter Service
FGT_VM_BUNDLE_CLOUD_SERVICES = 44           # "FGTFAMS" = FortiGate Cloud Management
                                            # "FGTSWNM" = SD-WAN Underlay
                                            # "FGTSOCA" = SOCaaS
                                            # "FGTFAZC" = FortiAnalyzer Cloud
                                            # "FGTSWOS" = Cloud-based Overlay-as-a-Service
                                            # "FGTFSPA" = SD-WAN Connector for FortiSASE
FGT_VM_BUNDLE_SUPPORT_SERVICE = 45          # "FGTFCELU" = FC Elite Upgrade

###########################################
# FortiManager VM                         #
###########################################
FMG_VM_MANAGED_DEV = 30                     # 1 - 100000 inclusive
FMG_VM_ADOM_NUM = 9                         # 1 - 100000 inclusive

###########################################
# FortiWeb VMe - Service Bundle           #
###########################################
FWB_VM_CPU_SIZE = 4                         # 1, 2, 4, 8, 16
FWB_VM_SVC_PKG = 5                          # "FWBSTD" = Standard
                                            # "FWBADV" = Advanced

###########################################
# FortiGate VM - A La Carte               #
###########################################
FGT_VM_LCS_CPU_SIZE = 6                     # 1 - 96 inclusive
FGT_VM_LCS_FORTIGUARD_SERVICES = 7          # "IPS" = Intrusion Prevention
                                            # "AVDB" = Advanced Malware
                                            # "FURLDNS" = Web, DNS & Video Filtering
                                            # "FGSA" = Security Rating
                                            # "DLDB" = DLP
                                            # "FAIS" = AI-Based InLine Sandbox
                                            # "FURL" = Web & Video Filtering (no longer available)
                                            # "IOTH" = IOT Detection (no longer available)
                                            # "ISSS" = Industrial Security (no longer available)
FGT_VM_LCS_SUPPORT_SERVICE = 8              # "FC247" = FortiCare Premium
                                            # "ASET" = FortiCare Elite
FGT_VM_LCS_VDOM_NUM = 11                    # 1 - 500 inclusive
FGT_VM_LCS_CLOUD_SERVICES = 12              # "FAMS" = FortiGate Cloud
                                            # "SWNM" = SD-WAN Cloud
                                            # "AFAC" = FortiAnalyzer Cloud with SOCaaS
                                            # "FAZC" = FortiAnalyzer Cloud
                                            # "FMGC" = FortiManager Cloud  (no longer available)

###########################################
# FortiClient EMS On-Prem                 #
###########################################
FC_EMS_OP_ZTNA_NUM = 13                     # 0 - 25000 inclusive
FC_EMS_OP_EPP_ZTNA_NUM = 14                 # 0 - 25000 inclusive
FC_EMS_OP_CHROMEBOOK = 15                   # 0 - 25000 inclusive
FC_EMS_OP_SUPPORT_SERVICE = 16              # "FCTFC247" = FortiCare Premium
FC_EMS_OP_ADDONS = 36                       # "BPS" = FortiCare Best Practice

###########################################
# FortiAnalyzer VM                        #
###########################################
FAZ_VM_DAILY_STORAGE = 21                   # 5 - 8300 inclusive
FAZ_VM_ADOM_NUM = 22                        # 0 - 1200 inclusive
FAZ_VM_SUPPORT_SERVICE = 23                 # "FAZFC247" = FortiCare Premium
FAZ_VM_ADDONS = 58                          # "FAZISSS" = OT Security Service
                                            # "FAZFGSA" = Attack Surface Security Service

###########################################
# FortiPortal VM                          #
###########################################
FPC_VM_MANAGED_DEV = 24                     # 0 - 100000 inclusive

###########################################
# FortiADC VM                             #
###########################################
FAD_VM_CPU_SIZE = 25                        # 1, 2, 4, 8, 16, 32
FAD_VM_SERVICE_PACKAGE = 26                 # "FDVSTD" = Standard
                                            # "FDVADV" = Advanced
                                            # "FDVFC247" = FortiCare Premium

###########################################
# FortiGate Hardware                      #
###########################################
FGT_HW_DEVICE_MODEL = 27                    # "FWF40F" = FortiWifi 40F
                                            # "FGT60E" = FortiGate 60E
                                            # "FGT60F" = FortiGate 60F
                                            # "FWF60F" = FortiWifi 60F
                                            # "FGR60F" = FortiGateRugged 60F
                                            # "FGT61F" = FortiGate 61F
                                            # "FGT70F" = FortiGate 70F
                                            # "FR70FB" = FortiGateRugged 70F
                                            # "FGT80F" = FortiGate 80F
                                            # "FGT81F" = FortiGate 81F
                                            # "FG100E" = FortiGate 100E
                                            # "FG100F" = FortiGate 100F
                                            # "FG101E" = FortiGate 101E
                                            # "FG101F" = FortiGate 101F
                                            # "FG200E" = FortiGate 200E
                                            # "FG200F" = FortiGate 200F
                                            # "FG201F" = FortiGate 201F
                                            # "FG4H0F" = FortiGate 400F
                                            # "FG4H1F" = FortiGate 401F
                                            # "FG6H0F" = FortiGate 600F
                                            # "FG1K0F" = FortiGate 1000F
                                            # "FG180F" = FortiGate 1800F
                                            # "F2K60F " = FortiGate 2600F
                                            # "FG3K0F" = FortiGate 3000F
                                            # "FG3K1F" = FortiGate 3001F
                                            # "FG3K2F" = FortiGate 3200F
                                            # "FG40FI " = FortiGate 40F-3G4G
                                            # "FW40FI" = FortiWifi 40F-3G4G
                                            # "FWF61F" = FortiWifi 61F
                                            # "FR60FI" = FortiGateRugged 60F 3G4G
                                            # "FGT71F" = FortiGate 71F
                                            # "FG80FP" = FortiGate 80F-PoE
                                            # "FG80FB" = FortiGate 80F-Bypass
                                            # "FG80FD " = FortiGate 80F DSL
                                            # "FWF80F" = FortiWiFi 80F-2R
                                            # "FW80FS" = FortiWiFi 80F-2R-3G4G-DSL
                                            # "FWF81F" = FortiWiFi 81F 2R
                                            # "FW81FS" = FortiWiFi 81F-2R-3G4G-DSL
                                            # "FW81FD" = FortiWiFi 81F-2R-3G4G-PoE
                                            # "FW81FP" = FortiWiFi 81F 2R POE
                                            # "FG81FP" = FortiGate 81F-PoE
                                            # "FGT90G " = FortiGate 90G
                                            # "FGT91G " = FortiGate 91G
                                            # "FG201E " = FortiGate 201E
                                            # "FG4H0E " = FortiGate 400E
                                            # "FG4HBE " = FortiGate 400E BYPASS
                                            # "FG4H1E " = FortiGate 401E
                                            # "FD4H1E " = FortiGate 401E DC
                                            # "FG6H0E " = FortiGate 600E
                                            # "FG6H1E " = FortiGate 601E
                                            # "FG6H1F " = FortiGate 601F
                                            # "FG9H0G" = FortiGate 900G
                                            # "FG9H1G" = FortiGate 901G
                                            # "FG1K1F" = FortiGate 1001F
                                            # "FG181F" = FortiGate 1801F
                                            # "FG3K7F" = FortiGate 3700F
                                            # "FG39E6" = FortiGate 3960E
                                            # "FG441F" = FortiGate 4401F
FGT_HW_SERVICE_PACKAGE = 28                 # "FGHWFC247" = FortiCare Premium
                                            # "FGHWFCEL" = FortiCare Elite
                                            # "FGHWATP" = ATP
                                            # "FGHWUTP" = UTP
                                            # "FGHWENT" = Enterprise
FGT_HW_ADDONS = 29                          # "FGHWFCELU" = FortiCare Elite Upgrade
                                            # "FGHWFAMS" = FortiGate Cloud Management
                                            # "FGHWFAIS" = AI-Based In-line Sandbox
                                            # "FGHWSWNM" = SD-WAN Underlay
                                            # "FGHWDLDB" = FortiGuard DLP
                                            # "FGHWFAZC" = FortiAnalyzer Cloud
                                            # "FGHWSOCA" = SOCaaS
                                            # "FGHWMGAS" = Managed FortiGate
                                            # "FGHWSPAL" = SD-WAN Connector for FortiSASE
                                            # "FGHWFCSS" = FortiConverter Service

###########################################
# FortiAP Hardware                        #
###########################################
FAP_HW_DEVICE_MODEL = 55                    # "FP23JF" = FortiAP-23JF
                                            # "FP221E" = FortiAP-221E
                                            # "FP223E" = FortiAP-223E
                                            # "FP231F" = FortiAP-231F
                                            # "FP231G" = FortiAP-231G
                                            # "FP233G" = FortiAP-233G
                                            # "FP234F" = FortiAP-234F
                                            # "FP234G" = FortiAP-234G
                                            # "FP431F" = FortiAP-431F
                                            # "FP431G" = FortiAP-431G
                                            # "FP432F" = FortiAP-432F
                                            # "F432FR" = FortiAP-432FR
                                            # "FP432G" = FortiAP-432G
                                            # "FP433F" = FortiAP-433F
                                            # "FP433G" = FortiAP-433G
                                            # "FP441K" = FortiAP-441K
                                            # "FP443K" = FortiAP-443K
                                            # "FP831F" = FortiAP-831F
                                            # "PU231F" = FortiAP-U231F
                                            # "PU234F" = FortiAP-U234F
                                            # "PU422E" = FortiAP-U422EV
                                            # "PU431F" = FortiAP-U431F
                                            # "PU432F" = FortiAP-U432F
                                            # "PU433F" = FortiAP-U433F
FAP_HW_SERVICE_PACKAGE = 56                 # "FAPHWFC247" = FortiCare Premium
                                            # "FAPHWFCEL" = FortiCare Elite
FAP_HW_ADDONS = 57                          # "FAPHWFSFG" = FortiSASE Cloud Managed AP

###########################################
# FortiWeb Cloud - Private                #
###########################################
FWBC_PRIVATE_AVERAGE_THROUGHPUT = 32        # All Mbps - 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000
FWBC_PRIVATE_WEB_APPLICATIONS = 33          # 0 - 2000 inclusive

###########################################
# FortiWeb Cloud - Public                 #
###########################################
FWBC_PUBLIC_AVERAGE_THROUGHPUT = 34        # All Mbps - 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000
FWBC_PUBLIC_WEB_APPLICATIONS = 35          # 0 - 2000 inclusive

###########################################
# FortiAppSec Cloud                       #
###########################################
FAPPSEC_SERVICE_TYPE = 82                  # "UCWAF" = Cloud WAF, "UCGSLB" = Cloud GSLB
FAPPSEC_WAF_SERVICE_PACKAGE = 83           # "UCWAFSTD" = Standard, "UCWAFADV" = Advanced, "UCWAFENT" = Enterprise
FAPPSEC_WAF_ADDONS = 84                    # "UCSOCA" = SOCaaS
FAPPSEC_THROUGHPUT = 85             # All Mbps - 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000
FAPPSEC_APPLICATIONS = 86               # 0 - 2000 inclusive
FAPPSEC_QPS = 87                          #
FAPPSEC_HEALTH_CHECKS = 88                #


###########################################
# FortiEMS Cloud                          #
###########################################
FC_EMS_CLOUD_ZTNA_NUM = 37                 # Value should be divisible by 25. 0 - 25000 inclusive
FC_EMS_CLOUD_ZTNA_FGF_NUM = 38             # Value should be divisible by 25. 0 - 25000 inclusive
FC_EMS_CLOUD_EPP_ZTNA_NUM = 39             # Value should be divisible by 25. 0 - 25000 inclusive
FC_EMS_CLOUD_EPP_ZTNA_FGF_NUM = 40         # Value should be divisible by 25. 0 - 25000 inclusive
FC_EMS_CLOUD_CHROMEBOOK = 41               # Value should be divisible by 25. 0 - 25000 inclusive
FC_EMS_CLOUD_ADDONS = 42                   # "BPS" = FortiCare Best Practice

###########################################
# FortiSASE                               #
###########################################
FORTISASE_USER = 48                        # 50 - 50000 inclusive
FORTISASE_SERVICEPACK = 49                 # FSASESTD or FSASEADV
FORTISASE_BANDWIDTH = 50                   # 0 or 25 - 10000 inclusive
FORTISASE_DEDICATEDIP = 51                 # 0 or 4 - 65534 inclusive

###########################################
# FortiEDR                                #
###########################################
FORTIEDR_SERVICEPACK = 46                  # FSASESTD or FSASEADV
FORTIEDR_ENDPOINT = 47                     # Read-only
FORTIEDR_ADDONS = 52                       # FEDRXDR = XDR

# FortiCloud_localDev and FortiFlex API Endpoints
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


def configs_create(
    access_token,
    program_serial_number,
    name,
    product_type_id,
    parameters,
    account_id=None,
):
    """Create FortiFlex Configuration - V2"""
    logging.debug("--> Create FortiFlex Configuration...")

    uri = FORTIFLEX_API_BASE_URI + "configs/create"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "programSerialNumber": program_serial_number,
        "name": name,
        "productTypeId": product_type_id,
        "parameters": parameters,
    }

    # accountId is optional
    if account_id:
        body["accountId"] = account_id

    results = requests_post(uri, body, headers)
    return results


def configs_disable(access_token, config_id):
    """Disable FortiFlex Configuration - V2"""
    logging.debug("--> Disable FortiFlex Configuration...")

    uri = FORTIFLEX_API_BASE_URI + "configs/disable"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "id": config_id,
    }

    results = requests_post(uri, body, headers)
    return results


def configs_enable(access_token, config_id):
    """Enable FortiFlex Configuration - V2"""
    logging.debug("--> Enable FortiFlex Configuration...")

    uri = FORTIFLEX_API_BASE_URI + "configs/enable"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "id": config_id,
    }

    results = requests_post(uri, body, headers)
    return results


def configs_update(access_token, config_id, name, parameters):
    """Update FortiFlex Configuration - V2"""
    logging.debug("--> Update FortiFlex Configuration...")

    uri = FORTIFLEX_API_BASE_URI + "configs/update"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "id": config_id,
        "name": name,
        "parameters": parameters,
    }

    results = requests_post(uri, body, headers)
    return results


def groups_list(access_token, account_id):
    """Retrieve FortiFlex Programs List - V2"""
    logging.debug("--> Retrieving FortiFlex Groups...")

    uri = FORTIFLEX_API_BASE_URI + "groups/list"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "accountId": account_id,
    }

    results = requests_post(uri, body, headers)
    return results


def groups_nexttoken(access_token, account_id, folder_path=None, config_id=None):
    """Get FortiFlex Group Next Token - V2"""
    logging.debug("--> Get FortiFlex Group Next Token...")

    uri = FORTIFLEX_API_BASE_URI + "groups/nexttoken"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "accountId": account_id,
        "folderPath": folder_path,
    }

    # configId is optional
    if config_id:
        body["configId"] = config_id

    results = requests_post(uri, body, headers)
    return results


def entitlements_list(
    access_token, config_id=None, account_id=None, program_serial_number=None
):
    """List FortiFlex Entitlements - V2"""
    logging.debug("--> List FortiFlex Entitlements...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/list"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {}

    #  configId OR accountId and programSerialNumber are required OR all three
    if config_id:
        body["configId"] = config_id

    if account_id:
        body["accountId"] = account_id

    if program_serial_number:
        body["programSerialNumber"] = program_serial_number

    results = requests_post(uri, body, headers)
    return results


def entitlements_vm_create(
    access_token, config_id, count, description, folder_path, end_date=None
):
    """Create FortiFlex Virtual Machine Entitlement - V2"""
    logging.debug("--> Create FortiFlex Virtual Machine Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/vm/create"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    # None is a valid value for endDate, defaults to Program End Date
    body = {
        "configId": config_id,
        "count": count,
        "description": description,
        "endDate": end_date,
        "folderPath": folder_path,
    }

    results = requests_post(uri, body, headers)
    return results


def entitlements_hardware_create(
    access_token, config_id, serial_numbers, end_date=None
):
    """Create FortiFlex Hardware Entitlement - V2"""
    logging.debug("--> Create FortiFlex Hardware Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/hardware/create"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    # None is a valid value for endDate, defaults to Program End Date
    body = {
        "configId": config_id,
        "serialNumbers": serial_numbers,
        "endDate": end_date,
    }

    results = requests_post(uri, body, headers)
    return results

def entitlements_cloud_create(
    access_token, config_id, end_date=None
):
    """Create FortiFlex Cloud Entitlement - V2"""
    logging.debug("--> Create FortiFlex Cloud Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/cloud/create"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    # None is a valid value for endDate, defaults to Program End Date
    body = {
        "configId": config_id,
        "endDate": end_date,
    }

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


def entitlements_update(access_token, serial_number, config_id, description, end_date=None):
    """Update FortiFlex Entitlement - V2"""
    logging.debug("--> Update FortiFlex Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/update"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "serialNumber": serial_number,
        "configId": config_id,
        "description": description,
        "endDate": end_date,
    }

    results = requests_post(uri, body, headers)
    return results


def entitlements_reactivate(access_token, serial_number):
    """Reactivate FortiFlex Entitlement - V2"""
    logging.debug("--> Reactivate FortiFlex Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/reactivate"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {"serialNumber": serial_number}

    results = requests_post(uri, body, headers)
    return results


def entitlements_stop(access_token, serial_number):
    """Stop FortiFlex Entitlement - V2"""
    logging.debug("--> Stop FortiFlex Entitlements...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/stop"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {"serialNumber": serial_number}

    results = requests_post(uri, body, headers)
    return results


def entitlements_vm_token(access_token, serial_number):
    """Retrieve FortiFlex VM Entitlement Token - V2"""
    logging.debug("--> Retrieve FortiFlex VM Entitlement Token...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/vm/token"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {"serialNumber": serial_number}

    results = requests_post(uri, body, headers)
    return results

def entitlements_transfer(access_token, source_account_id, source_config_id, target_account_id, target_config_id, serial_numbers):
    """Transfer FortiFlex Entitlement - V2"""
    logging.debug("--> Transfer FortiFlex Entitlement...")

    uri = FORTIFLEX_API_BASE_URI + "entitlements/transfer"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "sourceAccountId": source_account_id,
        "sourceConfigId": source_config_id,
        "targetAccountId": target_account_id,
        "targetConfigId": target_config_id,
        "serialNumbers": serial_numbers,
        }

    results = requests_post(uri, body, headers)
    return results

def tools_calc(
    access_token,
    program_serial_number,
    count,
    product_type_id,
    parameters
):
    """Calculate FortiFlex Points Consumption - V2"""
    logging.debug("--> Calculate FortiFlex Points Consumption...")

    uri = FORTIFLEX_API_BASE_URI + "tools/calc"
    headers = COMMON_HEADERS.copy()
    headers["Authorization"] = f"Bearer {access_token}"

    body = {
        "programSerialNumber": program_serial_number,
        "count": count,
        "productTypeId": product_type_id,
        "parameters": parameters,
    }

    results = requests_post(uri, body, headers)
    return results

if __name__ == "__main__":
    # Set credentials in enviroment or locally
    FORTIFLEX_ACCESS_USERNAME = os.getenv(
        "FORTIFLEX_ACCESS_USERNAME", "api-username-goes-here"
    )
    FORTIFLEX_ACCESS_PASSWORD = os.getenv(
        "FORTIFLEX_ACCESS_PASSWORD", "api-password-goes-here"
    )
    API_CLIENT_ID = os.getenv("API_CLIENT_ID", "flexvm")
    API_GRANT_TYPE = os.getenv("API_GRANT_TYPE", "password")

    #### Get FortiCloud_localDev API Token ####
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
        sys.exit("error retreiving api access token")

    ##### List FortiFlex Programs ####
    ##################################

    programs_list = programs_list(api_access_token)
    if programs_list:
        print(json.dumps(programs_list))

    #### List FortiFlex Configurations ####
    #######################################

    # PROGRAM_SERIAL_NUMBER = 'ELAVMR0000000000'  # Replace with your program serial number
    # ACCOUNT_ID = 1000000                        # Replace with your account ID
    # config_list = configs_list(
    #     api_access_token,
    #     PROGRAM_SERIAL_NUMBER,
    #     ACCOUNT_ID
    # )
    # if config_list:
    #     print(json.dumps(config_list))

    #### Create FortiFlex Configuration ####
    ########################################

    # PRODUCT_TYPE_ID = FGT_VM_BUNDLE
    # NAME = "New Config 2"                      # Replace with your configuration name
    # PARAMETERS = [                             # Replace with your configuration parameters
    #         {
    #             "id": FGT_VM_BUNDLE_CPU_SIZE,
    #             "value": "4"
    #         },
    #         {
    #             "id": FGT_VM_BUNDLE_SVC_PKG,
    #             "value": "UTP"
    #         }
    #     ]

    # config_create = configs_create(
    #     api_access_token,
    #     PROGRAM_SERIAL_NUMBER,
    #     NAME,
    #     PRODUCT_TYPE_ID,
    #     PARAMETERS,
    #     ACCOUNT_ID
    # )

    # if config_create:
    #     print(json.dumps(config_create))

    #### Disable FortiFlex Configuration ####
    #########################################

    # CONFIG_ID = 7090                           # Replace with your configuration ID
    # config_disable = configs_disable(
    #     api_access_token,
    #     CONFIG_ID
    # )
    # if config_disable:
    #     print(json.dumps(config_disable))

    #### Enable FortiFlex Configuration ####
    ########################################

    # CONFIG_ID = 7090                           # Replace with your configuration ID
    # config_enable = configs_enable(
    #     api_access_token,
    #     CONFIG_ID
    # )
    # if config_enable:
    #     print(json.dumps(config_enable))

    #### Update FortiFlex Configuration ####
    ########################################

    # CONFIG_ID = 7090                           # Replace with your configuration ID
    # NAME = "Updated Config 2"                  # Replace with your configuration name
    # PARAMETERS = [                             # Replace with your configuration parameters
    #         {
    #             "id": FGT_VM_BUNDLE_CPU_SIZE,
    #             "value": "2"
    #         },
    #         {
    #             "id": FGT_VM_BUNDLE_SVC_PKG,
    #             "value": "ATP"
    #         }
    #     ]
    # config_update = configs_update(
    #     api_access_token,
    #     CONFIG_ID,
    #     NAME,
    #     PARAMETERS
    # )
    # if config_update:
    #     print(json.dumps(config_update))

    #### List FortiFlex Groups ####
    ###############################

    # ACCOUNT_ID = 1000000                       # Replace with your account ID
    # groups_list = groups_list(api_access_token, ACCOUNT_ID)
    # if groups_list:
    #     print(json.dumps(groups_list))

    #### Get FortiFlex Group Next Token without config ID ####
    ##########################################################

    # ACCOUNT_ID = 1000000                         # Replace with your account ID
    # FOLDER_PATH = 'My Assets/VM04-ATP-01'        # Replace with your folder path
    # groups_nexttoken = groups_nexttoken(
    #     api_access_token,
    #     ACCOUNT_ID,
    #     FOLDER_PATH
    # )

    # if groups_nexttoken:
    #     print(json.dumps(groups_nexttoken))

    #### Get FortiFlex Group Next Token with config ID ####
    #######################################################

    # ACCOUNT_ID = 1000000                         # Replace with your account ID
    # FOLDER_PATH = 'My Assets/VM04-ATP-01'        # Replace with your folder path
    # CONFIG_ID = 4711                             # Replace with your config ID
    # groups_nexttoken = groups_nexttoken(
    #     api_access_token,
    #     ACCOUNT_ID,
    #     FOLDER_PATH,
    #     CONFIG_ID
    # )

    # if groups_nexttoken:
    #     print(json.dumps(groups_nexttoken))

    #### List FortiFlex Entitlements by Program Serial Number and account ID ####
    #############################################################################

    # PROGRAM_SERIAL_NUMBER = "ELAVMR0000000000"   # Replace with your program serial number
    # ACCOUNT_ID = 1000000                         # Replace with your account ID

    # entitlements_list = entitlements_list(
    #     api_access_token,
    #     account_id=ACCOUNT_ID,
    #     program_serial_number=PROGRAM_SERIAL_NUMBER
    # )
    # if entitlements_list:
    #     print(json.dumps(entitlements_list))

    #### List FortiFlex Entitlements by config ID ####
    ##################################################

    # CONFIG_ID = 3476                             # Replace with your config ID
    # entitlements_list = entitlements_list(
    #     api_access_token,
    #     config_id=CONFIG_ID
    # )
    # if entitlements_list:
    #     print(json.dumps(entitlements_list))

    #### Create FortiFlex Virtual Machine Entitlement ####
    ######################################################

    # CONFIG_ID = 3476                             # Replace with your config ID
    # COUNT = 1
    # DESCRIPTION = "FAZ VMs"
    # FOLDER_PATH = "My Assets/VM04-ATP-01"        # Replace with your folder path

    # entitlements_vm_create = entitlements_vm_create(
    #     api_access_token,
    #     CONFIG_ID,
    #     COUNT,
    #     DESCRIPTION,
    #     FOLDER_PATH
    # )

    # if entitlements_vm_create:
    #     print(json.dumps(entitlements_vm_create))

    #### Reactivate FortiFlex Entitlement ####
    ##########################################

    # SERIAL_NUMBER = 'FGVMMLTM21006013'           # Replace with your serial number
    # entitlements_reactivate = entitlements_reactivate(
    #     api_access_token,
    #     SERIAL_NUMBER
    # )

    # if entitlements_reactivate:
    #     print(json.dumps(entitlements_reactivate))

    #### Stop FortiFlex Entitlement ####
    ####################################

    # SERIAL_NUMBER = 'FGVMMLTM21006013'           # Replace with your serial number
    # entitlements_stop = entitlements_stop(
    #     api_access_token,
    #     SERIAL_NUMBER
    # )

    # if entitlements_stop:
    #     print(json.dumps(entitlements_stop))

    #### FortiFlex Entitlements VM Token ####
    #########################################

    # SERIAL_NUMBER = 'FGVMMLTM21006013'           # Replace with your serial number
    # entitlements_vm_token = entitlements_vm_token(
    #     api_access_token,
    #     SERIAL_NUMBER
    # )

    # if entitlements_vm_token:
    #     print(json.dumps(entitlements_vm_token))

    #### Update FortiFlex Entitlements ####
    #######################################

    # SERIAL_NUMBER = 'FGVMMLTM21006013'           # Replace with your serial number
    # CONFIG_ID = 584                              # Replace with your config ID
    # DESCRIPTION = "VM02 UTP"                     # Replace with your description
    # END_DATE = '2024-12-31'                      # Replace with your end date - can be set to None or omitted

    # entitlements_update = entitlements_update(
    #     api_access_token,
    #     SERIAL_NUMBER,
    #     CONFIG_ID,
    #     DESCRIPTION,
    #     END_DATE
    # )

    # if entitlements_update:
    #     print(json.dumps(entitlements_update))

    #### Calculate Points Consumption   ####
    ########################################

    # PROGRAM_SERIAL_NUMBER = 'ELAVMR0000000000'  # Replace with your program serial number
    # COUNT = 2                                   # Replace with count of entitlements
    # PRODUCT_TYPE_ID = FGT_VM_BUNDLE             # Replace with product type ID to calculate

    # PARAMETERS = [                             # Replace with your configuration parameters
    #         {
    #             "id": FGT_VM_BUNDLE_CPU_SIZE,
    #             "value": "2"
    #         },
    #         {
    #             "id": FGT_VM_BUNDLE_SVC_PKG,
    #             "value": "ATP"
    #         }
    #     ]
    # tools_calc = tools_calc(
    #     api_access_token,
    #     PROGRAM_SERIAL_NUMBER,
    #     COUNT,
    #     PRODUCT_TYPE_ID,
    #     PARAMETERS
    # )
    # if tools_calc:
    #     print(json.dumps(tools_calc))

    ##### Retrieve Point Consumption ####
    #####################################

    # config_id alone will retrieve all entitlement point consumption for the config
    # config_id and serial_number will retrieve that entitlement's point consumption
    # account_id and config_id is the same as just config_id
    # account_id alone will retrieve all entitlement point consumption for the account

    # PROGRAM_SERIAL_NUMBER = "ELAVMR0000000000"   # Replace with your program serial number
    # ACCOUNT_ID = 1000000                         # Replace with your account ID
    # STATE_DATE = '2023-12-31'                    # Replace with your state date
    # END_DATE = '2024-12-31'                      # Replace with your end date
    # CONFIG_ID = 4711                             # Replace with your config ID
    # SERIAL_NUMBER = 'FGVMMLTM21006013'           # Replace with your serial number


    # entitlements_points = entitlements_points(
    #     api_access_token,
    #     PROGRAM_SERIAL_NUMBER,
    #     STATE_DATE,
    #     END_DATE,
    #     CONFIG_ID,
    #     SERIAL_NUMBER,
    #     ACCOUNT_ID,
    # )
    # if entitlements_points:
    #     print(json.dumps(entitlements_points))
