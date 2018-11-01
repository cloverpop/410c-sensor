#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdint.h>
#include <string.h>
#include <sys/time.h>

#include "libsoc_i2c.h"
#include "libsoc_debug.h"

/**
 * 
 * This i2c_test is intended to be run on beaglebone white hardware
 * and uses the I2C2 which is device id 1 by default, as not all 3 I2C
 * busses are actiavted, and i2c devices are enumerated by amount.
 * 
 * The i2c bus is on pins P9_19 as SCL, P9_20 as SDA
 *
 * The BeagleBone is connected to a ST MicroElectronics M24C01-WBN6P 1K 
 * EEPROM
 *
 * The test covers writing 32 bytes of random data, to a random page
 * on the EEPROM. It then reads the page back, and compares the data
 * read against the data sent, the test passes if all data matches.
 * 
 */
 
#define I2C_BUS   0
#define ADDRESS   0x29

#define BUFF_LEN  32

uint8_t tx[BUFF_LEN];
uint8_t rx[BUFF_LEN];

int read_product_id(i2c* dev)
{
  tx[0] = 0x90;

  libsoc_i2c_write( dev, tx, 1);
  libsoc_i2c_read( dev, rx, 1);

  printf("Product ID:[0x%x]", rx[0]);
  
  if ( rx[0] == 0x83 )
      printf("BHI160 | BHI160B product\n");
  else
      printf("Unknown BHI160 product\n");
}


int read_revision_id(i2c* dev)
{
  tx[0] = 0x91;
  rx[0] = 0x91;
  
  libsoc_i2c_write( dev, tx, 1);
  libsoc_i2c_read( dev, rx, 1);

  printf("revision_id:[%x]\n", rx[0]);
}

int read_rom_version(i2c* dev)
{
  tx[0] = 0x70;
  rx[0] = 0x00;

  libsoc_i2c_write( dev, tx, 1);
  libsoc_i2c_read( dev, rx, 2);

  uint16_t rv=0;
  rv = rx[1] << 8 | rx[0]; 

  printf("ROM ver:[%x]\n", rv);
}

int read_ram_version(i2c* dev)
{
  tx[0] = 0x72;
  rx[0] = 0x00;

  libsoc_i2c_write( dev, tx, 1);
  libsoc_i2c_read( dev, rx, 2);

  uint16_t rv=0;
  rv = rx[1] << 8 | rx[0];

  printf("RAM ver:[%x]\n", rv);
}


int main()
{
  uint8_t tx[BUFF_LEN];
  uint8_t rx[BUFF_LEN];

  memset(tx, 0x00, BUFF_LEN);
  memset(rx, 0x00, BUFF_LEN);

  // Turn debug on
  libsoc_set_debug(1);
   
  // Initialise i2c struct
  i2c *i2c_dev = libsoc_i2c_init(I2C_BUS, ADDRESS);
  
  if (i2c_dev == NULL) {
    printf("Failed to get I2C device!\n");
    return EXIT_FAILURE;
  }
  
  // Set the timeout for the i2c slave
  libsoc_i2c_set_timeout(i2c_dev, 1);
  
  // Setup the seed for the random number
  struct timeval t1;
  gettimeofday(&t1, NULL);
  srand(t1.tv_usec * t1.tv_sec);
  
  tx[0] = 0x9B;
  tx[1] = 0x1;
  libsoc_i2c_write(i2c_dev, tx, 1);
  usleep(100);
  printf("soft reset\n");

  read_product_id( i2c_dev );
  read_revision_id( i2c_dev);
  read_rom_version( i2c_dev );
  read_ram_version( i2c_dev );


  printf("Reading data\n");
  
  // Free i2c struct
  libsoc_i2c_free(i2c_dev);

  return EXIT_SUCCESS;
}
