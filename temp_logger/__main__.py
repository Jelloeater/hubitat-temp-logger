import os

import hubitatcontrol


class Main:
    def __init__(self):
        self.hub = self.get_hub()
        if self.hub.devices is None:
            raise Exception("Cannot access hub")

    @staticmethod
    def get_hub():
        host_env = os.getenv("HUBITAT_HOST")
        token_env = os.getenv("HUBITAT_API_TOKEN")
        app_id_env = os.getenv("HUBITAT_API_APP_ID")
        return hubitatcontrol.get_hub(host=host_env, token=token_env, app_id=app_id_env)

    def get_temp_sensors_now(self):
        pass

    def log_temperature_data(self):
        pass


if __name__ == "__main__":
    pass

# TODO Get all temp sensors
# TODO Add DB check
