import os

import hubitatcontrol


class Main:
    def __init__(self):
        host_env = os.getenv("HUBITAT_HOST")
        token_env = os.getenv("HUBITAT_API_TOKEN")
        app_id_env = os.getenv("HUBITAT_API_APP_ID")
        cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")

        self.hub = hubitatcontrol.get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token)
        if self.hub.devices is None:
            raise Exception("Cannot access hub")

    def get_temp_sensors_now(self):
        temp_sensors = self.hub.devices()

        for i in temp_sensors:
            i.name
            i.temperature
            i.humidity
            # TODO Add data log

    def log_temperature_data(self):
        pass


if __name__ == "__main__":
    pass

# TODO Get all temp sensors
# TODO Add DB check

# TODO Add Graph WebGUI https://plotly.com/python/line-charts/
