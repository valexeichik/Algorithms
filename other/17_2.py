import mmap
import heapq

class Task:
    def __init__(self, i, preparation, duration):
        self.preparation = preparation
        self.duration = duration
        self.index = i

    def __lt__(self, other):
        if self.preparation == other.preparation:
            return self.duration < other.duration
        return self.preparation < other.preparation
    
    def copy(self):
        return Task(self.index, self.preparation, self.duration)
    
def main(): 
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline().strip())
            tasks = []
            for i in range(n):
                preparation, duration = map(int, mfile.readline().strip().split())
                task = Task(i, preparation, duration)
                heapq.heappush(tasks, task)

    current_time = 0
    total_penalty = 0
    order = []

    for _ in range(n - 1):
        task1 = heapq.heappop(tasks)
        task2 = heapq.heappop(tasks)

        if max(0, max(current_time, task1.preparation) + task1.duration - task2.preparation) \
            <= max(0, max(current_time, task2.preparation) + task2.duration - task1.preparation):
            current_task = task1.copy()
            heapq.heappush(tasks, task2)
        else:
            current_task = task2.copy()
            heapq.heappush(tasks, task1)

        current_time = max(current_time, current_task.preparation)
        order.append(current_task.index + 1)
        total_penalty += max(0, current_time - current_task.preparation)
        current_time += current_task.duration
    
    task = heapq.heappop(tasks)
    order.append(task.index + 1)
    total_penalty += max(0, current_time - task.preparation)

    with open('output.txt', 'w') as file:
        file.write(f"{n} {total_penalty}\n")
        file.write(' '.join(map(str, order)))

if __name__ == "__main__":
    main()