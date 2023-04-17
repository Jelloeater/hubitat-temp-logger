from datetime import time


class Setup:
    def check_db(self):
        pass

    def init_db(self):
        pass


class Data:
    def get_temps(self, num_minutes_to_get: int) -> list[time, {str, int}]:
        """
        Takes time range of past mins, and returns list of db rows w/ temp data
        """
        pass

    def get_temp_summary(self, num_minutes_to_get: int):
        pass

    def insert_temp(self, sensor_name, temp):
        pass
