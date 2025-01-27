##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital Circuits - 4 Number Conversion
Fourth week's assignments


### 1.1 Following numbers to binary numbers 

### a) $55_{10}$
- $\frac{55}{2} = 27 + 1$
- $\frac{27}{2} = 13 + 1$
- $\frac{13}{2} = 6  + 1$
- $\frac{6}{2}  = 3     $
- $\frac{3}{2}  = 1  + 1$
- $\frac{1}{2}  = 0  + 1$
- $55_{10} = (110 \space 111)_2$

### b) $677_{10}$
- $\frac{677}{2} = 338 + 1$
- $\frac{338}{2} = 169    $
- $\frac{169}{2} = 84 + 1 $
- $\frac{84}{2}  = 42     $
- $\frac{42}{2}  = 21     $
- $\frac{21}{2}  = 10 + 1 $
- $\frac{10}{2}  = 5      $
- $\frac{5}{2}   = 2 + 1  $
- $\frac{2}{2}   = 1      $
- $\frac{1}{2}   = 0 + 1  $
- $677_{10} = (10 \space 1010 \space 0101)_2$

### c) $65_{10}$
- $\frac{65}{2} = 32 + 1$
- $\frac{32}{2} = 16    $
- $\frac{16}{2} = 8     $
- $\frac{8}{2}  = 4     $
- $\frac{4}{2}  = 2     $
- $\frac{2}{2}  = 1     $
- $\frac{1}{2}  = 0 + 1 $
- $65_{10} = (100 \space 0001)_2$

### d) $700_{10}$
- $\frac{700}{2} = 350$
- $\frac{350}{2} = 175$
- $\frac{175}{2} = 87 + 1$
- $\frac{87}{2} = 43 + 1$
- $\frac{43}{2} = 21 + 1$
- $\frac{21}{2} = 10 + 1$
- $\frac{10}{2} = 5$
- $\frac{5}{2} = 2 + 1$
- $\frac{2}{2} = 1$
- $\frac{1}{2} = 0 + 1$
- $700_{10} = (10 \space 1011 \space 1100)_2$

___

### 1.2 Following base-10 numbers to 2-complement 8 bits numbers. 


