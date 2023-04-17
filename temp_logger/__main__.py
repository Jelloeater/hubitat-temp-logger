import os

import hubitatcontrol


class Main:
    def __init__(self):
        host_env = os.getenv("HUBITAT_HOST")
        token_env = os.getenv("HUBITAT_API_TOKEN")
        app_id_env = os.getenv("HUBITAT_API_APP_ID")
        self.hub = hubitatcontrol.get_hub(host=host_env, token=token_env, app_id=app_id_env)
        if self.hub.devices is None:
            raise Exception("Cannot access hub")

    def get_temp_sensors(self):
        pass

    def log_temperature_data(self):
        pass


if __name__ == "__main__":
    pass

# TODO Get all temp sensors
# TODO Add DB check
