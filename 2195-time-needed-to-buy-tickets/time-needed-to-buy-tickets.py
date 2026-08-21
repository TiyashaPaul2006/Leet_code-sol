from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)

        time = 0

        while queue:
            person = queue.popleft()

            tickets[person] -= 1
            time += 1

            # If the target person finishes, return the time
            if person == k and tickets[person] == 0:
                return time

            # Person goes back to the end if they still need tickets
            if tickets[person] > 0:
                queue.append(person)

        return time
        