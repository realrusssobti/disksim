import argparse
import random
# import matplotlib.pyplot as plt
# import numpy as np

# Disk scheduling functions defined here (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)
def fcfs(initial_position, requests):
    distance = abs(initial_position - requests[0])
    for i in range(1, len(requests)):
        distance += abs(requests[i] - requests[i-1])
    return distance

def sstf(initial_position, requests):
    position = initial_position
    distance = 0
    requests = requests.copy()

    while requests:
        closest = min(requests, key=lambda x: abs(x - position))
        distance += abs(position - closest)
        position = closest
        requests.remove(closest)

    return distance

def scan(initial_position, requests, disk_size=5000):
    direction = "right"  # Assume initial direction is towards the higher numbered cylinders
    distance = 0
    position = initial_position
    sorted_requests = sorted(requests + [0, disk_size - 1])

    # Split requests into those less than and greater than the initial position
    left = [request for request in sorted_requests if request < position]
    right = [request for request in sorted_requests if request > position]

    # Process requests in the direction of initial movement, then reverse
    if direction == "right":
        for request in right:
            distance += abs(position - request)
            position = request
        # Reverse direction at the end of the disk
        if left:
            distance += abs(position - 0)  # Move to the start of the disk
            position = 0
        for request in reversed(left):
            distance += abs(position - request)
            position = request
    else:
        for request in reversed(left):
            distance += abs(position - request)
            position = request
        # Reverse direction at the start of the disk
        if right:
            distance += abs(position - (disk_size - 1))  # Move to the end of the disk
            position = disk_size - 1
        for request in right:
            distance += abs(position - request)
            position = request

    return distance


def c_scan(initial_position, requests, disk_size=5000):
    position = initial_position
    requests.copy().sort()
    distance = 0

    if position > requests[-1]:
        distance += disk_size - position + disk_size + requests[-1]
    elif position < requests[0]:
        distance += requests[-1] - position
    else:
        distance += disk_size - position + disk_size + requests[-1] - requests[0]

    return distance

def look(initial_position, requests, disk_size=5000):
    position = initial_position
    distance = 0
    requests.copy().sort()

    if position < requests[0] or position > requests[-1]:
        distance += abs(position - requests[0]) + abs(requests[-1] - requests[0])
    else:
        left = [r for r in requests if r <= position]
        right = [r for r in requests if r > position]
        distance += max(position - min(left, default=position), max(right, default=position) - position)

    return distance

def c_look(initial_position, requests):
    position = initial_position
    distance = 0
    requests.copy().sort()

    if position > requests[-1]:
        distance += position - requests[0]
    elif position < requests[0]:
        distance += requests[-1] - position
    else:
        left = [r for r in requests if r <= position]
        right = [r for r in requests if r > position]
        distance += requests[-1] - min(left) + max(right) - requests[0]

    return distance


def parse_arguments():
    parser = argparse.ArgumentParser(description='Disk Scheduling Simulator')
    parser.add_argument('initial_position', type=int, help='Initial position of the disk arm')
    parser.add_argument('-f', '--file', type=str, help='File containing disk track requests')
    return parser.parse_args()


def read_or_generate_requests(filename, num_requests=100, disk_size=5000):
    if filename:
        with open(filename, 'r') as file:
            requests = [int(line.strip()) for line in file.readlines()]
    else:
        requests = [random.randint(0, disk_size - 1) for _ in range(num_requests)]
    return requests


def main():
    args = parse_arguments()
    requests = read_or_generate_requests(args.file)

    print(f"FCFS: {fcfs(args.initial_position, requests)}")
    print(f"SSTF: {sstf(args.initial_position, requests)}")
    print(f"SCAN: {scan(args.initial_position, requests)}")
    print(f"C-SCAN: {c_scan(args.initial_position, requests)}")
    print(f"LOOK: {look(args.initial_position, requests)}")
    print(f"C-LOOK: {c_look(args.initial_position, requests)}")

#
# # The effect of the random variance on the total distance
# def mkplot_1():
#     # generate 100 random requests
#     requests = [[random.randint(0, 5000) for _ in range(100)] for _ in range(100)]
#     # run all the algorithms and store the results in represeentative lists
#     fcfs_results = [fcfs(100, r) for r in requests]
#     sstf_results = [sstf(100, r) for r in requests]
#     scan_results = [scan(100, r) for r in requests]
#     c_scan_results = [c_scan(100, r) for r in requests]
#     look_results = [look(100, r) for r in requests]
#     c_look_results = [c_look(100, r) for r in requests]
#     # plot the results
#     x = np.arange(100)
#     plt.plot(x, fcfs_results, label='FCFS')
#     plt.plot(x, sstf_results, label='SSTF')
#     plt.plot(x, scan_results, label='SCAN')
#     plt.plot(x, c_scan_results, label='C-SCAN')
#     plt.plot(x, look_results, label='LOOK')
#     plt.plot(x, c_look_results, label='C-LOOK')
#     plt.xlabel('Simulation Number')
#     plt.ylabel('Total Distance')
#     plt.title('Disk Scheduling Simulation')
#     plt.legend()
#     plt.show()
#
#
# # The effect of the initial position on the total distance
# def mkplot_2():
#     # start position anywhere from 0 to 5000
#     start_positions = [i for i in range(5000)]
#     # generate 100 random requests
#     requests = [random.randint(0, 5000) for _ in range(100)]
#
#     # run all the algorithms and store the results in represeentative lists
#     fcfs_results = [fcfs(i, requests) for i in start_positions]
#     sstf_results = [sstf(i, requests) for i in start_positions]
#     scan_results = [scan(i, requests) for i in start_positions]
#     c_scan_results = [c_scan(i, requests) for i in start_positions]
#     look_results = [look(i, requests) for i in start_positions]
#     c_look_results = [c_look(i, requests) for i in start_positions]
#     # plot the results
#     x = np.arange(5000)
#     plt.plot(x, fcfs_results, label='FCFS')
#     plt.plot(x, sstf_results, label='SSTF')
#     plt.plot(x, scan_results, label='SCAN')
#     plt.plot(x, c_scan_results, label='C-SCAN')
#     plt.plot(x, look_results, label='LOOK')
#     plt.plot(x, c_look_results, label='C-LOOK')
#     plt.xlabel('Initial Position')
#     plt.ylabel('Total Distance')
#     plt.title('Disk Scheduling Simulation')
#     plt.legend()
#     plt.show()
#

if __name__ == '__main__':
    main()
    # mkplot_1()
    # mkplot_2()
