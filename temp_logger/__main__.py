import os

import hubitatcontrol

import temp_logger.db as db


class Main:
    def __init__(self):
        host_env = os.getenv("HUBITAT_HOST")
        token_env = os.getenv("HUBITAT_API_TOKEN")
        app_id_env = os.getenv("HUBITAT_API_APP_ID")
        cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")

        self.hub = hubitatcontrol.get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token)
        if self.hub.devices is None:
            raise Exception("Cannot access hub")

    def log_temperature_data(self):
        temp_sensors = hubitatcontrol.get_all_environmental_sensors(self.hub)

        for i in temp_sensors:
            db.TemperatureData().insert_temp_data(sensor_name=i.name, temp=i.temperature, humidity=i.humidity)


if __name__ == "__main__":
    pass

# TODO Get all temp sensors
# TODO Add DB check

# TODO Add Graph WebGUI https://plotly.com/python/line-charts/
