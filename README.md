# chip8-emulator

Another Chip8 emulator

#Registers

## Special Registers


## 16 general purpose 8-bit Registers :

* V0 
* V1
* V2
* V3
* V4
* V5
* V6
* V7
* V8
* V9
* VA
* VB
* VC
* VD
* VE
* VF

### Register I

16 bit register used to store memory address. Only the 12 lowest are used 

# Instructions

CHIP-8 has 35 opcodes big-endian, each instruction has exactly two bytes.


| Opcode | Assembly command  | 	Explanation       |
|--------|-------------------|--------------------|
| 1NNN   | JUMP  | Jump to the adress NNN         |
| 2NNN   | CALL  | Move the PC to the address NNN |
| 3xNN   | IF_EQ | If Vx == NN skip the next instruction |
| 6xNN   | LOAD  | Load the value NN into register Vx. |
| 8xy0   | LOAD  | Load the value of Vy into register Vx. |
| ANNN   | I     | The interpreter puts the value nnn into register I.
| CxNN   | RAND  | The interpreter picks a random number from 0 to 255, performs a AND with the numberNN then stores it in the register Vx
| DxyN   | DRAW  | Draw the sprites at position (Vx, Vy) from register I until count n

