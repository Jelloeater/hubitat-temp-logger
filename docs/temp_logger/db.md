# Module temp_logger.db

## Functions

`setup_db_connection()`
:

## Classes

`TemperatureData(*args, **kwargs)`
:

```
### Ancestors (in MRO)

* peewee.Model
* peewee._metaclass_helper_
* peewee.Node

### Class variables

`DoesNotExist`
:   Common base class for all non-exit exceptions.

`id`
:

`sensor_name`
:

`temp`
:

`timestamp`
:

### Methods

`get_single_record(self) ‑> list[object]`
:

`get_temp_summary(self, num_minutes_to_get: int)`
:

`get_temps(self, num_minutes_to_get: int) ‑> list`
:   Takes time range of past mins, and returns list of db rows w/ temp data

`insert_temp(self, sensor_name: str, temp: int) ‑> None`
:
```
