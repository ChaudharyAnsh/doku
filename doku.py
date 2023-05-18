import socket
from sudoku import *
import time

from tqdm import tqdm
import time


print("Complete.")


s = socket.socket()
port = 9002
s.connect(('167.71.234.184', port))

pre = s.recv(198)
print(pre)

for i in range(50):

    # jugad 1
    buf = 1794 + 45
    start = 45
    end = -16

    # jugad 2
    if (i == 0):
        buf = 1794
        start = 0
        end = -16

    # jugad 3
    if (i >= 9):
        buf = 1794 + 46
        start = 46
        end = -16

    x = list(s.recv(2048))
    time.sleep(1)

    # print(len(x))
    while (len(x) < buf):
        y = list(s.recv(buf-len(x)))
        for i in y:
            x.append(i)
        time.sleep(1)

    x = x[start:end]

    count = 0
    for i in range(2, len(x)-2):
        if (x[i-1] == 32 and x[i+1] == 32 and x[i+2] != 32 and x[i+3] != 32):
            if (x[i] == 32):
                grid[int(count//9)][count % 9] = 0
            else:
                grid[int(count//9)][count % 9] = x[i] - ord('0')

            grid_indices[int(count//9)][count % 9] = i
            count += 1

    Suduko(grid, 0, 0)
    count = 0

    print(f'Puzzle {i}: \n')
    print(bytes(x).decode('utf-8'))
    print()
    print()

    ans = b''

    for i in range(9):
        for j in range(9):
            grid[i][j] += 48

    for i in range(len(x)):
        if (count == 81):
            ans += x[i].to_bytes(1, 'big')
            continue

        if (i == grid_indices[int(count//9)][count % 9]):
            ans += grid[int(count//9)][count % 9].to_bytes(1, 'big')
            count += 1
        else:
            ans += x[i].to_bytes(1, 'big')

    ans
    print(f'Answer {i}: \n')
    print(bytes(ans).decode('utf-8'))
    print()
    s.send(ans)
result = s.recv(2048).decode('utf-8')
print(result)
