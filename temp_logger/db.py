import datetime

import peewee as p

DB_NAME = "temp_data.db"


def setup_db_connection():
    db = p.SqliteDatabase(
        DB_NAME,  # pragmas={"journal_mode": "wal", "foreign_keys": 1}
    )
    db.connect()
    return db


class ModelBase(p.Model):
    class Meta:
        database = setup_db_connection()


class TemperatureDataModel(ModelBase):
    timestamp = p.DateTimeField(unique=True)
    sensor_name = p.TextField()
    temp = p.IntegerField()
    humidity = p.IntegerField()


class TemperatureData(TemperatureDataModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_table()

    def get_temps(self, num_minutes_to_get: int) -> list:
        """
        Takes time range of past mins, and returns list of db rows w/ temp data
        """
        return self.select().where(
            self.timestamp < (datetime.datetime.utcnow() + datetime.timedelta(minutes=num_minutes_to_get))
        )

    def get_single_record(self) -> dict:
        return self.select().get()

    def get_temp_summary(self, num_minutes_to_get: int):
        pass

    def insert_temp_data(self, sensor_name: str, temp: int, humidity: int) -> None:
        self.timestamp = datetime.datetime.utcnow()
        self.sensor_name = sensor_name
        self.temp = temp
        self.humidity = humidity
        self.save()
