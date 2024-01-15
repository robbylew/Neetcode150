# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of pairs where each pair consists of a car's position and speed.
        # This is done by zipping the position and speed lists together.
        pair = [(p, s) for p, s in zip(position, speed)]

        # Sort the list of pairs in reverse order based on the position of the cars.
        # This is so we can process the cars closest to the target first.
        pair.sort(reverse=True)

        # Initialize an empty stack that will be used to store the time taken for each car
        # to reach the target.
        stack = []

        # Iterate through each pair of position and speed in reverse sorted order.
        for p, s in pair:
            # Calculate the time taken for the current car to reach the target and push it onto the stack.
            stack.append((target - p) / s)

            # If there are at least two elements in the stack and the time of the car at the top
            # of the stack is less than or equal to the time of the car next to top, it means the
            # car at the top of the stack will catch up and form a fleet with the car next to top.
            # Therefore, we pop the top car as it no longer forms a separate fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The remaining elements in the stack represent the separate fleets, so we return the stack's length.
        return len(stack)
