# 410c-sensor

For China users, need to update the sources.list to choose the faster local Debian servers.
/etc/

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


Need to export LD_LIBRARY_PATH for the libbmm150.so file path.

   

# Pin Mapping
Pin mapping table shows signals pertaining to 40-pin low speed expansion header based on 96Boards Consumer Edition Specification.

| 96Boards Signals	|PIN    |  PIN  |  96Boards    Signals | 
| --------        	| -----:| :----:|                :----:|
|GND		  	|  1	|      2|	GND   		|
|UART0_CTS|	3	|	4	|	PWR_BTN_N	|
|UART0_TxD|	5	|	6	|	RST_BTN_N	|
|UART0_RxD|	7	|	8	|	SPI0_SCLK	|
|UART1_RTS|	9	|	10	|	SPI0_DIN	|
|UART1_TxD|	11	|	12	|	SPI0_CS		|
|UART1_RxD|	13	|	14	|	SPI0_DOUT	|
|I2C0_SCL|	15	|	16	|	PCM_FS		|
|I2C0_SDA|	17	|	18	|	PCM_CLK		|
|I2C1_SCL|	19	|	20	|	PCM_DO		|
|I2C1_SDA|	21	|	22	|	PCM_DI		|
|GPIO-A	|	23	|	24	|	GPIO-B		|
|GPIO-C	|	25	|	26	|	GPIO-D		|
|GPIO-E	|	27	|	28	|	GPIO-F		|
|GPIO-G	|	29	|	30	|	GPIO-H		|
|GPIO-I	|	31	|	32	|	GPIO-J		|
|GPIO-K	|	33	|	34	|	GPIO-L		|
|+1V8	|	35	|	36	|	SYS_DCIN	|
|+5V	|	37	|	38	|	SYC_DCIN	|
|GND	|	39	|	40	|	GND		|

![](https://github.com/cloverpop/410c-sensor/blob/master/jpg/db_pinout.png)

![](https://github.com/cloverpop/410c-sensor/blob/master/jpg/410c-gpio.jpg)

# Reference:

96boards normal Sensor Mezzanine Getting Started
https://github.com/96boards/Sensor_Mezzanine_Getting_Started#using-your-sensors-board

Programming I2C devices with libmraa and libupm
https://www.96boards.org/blog/programing-i2c-devices-libmraa-libupm/

Sensor list of UPM libraries that can be used
http://iotdk.intel.com/docs/master/upm/modules.html

96boards Consumer Edition Specification
https://github.com/96boards/documentation/blob/master/Specifications/96Boards-CE-Specification.pdf
