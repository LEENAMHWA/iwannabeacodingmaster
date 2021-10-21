import sys

N, K = list(map(int, sys.stdin.readline().split()))
convey_arr = list(map(int, sys.stdin.readline().split()))

is_robot = [0] * N
fault_ea = 0
try_n = 0

while True:
    try_n += 1
    
    print(is_robot)

    # Convey ++
    tmp_convey = []
    for tmp_idx in range(0, (N * 2)):
        tmp_convey.append(convey_arr[(len(convey_arr) - 1 + tmp_idx) % len(convey_arr)])
    convey_arr = tmp_convey.copy()

    # Robot ++         
    for robot_idx in range(N-2,-1,-1):
        is_robot[robot_idx + 1] = is_robot[robot_idx]
        is_robot[robot_idx] = 0
    # Robot ++ end

    is_robot[N - 1] = 0

    # Additional Robot ++
    for robot_idx in range(N-2,-1,-1):
        if (convey_arr[robot_idx + 1] > 0) and (is_robot[robot_idx + 1] == 0):
            is_robot[robot_idx + 1] = is_robot[robot_idx]
            is_robot[robot_idx] = 0

            convey_arr[robot_idx + 1] -= 1
            if convey_arr[robot_idx + 1] == 0:
                fault_ea += 1

    is_robot[N - 1] = 0            
    
    # IN
    if convey_arr[0] > 0:
        convey_arr[0] -= 1
        is_robot[0] = 1

        if convey_arr[0] == 0:
            fault_ea += 1
        
    if fault_ea >= K:
        print(try_n)
        break