### a) $+59_{10}$
- $\frac{59}{2} = 29 + 1$
- $\frac{29}{2} = 14 + 1$
- $\frac{14}{2} = 7$
- $\frac{7}{2} = 3 + 1$
- $\frac{3}{2} = 1 + 1$
- $\frac{1}{2} = 0 + 1$
- $59_{10} = (111 \space 011)_2$
- $59_{10} = (0011 \space 1011)_2$ (8-bit 2's complement)

### b) $-1_{10}$
- $1_{10} = 0000 \space 0001_2$
- $-1_{10} = (1111 \space 1111)_2$ (8-bit 2's complement)

### c) $-128_{10}$
- $\frac{128}{2} = 64$
- $\frac{64}{2} = 32$
- $\frac{32}{2} = 16$
- $\frac{16}{2} = 8$
- $\frac{8}{2} = 4$
- $\frac{4}{2} = 2$
- $\frac{2}{2} = 1$
- $\frac{1}{2} = 0 + 1$
- $128_{10} = (1000 \space 0000)_2$
- $-128_{10} = (1000 \space 0000)_2$ (8-bit 2's complement)

### d) $-97_{10}$
- $\frac{97}{2} = 48 + 1$
- $\frac{48}{2} = 24$
- $\frac{24}{2} = 12$
- $\frac{12}{2} = 6$
- $\frac{6}{2} = 3$
- $\frac{3}{2} = 1 + 1$
- $\frac{1}{2} = 0 + 1$
- $97_{10} = (110 \space 0001)_2$ (7-bit)
- $97_{10} = (0110 \space 0001)_2$ (8-bit)
- $-97_{10} = (1001 \space 1111)_2$ (8-bit 2's complement)

___


### 1.3 Following base-10 numbers to 2-complement 8 bits numbers. 
### a) $0x1E5$ → 8 bit binary
- $1_{16} = 0001$
- $E_{16} = 1110$
- $5_{16} = 0101$

Combining gives:
- $0001 \space 1110 \space 0101$ (12 bits)

__0x1E5__ cannot be represented as an 8-bit binary number because its value exceeds the maximum range.    



### b) $0x0F1$ → 8 bit binary
- $0_{16} = 0000$
- $F_{16} = 1111$
- $1_{16} = 0001$

Combining gives:
- $0000 \space 1111 \space 0001$ (12 bits)

For 8-bit representation:
- Last 8 bits: $1111 \space 0001$

__0x0F1__ can be converted to 8-bit binary: __1111 0001__


### c) $0x2E8$ → 10 bit binary
- $2_{16} = 0010$
- $E_{16} = 1110$
- $8_{16} = 1000$

Combining gives:
- $0010 \space 1110 \space 1000$ (12 bits)

To represent as 10 bits:
- Last 10 bits: $1011 \space 1000 \space 00$

__0x2E8__ as a 10-bit binary = __1011 1000 00__



### d) $0000\ 0100\ 1000\ 1011$ → 12 bit binary
- $0000 \space 0100 \space 1000 \space 1011$ (16 bits)
- Removing leading zeros gives: $0100 \space 1000 \space 1011$ (12 bits)

__0000 0100 1000 1011__ as a 12-bit binary: __0100 1000 1011__



### e) $1101\ 1001$ → 16 bit binary
- $1101 \space 1001$ (8 bits)

For 16 bits, add 8 zeros:
- $0000 \space 0000 \space 1101 \space 1001$

__1101 1001__ as a 16-bit binary: __0000 0000 1101 1001__

___

### 1.4 Following signed two’s complement numbers to the given size if possible

### a) $1001\ 1101$ → 12 bit binary
- $1001\ 1101_2$ (8 bits)
- Add 4 bits: $1111\ 1001\ 1101_2$ (12 bits)

__1001 1101__ can be converted to 12-bit: → __1111 1001 1101__



### b) $1110\ 1011\ 1001\ 0001$ → 12 bit binary
- Given: $1110\ 1011\ 1001\ 0001_2$ (16 bits)

__1110 1011 1001 0001__ cannot be converted to 12-bit due to range limitation.



### c) $0xFAC$ → 16 bit binary
- Hexadecimal to binary:
  - $F = 1111$
  - $A = 1010$
  - $C = 1100$

→ $1111\ 1010\ 1100$ (12 bits)
- Add 4 bits: $1111\ 1111\ 1010\ 1100$ (16 bits)

__0xFAC__ can be converted to 16-bit: → __1111 1111 1010 1100__


### d) $0xFF13$ → 10 bit binary
- Hexadecimal to binary:
  - $F = 1111$
  - $F = 1111$
  - $1 = 0001$
  - $3 = 0011$

→ $1111\ 1111\ 0001\ 0011$ (16 bits)

__0xFF13__ cannot be converted to 10-bit binary due to range limitation.

___

### 1.5 Python’s bitwise operators 

```python
from machine import Pin
import time

def leds_as_binary():
    sw = Pin(12, mode = Pin.IN, pull = Pin.PULL_UP)
    LEDs = [Pin(22, Pin.OUT), Pin(21, Pin.OUT),Pin(20, Pin.OUT)]

    b0 = LEDs[0]
    b1 = LEDs[1]
    b2 = LEDs[2]

    count = 0
    i = 0
        
    for led in LEDs:
        led.off()

    while True:
        
        if not sw.value():
            time.sleep(0.25)
            count += 1
            
            if count > 7:
                count = 0
        
        b0.value(count & 1)
        b1.value((count >> 1) & 1)
        b2.value((count >> 2) & 1)
        
leds_as_binary()

```