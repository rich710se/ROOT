[![Build Status][travis_status]][travis] [![PyPI version][pypi_badge]][pypi] _Get information from, and control various Google devices._

***

[HOME][home] | [PLATFORMS][platforms] | [**CLASSES**][classes] | [METHODS][methods] | [FUNCTIONS][functions] | [CLI][cli]

***

This class handles methods that are nested under the `info` endpoint.

## Methods for the `Info` class.

- [get_host](https://ludeeus.github.io/ROOT/methods/wifi/info/get_host)
- [get_wifi_info](https://ludeeus.github.io/ROOT/methods/wifi/info/get_wifi_info)

## Properties for the `Info` class.

- `wifi_host` Return the hostname or IP of the device. _You need to run the [get_host](https://ludeeus.github.io/ROOT/methods/wifi/info/get_host) method before this get populated._
- `wifi_info` Return the device info if any.. _You need to run the [get_host](https://ludeeus.github.io/ROOT/methods/wifi/info/get_host) method before this get populated._


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