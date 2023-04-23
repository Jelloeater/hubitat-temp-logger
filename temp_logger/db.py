import datetime

import peewee as p

DB_NAME = "temp_data.db"


def setup_db_connection():
    db = p.SqliteDatabase(DB_NAME)
    db.connect()
    return db


class TemperatureData(p.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_table()

    timestamp = p.DateTimeField(unique=True)
    sensor_name = p.TextField()
    temp = p.IntegerField()

    class Meta:
        database = setup_db_connection()

    def get_temps(self, num_minutes_to_get: int) -> list:
        """
        Takes time range of past mins, and returns list of db rows w/ temp data
        """
        return self.select().where(
            TemperatureData.timestamp < (datetime.datetime.utcnow() + datetime.timedelta(minutes=num_minutes_to_get))
        )

    def get_single_record(self) -> list[object]:
        return self.select().get()

    def get_temp_summary(self, num_minutes_to_get: int):
        pass

    def insert_temp(self, sensor_name: str, temp: int) -> None:
        self.timestamp = datetime.datetime.utcnow()
        self.sensor_name = sensor_name
        self.temp = temp
        self.save()
