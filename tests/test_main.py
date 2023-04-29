import os
import random

from dotenv import load_dotenv

import temp_logger.__main__ as tl
import temp_logger.db as db

load_dotenv()
os.environ.setdefault("PL_TEST_MODE", str(True))


class TestMain:
    def test_check_hub(self):
        assert tl.Main.get_hub().devices is not None

    def test_get_temp_data(self):
        x = tl.Main().get_temp_sensors_now()
        assert x is not None


class TestDB:
    @classmethod
    def teardown_class(cls):
        db.TemperatureData.drop_table(safe=False)
        if ".db" in db.setup_db_connection().database:
            os.remove(db.setup_db_connection().database)

    def test_db_insert(self):
        d = db.TemperatureData()
        d.insert_temp_data(sensor_name="TempTempSensor", temp=random.randint(30, 80), humidity=random.randint(0, 100))
        # r = d.get_single_record()
        # assert r is not None
        # d.get_temps(60)

    def test_get_single(self):
        d = db.TemperatureData()
        r = d.get_single_record()
        assert r is not None

    def test_db_min_get(self):
        d = db.TemperatureData()
        temps = d.get_temps(99)
        for i in temps:
            print(i)
        assert temps is not None
