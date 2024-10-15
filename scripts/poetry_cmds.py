from . import _cmd_utils


def reset_config_file():
    """
    Reset the configuration file to default values
    """
    print("Resetting configuration file to default values")
    _cmd_utils.save_config(_cmd_utils.DEFAULT_CONFIG)


def check_config():
    """
    Check that the configuration file is valid and that the IPFS and STAC endpoints are reachable
    """
    _cmd_utils.check_stac_endpoint()
    _cmd_utils.check_ipfs_settings()


def modify_config_file():
    """
    Modify the configuration file interactively
    """
    _cmd_utils.modify_config()


def print_default_config():
    """
    Print the default configuration file
    """
    print("Configuration property defaults:\n")
    print(_cmd_utils.DEFAULT_CONFIG)
