import sys
from time import sleep

def print_lyrics():
    lines = [
        ("aku yang jatuh cinta...", 0.10),
        ("haruskah kau ku beri kesempatan", 0.07),
        ("ingin aku jadi kekasih yang baik", 0.07),
        ("berikan aku kesempatan oh.....", 0.08),
        ("tahuka dirimu, tahuka hatimu?", 0.06),
        ("Berulang ku ketuk, aku mencintamu", 0.08),
        ("tapi dirimu, tak pernah sadari", 0.05),
        ("aku yang jatuh cinta", 0.10)
    ]

    delays = [7.2, 3, 2.5, 7.5, 3.5, 4, 3.5, 3.5]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')  # ganti baris

# Panggil fungsi di luar definisinya
print_lyrics()
