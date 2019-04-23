Firmware project

I have started on a firmware rewrite project.  I'll capture progress here once in a while.  I am currently decompiling the firmware from disassembled code.  Not ready to share intermediate results of that work.

.ihx firmware has been successfully read from flash.  Version Info:  Nov 21 2016 15:32:51 pi-desktop_iap_rev03 and stored here for safekeeping.  I can reflash pi-desktop boards with this firmware successfully.

Note the revision information matches the board version.

Firmware has been disassembled - .asm file has been uploaded here - decompile work is ongoing.

https://www.st.com/content/st_com/en/products/microcontrollers/stm8-8-bit-mcus/stm8s-series/stm8s-value-line/stm8s005k6.html 
https://www.st.com/resource/en/datasheet/stm8s005k6.pdf 

Part: STM8S005K6T6C MCU

Value line, 16 MHz STM8S 8-bit MCU, 32-Kbyte Flash memory, data EEPROM, 10-bit ADC, timers, UART, SPI, I²C

Decoded:

STM8: Product Class STM8 = ST Microcontroller 8-bit
S : Family type S = standard
005 : Sub-family type 005 = value line medium density
K : Pin count K = 32 pins
6 : Program memory size 6 = 32 Kbyte
T Package type T = LQFP
6: Temperature range 6 = -40 °C to 85 °C
C: Package pitch C = 0.8 mm
 : Packing no character = tray or tube 
 
 Feature summary
 
 32 Pin package with 25 GPIO, 23 external interrupt pins, 8 timer complementary outputs, 7 A/D converter channels, 
 12 High-sick I/Os, 32K medium density fash program memory (bytes), 128 Data EEPROM (bytes), 2K RAM (bytes)
 Peripheral set: Advanced timer control (tim1), general purpose timers (tim2,tim3), basic timer (tim4), SPI, I2C, UART, 
 Window WDG, independent WDG, ADC
 
PINOUT MAPPING to Add-on Board and Pi
 
Here is a FULL mapping by tracing the add-on board components to map to the PI 40 pin GPIO Connector, note where 
NOT CONNECTED is indicated it means there is a resistor missing on the board that creates an open connection.  For example, 
NRST (PA0) can be connected to GPIO19 (Pin 35) via a missing R57 but it is NOT CONNECTED.  Where NO CONNECTION is indicated 
it appears there is no trace from the STM8 pad. PA1 and PA2 are examples of this.  You can see nearly every pin has some potential 
purpose even if unknown at the moment. I did not document the six pins used for power and ground here.

| Pin | Name	| Function and COnnections
| --- | --- | ---
| 1 | PA0 | NRST to J6P1 DEBUG (STLink) ACTIVE & to Pi GPIO19 (Pin 35) - R57 MISSING SO NOT CONNECTED
| 2 | PA1 | NO CONNECTION
| 3 | PA2 | NO CONNECTION
| 8 | PF4 | NO CONNECTION 
|11	| PB5	| I2C_SDA w/ RTC to Pi GPIO02 (Pin 3) ACTIVE
|12	| PB4	| I2C SCL w/ RTC to Pi GPIO03 (Pin 5) ACTIVE
|13 | PB3 | GPIO to TP4 - Purpose UNKNOWN
|14 | PB2 | GPIO to TP5 - Purpose UNKNOWN
|15 | PB1 | GPIO to MSATA Pin 1 via R32/42 MISSING SO NOT CONNECTED
|16 | PB0 | GPIO to MSATA Pin 2 via R33 MISSING SO NOT CONNECTED
|17	| PE5	| SPI_NSS	to Pi GPIO08 (pin 24 SPI-CE0) via R55 MISSING SO NOT CONNECTED
|18	| PC1	| GPIO_Output to LED (OUT PP LOW FAST) via R59 ACTIVE
|19	| PC2	| GPIO_Output	to TP6 & PI LED (OUT PP LOW FAST) via R??? 
|20	| PC3	| GPIO_Input	to KEY (IN PU NO IT) via R20 ACTIVE
|21	| PC4	| GPIO_Output	to POWER (OUT PP LOW FAST) via R5/R7 ACTIVE
|22	| PC5	| SPI_SCK to Pi GPIO11 (Pin 23 SCLK) via R52 MISSING SO NOT CONNECTED
|23	| PC6	| SPI_MOSI to Pi GPIO09 (Pin 21 MISO) via R53 MISSING SO NOT CONNECTED
|24	| PC7	| SPI_MISO to Pi GPIO10 (Pin 19 MOSI) via R54 MISSING SO NOT CONNECTED
|25	| PD0	| GPIO to Pi GPIO26 (Pin 37) NO CODE so UNUSED
|26	| PD1	| SYS_SWIM	to J6P3 DEBUG (STLink) ACTIVE
|27	| PD2	| GPIO_Output	CLOSE to GPIO13 (Pin 33) ACTIVE
|28	| PD3	| GPIO_Input OPEN to GPIO06 (Pin 31) ACTIVE
|29	| PD4	| GPIO (PD4) to Pi GPIO05 (Pin 29) NO CODE so UNUSED
|30	| PD5	| UART2_TX (PD5) to GPIO15 RXD (Pin 10) via R61 MISSING SO NOT CONNECTED
|31	| PD6	| UART2_RX	(PD6) to GPIO14 TDX (Pin 08) via R22 MISSING SO NOT CONNECTED
|32	| PD7	| GPIO_Output to SATA Power (OUT PP LOW FAST) via R12 ACTIVE

