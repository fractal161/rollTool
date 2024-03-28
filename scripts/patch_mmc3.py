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

# dummy reset patch (credits: zohassadar)
patch = bytearray([0xa2,0x06,0xa0,0x00,0x8e,0x00,0x80,0x8c,0x01,0x80,0xe8,0xc8,0x8e,0x00,0x80,0x8c,0x01,0x80,0x4c])

"""
    ldx #$06
    ldy #$00
    stx $8000
    sty $8001
    inx
    iny
    stx $8000
    sty $8001
    jmp $8161
"""

reset_lo = rom[0x800c]
reset_hi = rom[0x800d]

patch.extend([reset_lo, reset_hi])

rom[0x7f10:0x7f10+len(patch)] = patch
rom[0x800c] = 0x00
rom[0x800d] = 0xFF

with open('roll.nes', 'wb') as f:
    f.write(bytearray(rom[:NEW_SIZE]))
