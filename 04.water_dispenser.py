from collections import deque

water = int(input())
name = input()

people_queue = deque()
end_command = 'End'

while not name == 'Start':
    people_queue.append(name)
    name = input()

while True:
    command = input()
    if command.startswith('r'):
        command_params = command.split()
        command = command_params[0]
        current_water = int(command_params[1])
        water += current_water
    elif command == 'End':
        break
    else:
        command = int(command)
        if water >= command:
            print(f'{people_queue.popleft()} got water')
            water -= command
        else:
            print(f'{people_queue.popleft()} must wait')

print(f'{water} liters left')