Notes:  It is not clear what PC2 driving the PI LED is actually connected to, but there is active code - more investigation is 
needed on a live board.  PB1 and PB2 could have somethign to do with the MSATA connector but I need to research to determine that.

Ideas:
1) Need to use I2C to allow firmware updates without STLink hardware, this code was never completed in the original firmware
2) Once I get the new firmware active a good first project would be to get the UART working, that would allow debugging output
3) Would be interesting to see if MSATA pins could be used to detect if a MSATA device was present or help better control power
4) The SPI pins have MISO/MOSI mismapped, is this a bug or is there something more going on?
5) Could the reset pin be activated for some sort of watchdog behavior

TEST POINTS

TP1 Appears to be connected to the RTC somehow, more investigation needed. TP4-6 are connected to PB3, PB2, PC2 with no known 
purpose, perhaps the test points could be used as solder pads to patch into the hardware to use the pins.

REAL TIME CLOCK

RTC device sharing I2C slave address: read A3h and write A2h is a PCF8563 device TSSOP8 package that is multi function.  There is no
code in the firmware, it uses standard drivers.

https://www.nxp.com/docs/en/data-sheet/PCF8563.pdf

DISCOVERY DOCUMENTS

Evaluation - https://www.st.com/en/evaluation-tools/stm8-mcu-eval-boards.html?querycriteria=productId=LN1644

STM8S VL Discovery - https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm8-mcu-eval-tools/stm8-mcu-eval-boards/stm8svldiscovery.html

Discovery Evaluation Tools - https://www.st.com/en/evaluation-tools/stm8s-discovery.html

Discovery User Manual - https://www.st.com/resource/en/user_manual/cd00250600.pdf 

Discovery Programming Manual - https://www.st.com/resource/en/user_manual/cd00252856.pdf

Developer Tools:  https://www.st.com/en/development-tools/stvd-stm8.html 

TUTORIAL

STM8 Discovery - http://www.benryves.com/tutorials/stm8s-discovery/ 

STM8 Bare Metal - https://lujji.github.io/blog/bare-metal-programming-stm8/ 

OPEN TOOLS

SDCC STM8 Compiler - http://sdcc.sourceforge.net/

STM8 Flash Read/Write - https://github.com/vdudouyt/stm8flash 

firmware disassembly - https://github.com/mikeakohn/naken_asm

firmware file manipulation - https://github.com/gicking/hexfile_merger 

STM8 minimal library - https://github.com/lujji/stm8-bare-min

STM8S ported SDCC library - https://github.com/roshbaby/stm8s-sdcc
