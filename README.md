# bsbgateway
Read and write data on a [BSB](doc/protocol.md) (Boiler System Bus).

Functionalities offered:

 * [Commandline interface](doc/cmdline.md). Enter `help` to get list of commands, `help <cmd>` for documentation of a specific command.
 * [Web interface](doc/web.md) at port :8081 (e.g. http://localhost:8081)
 * [Logging of fields](doc/logging.md) with preset interval. The logs are written in ASCII `.trace` files and can be loaded with `trace/load_trace.py` into `numpy` arrays.

## Hardware

You need hardware to interface with the bus. In principle, a serial port and a level converter / galvanic decoupler is required.

For a Pi zero W, you can use https://github.com/fredlcore/bsb_lan/blob/master/schematics/BSB-Board%20on%20Raspberry%20Pi%202.jpg
Be sure that the gpio18 is Up :

gpio mode 1 out
gpio write 1 1


## Installation

Dependencies are web.py and pySerial.
On a debian-based system: `sudo apt-get install python-serial python-webpy`

Clone or download the project.

Edit `config.py` to your liking.

Run using `sh bsbgateway.sh`.

For continuous operation, it is (currently) recommendable to run in a `screen` environment like so:

`screen -dmS bsbgateway '/bin/sh /path/to/bsbgateway.sh'`
