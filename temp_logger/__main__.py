import os

import hubitatcontrol


def get_hub():
    host_env = os.getenv("HUBITAT_HOST")
    token_env = os.getenv("HUBITAT_API_TOKEN")
    app_id_env = os.getenv("HUBITAT_API_APP_ID")
    return hubitatcontrol.get_hub(host=host_env, token=token_env, app_id=app_id_env)


def check_hub():
    h = get_hub()
    if h.devices is None:
        raise Exception("Cannot access Hubitat")
    return h
