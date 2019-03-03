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
