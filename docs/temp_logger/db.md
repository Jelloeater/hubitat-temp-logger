# Module temp_logger.db

## Functions

`setup_db_connection()`
:

## Classes

`ModelBase(*args, **kwargs)`
:

```
### Ancestors (in MRO)

* peewee.Model
* peewee._metaclass_helper_
* peewee.Node

### Descendants

* temp_logger.db.TemperatureDataModel

### Class variables

`DoesNotExist`
:   Common base class for all non-exit exceptions.

`id`
:
```

`TemperatureData(*args, **kwargs)`
:

```
### Ancestors (in MRO)

* temp_logger.db.TemperatureDataModel
* temp_logger.db.ModelBase
* peewee.Model
* peewee._metaclass_helper_
* peewee.Node

### Class variables

`humidity`
:

`id`
:

`sensor_name`
:

`temp`
:

`timestamp`
:

### Methods

`get_single_record(self) ‑> dict`
:

`get_temp_summary(self, num_minutes_to_get: int)`
:

`get_temps(self, num_minutes_to_get: int) ‑> list`
:   Takes time range of past mins, and returns list of db rows w/ temp data

`insert_temp_data(self, sensor_name: str, temp: int, humidity: int) ‑> None`
:
```

`TemperatureDataModel(*args, **kwargs)`
:

```
### Ancestors (in MRO)

* temp_logger.db.ModelBase
* peewee.Model
* peewee._metaclass_helper_
* peewee.Node

### Descendants

* temp_logger.db.TemperatureData

### Class variables

`humidity`
:

`id`
:

`sensor_name`
:

`temp`
:

`timestamp`
:
```
