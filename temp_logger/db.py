from datetime import time

from peewee import Database, InterfaceError, SqliteDatabase


def setup_db() -> Database:
    db = SqliteDatabase("temp_data.db")
    try:
        db.connect()
    except InterfaceError():
        # TODO setup DB
        pass
    return db


class TemperatureData:
    class Meta:
        database = setup_db()

    pass


class Data:
    def __init__(self):
        self.db = setup_db()

    def get_temps(self, num_minutes_to_get: int) -> list[time, {str, int}]:
        """
        Takes time range of past mins, and returns list of db rows w/ temp data
        """
        pass

    def get_temp_summary(self, num_minutes_to_get: int):
        pass

    def insert_temp(self, sensor_name, temp):
        pass
