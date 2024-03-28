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

# krzysio workaround
patch = bytearray(
    [
        # intialize prg banks
        0xA2,  # ldx #$06
        0x06,
        0xA0,  # ldy #$00
        0x00,
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        0xE8,  # inx
        0xC8,  # iny
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        # initialize chr $1000-$1FFF
        0xA2,  # ldx #$02
        0x02,
        0xA0,  # ldy #$00
        0x00,
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        0xE8,  # inx
        0xC8,  # iny
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        0xE8,  # inx
        0xC8,  # iny
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        0xE8,  # inx
        0xC8,  # iny
        0x8E,  # stx $8000
        0x00,
        0x80,
        0x8C,  # sty $8001
        0x01,
        0x80,
        0x4C,  # jmp
    ]
)

target = 0xFF00
romtarget = target - 0x7FF0

patch.extend(rom[0x800C:0x800E])

# verify target is all zeroes
if rom[romtarget : romtarget + len(patch)] != [0] * len(patch):
    raise RuntimeError(
        f"ROM space at ${target:04x} through ${target+len(patch):04x} is in use"
    )

rom[romtarget : romtarget + len(patch)] = patch

rom[0x800C] = target & 0xFF
rom[0x800D] = target >> 8

with open('roll.nes', 'wb') as f:
    f.write(bytearray(rom[:NEW_SIZE]))
