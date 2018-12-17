import sys

file_name = sys.argv[1]

# 16 registrators V0 .. V16
REGISTRATORS = [0]*16
with open(file_name, 'rb') as file:
    instruction =  int.from_bytes(file.read(2), byteorder='big')
    while instruction:
        first_nibble = instruction >> 12
        second_nibble = instruction >> 8 & 0x0F
        second_byte = instruction & 0x00FF
        lowerst_12 = instruction & 0x0FFF

        # clear display or Return from a subroutine.
        if first_nibble == 0x0:
            #op = int.from_bytes(file.read(1), byteorder='big')
            pass
        elif first_nibble == 0x1:
            pass
        elif first_nibble == 0x2:
            pass

        elif first_nibble == 0x3:
            print("IF_EQ V%s" % second_nibble, "0x%s" % hex(second_byte)[2:].zfill(2))

        elif first_nibble == 0x4:
            pass
        elif first_nibble == 0x5:
            pass

        # write second_byte in V[second nibble]
        elif first_nibble == 0x6:
            print("LD V%s" % second_nibble, "0x%s" % hex(second_byte)[2:].zfill(2))

        elif first_nibble == 0x7:
            pass
        elif first_nibble == 0x8:
            pass
        elif first_nibble == 0x9:
            pass
        elif first_nibble == 0x0:
            pass

        # stores the lowerst_12 into register I
        elif first_nibble == 0xa:
            print("I %s" % hex(lowerst_12))

        elif first_nibble == 0xb:
            pass

        # generates a random number and stores it into register Vx
        elif first_nibble == 0xc:
            print("RAND V%s" % second_nibble, "0x%s" % hex(second_byte)[2:].zfill(2))

        # drawn from Vx to Vy
        elif first_nibble == 0xd:
            pass
        elif first_nibble == 0xe:
            pass
        elif first_nibble == 0xf:
            pass

        instruction = int.from_bytes(file.read(2), byteorder='big')
