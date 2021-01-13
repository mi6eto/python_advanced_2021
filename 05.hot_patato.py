from collections import deque

name = input().split()
count = int(input())

q = deque(name)
counter = 0

while len(q) > 1:
    counter += 1
    current_player = q.popleft()
    if counter == count:
        print(f'Removed {current_player}')
        counter = 0
    else:
        q.append(current_player)

print(f'Last is {q.popleft()}')
