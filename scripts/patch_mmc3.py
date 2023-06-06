PRG_BANKS = 2
CHR_BANKS = 2
# header + prg + chr
NEW_SIZE = 16 + 16384*PRG_BANKS + 8192*CHR_BANKS

rom = list(open('roll.nes', 'rb').read())
# set number of chr banks to 2 (4 tilesets)
rom[5] = CHR_BANKS
# set mapper to mmc3
rom[6] = 0x41
rom[7] = 0x08

with open('roll.nes', 'wb') as f:
    f.write(bytearray(rom[:NEW_SIZE]))
