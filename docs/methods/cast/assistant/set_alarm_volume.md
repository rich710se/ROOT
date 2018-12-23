[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [CLASSES][classes] | [**METHODS**][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

## [Cast](https://ludeeus.github.io/ROOT/platforms#cast) - [Assistant](https://ludeeus.github.io/ROOT/classes/cast/assistant) - [`set_alarm_volume`](https://ludeeus.github.io/ROOT/methods/cast/assistant/set_alarm_volume)

This method takes one parameter. 
This is a numeric value between `0` and `1` like `0.6`

Sample usage:

```python
from googledevices.api.connect import Cast
from googledevices.helpers import gdh_session, gdh_loop, gdh_sleep
from googledevices.utils.convert import format_json

CAST_HOST = '192.168.2.241'
LOOP = gdh_loop()

async def sample():
    """Sample usage."""
    async with gdh_session() as session:
        sample_class = await Cast(CAST_HOST, LOOP, session).assistant()
        test = await sample_class.set_alarm_volume(0.6)
        print(format_json(test))
LOOP.run_until_complete(sample())
```

<!-- menu -->
[travis]: https://travis-ci.com/ludeeus/googledevices
[travis_status]: https://travis-ci.com/ludeeus/googledevices.svg?branch=master
[pypi]:https://pypi.org/project/googledevices/
[pypi_badge]: https://badge.fury.io/py/googledevices.svg
[home]: https://ludeeus.github.io/ROOT
[platforms]: https://ludeeus.github.io/ROOT/platforms
[classes]: https://ludeeus.github.io/ROOT/classes
[methods]: https://ludeeus.github.io/ROOT/methods
[functions]: https://ludeeus.github.io/ROOT/functions
[cli]: https://ludeeus.github.io/ROOT/cli