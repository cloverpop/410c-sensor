# 410c-sensor

Update SnapDragon410c board with Debian Linux (LXQT)
1. sudo apt-get update
2. sudo apt-get dist-upgrade -u
	Select Y 
3. sudo apt-get install libmraa-dev libupm-dev
   This command above will install the following four libmraa and libupm packages. 
   - libmraa0:		contains only libraa run-time library
   - libmraa-dev:	includes header files to compile program using libmraa
   - libupm0:		contains only libupm run-time library
   - libupm-dev:	includes header files to compile program using libupm
   


Reference:

# 96boards normal Sensor Mezzanine Getting Started
https://github.com/96boards/Sensor_Mezzanine_Getting_Started#using-your-sensors-board

# Programming I2C devices with libmraa and libupm
https://www.96boards.org/blog/programing-i2c-devices-libmraa-libupm/

# Sensor list of UPM libraries that can be used
http://iotdk.intel.com/docs/master/upm/modules.html

# 96boards Consumer Edition Specification
https://github.com/96boards/documentation/blob/master/Specifications/96Boards-CE-Specification.pdf