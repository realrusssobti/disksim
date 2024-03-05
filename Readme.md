# Disk Scheduling Simulator
## Author : Russ Sobti

### Overview
This Disk Scheduling Simulator is a comprehensive Python program designed to simulate various disk scheduling algorithms, including First Come First Serve (FCFS), Shortest Seek Time First (SSTF), SCAN, C-SCAN, LOOK, and C-LOOK. The simulator calculates the total distance the disk arm moves to fulfill a series of requests, allowing for performance comparison among the different algorithms.

The program supports custom initial positions and can process disk track requests from a file or generate them randomly. It is aimed at demonstrating the efficiency of disk scheduling algorithms in managing I/O operations on a disk.

### Usage
To run the simulator, use the following command:

``` disk_scheduling_simulator.py <initial_position> [-f <file_with_requests>] ```
Where:

- initial_position: The starting position of the disk arm.
- -f <file_with_requests>: Optional. A file containing disk track requests. If not provided, requests will be generated randomly.
### Note on Performance and Commented Code
The simulator includes commented-out code for performance testing, specifically two functions (mkplot_1 and mkplot_2) designed to generate plots illustrating the effects of random variance and initial position on the total distance traveled by the disk arm. These functions are fully functional but have been commented out to avoid dependencies on matplotlib and numpy, thus simplifying the program's setup and ensuring it runs without needing these additional libraries.

If you wish to use the plotting features, ensure matplotlib and numpy are installed, and uncomment the relevant sections in the code.

### The Algorithms:
- First Come First Serve (FCFS): The disk arm moves to fulfill requests in the order they are received.
- Shortest Seek Time First (SSTF): The disk arm moves to fulfill the request closest to its current position.
- SCAN: The disk arm moves in one direction until it reaches the end of the disk, then reverses direction and fulfills requests in the opposite direction.
- C-SCAN: Similar to SCAN, but the disk arm moves to the end of the disk in one direction, then jumps to the beginning of the disk and fulfills requests in the same direction.
- LOOK: The disk arm moves in one direction until it reaches the end of the disk, then reverses direction and fulfills requests in the opposite direction, without moving to the end of the disk.
- C-LOOK: Similar to LOOK, but the disk arm jumps to the beginning of the disk after reaching the end and fulfills requests in the same direction.