#!/usr/bin/python

from time	import sleep
from libsoc import gpio
from libsoc import spi

SPI0_CS_N = 18

# chip ID
BMP3_CHIP_ID  	= 0x50

BMP3_CMD_RDY	= 0x10
BMP3_DRDY_PRESS	= 0x20
BMP3_DRDY_TEMP	= 0x40

MODE_SLEEP	= 0
MODE_FORCED = 1
MODE_NORMAL	= 2

# name Register Address
BMP3_CHIP_ID_ADDR 		= 0x00
BMP3_ERR_REG_ADDR 		= 0x02
BMP3_SENS_STATUS_REG_ADDR = 0x03
BMP3_DATA_ADDR			= 0x04
BMP3_EVENT_ADDR			= 0x10
BMP3_INT_STATUS_REG_ADDR = 0x11
BMP3_FIFO_LENGTH_ADDR	 = 0x12
BMP3_FIFO_DATA_ADDR		 = 0x14
BMP3_FIFO_WM_ADDR		 = 0x15
BMP3_FIFO_CONFIG_1_ADDR	 = 0x17
BMP3_FIFO_CONFIG_2_ADDR	 = 0x18
BMP3_INT_CTRL_ADDR		 = 0x19
BMP3_IF_CONF_ADDR		 = 0x1A
BMP3_PWR_CTRL_ADDR		 = 0x1B
BMP3_OSR_ADDR			 = 0X1C
BMP3_CALIB_DATA_ADDR	 = 0x31
BMP3_CMD_ADDR			 = 0x7E

#-----------------------------

global op_mode
op_mode = 0

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return result


# reg_addr is int type
def get_regs(reg_addr, reg_data, len, dev):
	assert reg_addr != None
	assert reg_data != None
	assert len > 0
	assert dev != 0
	
	reg_addr = reg_addr | 0x80
	tx = int_to_bytes(reg_addr, 1)
	print tx
	rx = dev.rw(1, tx)
	

def set_regs(reg_addr, reg_data, len, dev):
	assert reg_addr != None
	assert reg_data != None
	assert len > 0
	assert dev != 0
	
	for i in range(len):
		dev.write(reg_data[i])
	
	pass

def soft_reset(spi_dev):
	assert spi_dev!= None
	
	tx = b'\x83'	# 0x03
	rx = spi_dev.rw(1, tx)
	if rx[0] == 0x10:
		rst_tx = b'\x7E'
		rst_rx = spi_dev.write(rst_tx)
		sleep(0.02)
		
		err_tx = b'\x02'
		err_rx = spi_dev.rw(1, err_tx)
	
	pass

# mode
# 0 = sleep 1 = forced 2 = normal 
#
def set_op_mode(mode):
	assert mode!= None
	
	global op_mode
	
	if op_mode == mode:
		print("Skip the same mode setting")
		return
	
	
	pass

def single_sample():
	#set forced mode
	set_op_mode(MODE_FORCED)
	
	pass

def get_chip_id(spi_dev):	
	# read CHIP ID
	tx = b'\x80' 	# 0x00
	rx = spi_dev.rw(1, tx)
	id = bytes_to_int(rx)
	print("ChipID:%x" %id )
	if id != BMP3_CHIP_ID:
		raise IOError("Detect wrong BMP3x chip ID")

def main():
    spi.SPI.set_debug(1)
    gpio_cs = gpio.GPIO(SPI0_CS_N, gpio.DIRECTION_OUTPUT)
    res = gpio.request_gpios([gpio_cs])
	
	# enable SPI
	gpio_cs.set_high()
	sleep(0.00001)
	gpio_cs.set_low()
	
	spi_dev = spi.SPI(0, 0, spi.MODE_0, 10000, spi.BITS_8)
	
	# enable debug
	spi_dev.set_debug(1)

	get_chip_id(spi_dev)

	soft_reset(spi_dev)

	pass

if __name__ == '__main__':
    main()