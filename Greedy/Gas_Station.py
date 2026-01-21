"""
LeetCode 134: Gas Station
Difficulty: Medium

Approach:
- Greedy
- If total gas < total cost → return -1
- Track current fuel and reset start when fuel < 0

Time Complexity: O(n)
Space Complexity: O(1)
"""

def canCompleteCircuit(gas, cost):
    total_gas = 0
    curr_gas = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        curr_gas += gas[i] - cost[i]

        if curr_gas < 0:
            start = i + 1
            curr_gas = 0

    return start if total_gas >= 0 else -1
