# Module temp_logger.db

## Functions

`setup_db() ‑> peewee.Database`
:

## Classes

`Data()`
:

```
### Methods

`get_temp_summary(self, num_minutes_to_get: int)`
:

`get_temps(self, num_minutes_to_get: int) ‑> list[datetime.time, {<class 'int'>, <class 'str'>}]`
:   Takes time range of past mins, and returns list of db rows w/ temp data

`insert_temp(self, sensor_name, temp)`
:
```

`TemperatureData()`
:

```
### Class variables

`Meta`
:
```
