import sys

file_name = sys.argv[1]

# 16 registrators V0 .. V16
REGISTRATORS = [0]*16


def extract_nibbles(byte):
    first_nibble = byte >> 4
    second_nibble = byte & 0x0F
    return first_nibble, second_nibble


def get_hex_value_from_byte(byte):
    return hex(byte)[2:].zfill(2)


with open(file_name, 'rb') as file:
    instruction =  int.from_bytes(file.read(2), byteorder='big')
    while instruction:
        first_nibble = instruction >> 12
        second_nibble = instruction >> 8 & 0x0F
        second_byte = instruction & 0x00FF
        lowest_12 = instruction & 0x0FFF

        # clear display or Return from a subroutine.
        if first_nibble == 0x0:
            pass

        #jump to address NNN
        elif first_nibble == 0x1:
            print("JUMP $%s" % hex(lowest_12))

        #call address nnn
        elif first_nibble == 0x2:
            print("CALL $%s" % hex(lowest_12))

        elif first_nibble == 0x3:
            print("IF_EQ V%s," % second_nibble, "#0x%s" % get_hex_value_from_byte(second_byte))

        elif first_nibble == 0x4:
            pass
        elif first_nibble == 0x5:
            pass

        # write second_byte in V[second nibble]
        elif first_nibble == 0x6:
            print("LOAD V%s," % second_nibble, "#0x%s" % get_hex_value_from_byte(second_byte))

        #increment register Vx with NN
        elif first_nibble == 0x7:
            print("ADD V%s," % second_nibble, "#0x%s" % get_hex_value_from_byte(second_byte))

        # Logic operations
        elif first_nibble == 0x8:
            second_register, operation = extract_nibbles(second_byte)

            # Assing Vx = Vy
            if operation == 0x0:
                print("LOAD V%s," % second_nibble, "V%s" % second_register)

            if operation == 0x1:
                pass
            elif operation == 0x2:
                pass
            elif operation == 0x3:
                pass
            elif operation == 0x4:
                pass
            elif operation == 0x5:
                pass
            elif operation == 0x6:
                pass
            elif operation == 0x7:
                pass
            elif operation == 0x8:
                pass
            elif operation == 0x9:
                pass
            elif operation == 0xa:
                pass
            elif operation == 0xb:
                pass
            elif operation == 0xc:
                pass
            elif operation == 0xd:
                pass
            elif operation == 0xe:
                pass
            elif operation == 0xf:
                pass

        elif first_nibble == 0x9:
            pass

        elif first_nibble == 0x0:
            pass

        # stores the lowest_12 into register I
        elif first_nibble == 0xa:
            print("I #%s" % hex(lowest_12))

        elif first_nibble == 0xb:
            pass

        # generates a random number and stores it into register Vx
        elif first_nibble == 0xc:
            print("RAND V%s," % second_nibble, "#0x%s" % get_hex_value_from_byte(second_byte))

        # drawn from Vx to Vy
        elif first_nibble == 0xd:
            second_register, value = extract_nibbles(second_byte)
            print("DRAW V%s," % second_nibble, "V%s," % second_register, "#0x%s" % get_hex_value_from_byte(value))

        elif first_nibble == 0xe:
            pass
        elif first_nibble == 0xf:
            pass

        instruction = int.from_bytes(file.read(2), byteorder='big')

