import json
import requests

# Create config file with defaults
# Get input from user to modify the existing configuration settings

# Default config properties and params
CONFIG_FILE_NAME = "config.json"
IPFS_GATEWAY_ADDR = "127.0.0.1"
IPFS_API_PORT = "5001"
IPFS_GATEWAY_PORT = "8080"
STAC_ENDPOINT = "https://stac.easierdata.info"

# Set default configuration dictionary
DEFAULT_CONFIG = {
    "ipfs_endpoint": IPFS_GATEWAY_ADDR,
    "ipfs_api_port": IPFS_API_PORT,
    "ipfs_gateway_port": IPFS_GATEWAY_PORT,
    "stac_endpoint": STAC_ENDPOINT,
}


def check_stac_endpoint():
    # Grab the stac endpoint from the config file
    config = json.load(open(CONFIG_FILE_NAME))
    endpoint = config["stac_endpoint"]
    try:
        resp = requests.get(endpoint)
        if resp.status_code == 200:
            print(f"STAC endpoint {endpoint} is reachable")
        else:
            print(f"STAC endpoint {endpoint} is not reachable")
    except Exception as e:
        print(f"Error: {e}")


def check_ipfs_settings():
    config = json.load(open(CONFIG_FILE_NAME))

    ipfs_addr = config["ipfs_endpoint"]

    # Check if the IPFS gateway port is set correctly
    gateway_port = config["ipfs_gateway_port"]
    # TODO: add the ability to check if the IPFS gateway is reachable
    # url = f"http://{ipfs_addr}:{gateway_port}"

    # Check if the IPFS port is set correctly
    api_port = config["ipfs_api_port"]
    # TODO: add the ability to check if the IPFS port is set
    # url = f"http://{ipfs_addr}:{api_port}/api/v0/version"


def modify_config():
    config_params = DEFAULT_CONFIG
    print("Welcome to the configuration setup wizard")
    print("Please provide the following information to setup the configuration")
    config_params["ipfs_endpoint"] = (
        input(f"Enter the IPFS endpoint (default: {IPFS_GATEWAY_ADDR}): ")
        or IPFS_GATEWAY_ADDR
    )
    config_params["ipfs_api_port"] = (
        input(f"Enter the IPFS API port (default: {IPFS_API_PORT}): ") or IPFS_API_PORT
    )
    config_params["ipfs_gateway_port"] = (
        input(f"Enter the IPFS gateway port (default: {IPFS_GATEWAY_PORT}): ")
        or IPFS_GATEWAY_PORT
    )
    config_params["stac_endpoint"] = (
        input(f"Enter the STAC endpoint (default: {STAC_ENDPOINT}): ") or STAC_ENDPOINT
    )

    # save json payload to file
    save_config(config_params)


def save_config(config_dict):
    json.dump(config_dict, open(CONFIG_FILE_NAME, "w"))
