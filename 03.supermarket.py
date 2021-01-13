from collections import deque

name = input()

q = deque()
people_count = 0
while not name == 'End':
    if name == 'Paid':
        while q:
            print(q.popleft())
            people_count = 0
    else:
        q.append(name)
        people_count += 1

    name = input()

print(f'{people_count} people remaining.')
