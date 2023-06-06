rom = list(open('roll.nes', 'rb').read())
# set number of chr banks to 3
rom[5] = 0x03
# set mapper to mmc3
rom[6] = 0x40
rom[7] = 0x08

# header + prg + chr
NEW_SIZE = 16+16384*2+8192*3
with open('roll.nes', 'wb') as f:
    f.write(bytearray(rom[:NEW_SIZE]))
