'''
For the 60hz case, given a tap count and length, fetch the corresponding
hz measurement. Assumes that taps < 9 and length < 32, the resulting table
should fit within a page. uses bcd for each value
'''

from math import floor

with open('src/hz_table.fab', 'w') as f:
    # initial stuff
    f.write('ct U[224] HZ_TABLE = U[224](\n')
    for i in range(2, 9):
        # write chunks of 8 values
        for j in range(4):
            f.write('    ')
            for k in range(8):
                length = max(8*j + k, 1)
                hz = floor(60*(i-1) / length)
                # hack to take care of impossible values
                if hz >= 100:
                    hz = 0
                f.write(f'${hz:02},')
                if k < 7:
                    f.write(' ')
            f.write('\n')
    f.write(')\n')
