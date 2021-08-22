def solution(bridge_length, weight, truck_weights):
    truck_in_bridge = []
    time_checker = []
    # answer == total_time
    answer = 0
    while True:
        if len(time_checker) == 0 and len(truck_weights) == 0:
            break

        answer += 1
        if len(time_checker) > 0:
            time_checker = [x+1 for x in time_checker]
            if time_checker[0] == bridge_length:
                time_checker.pop(0)
                truck_in_bridge.pop(0)

        if len(truck_weights) == 0:
            continue

        if bridge_length == truck_in_bridge or sum(truck_in_bridge) + truck_weights[0] > weight:
            diff = bridge_length - time_checker[0] - 1
            time_checker = [x+diff for x in time_checker]
            answer += diff
            continue
        elif len(truck_in_bridge) == 0 or sum(truck_in_bridge) + truck_weights[0] <= weight:
            truck_in_bridge.append(truck_weights[0])
            time_checker.append(0)
            truck_weights.pop(0)
            continue

    return answer
