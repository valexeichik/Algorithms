import mmap
import heapq

class Task:
    def __init__(self):
        self.deadline = -1
        self.duration = -1
        self.index = -1
        self.next_tasks = set()
        self.prev_tasks = []

    def __lt__(self, other):
        return self.deadline < other.deadline
    
    def __str__(self):
        return f"{self.index} {self.duration} {self.deadline}"

with open('input.txt', 'r') as file:
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
        n = int(mfile.readline())
        tasks = []

        total_time = 0

        for i in range(n):
            duration, deadline = map(int, mfile.readline().split()) 
            task = Task()
            task.index, task.duration, task.deadline = i, duration, -deadline
            total_time += duration
            tasks.append(task)

        m = int(mfile.readline())
        for i in range(m):
            vertex1, vertex2 = map(int, mfile.readline().split())
            tasks[vertex1 - 1].next_tasks.add(vertex2 - 1)
            tasks[vertex2 - 1].prev_tasks.append(vertex1 - 1)

        sequence = []
        for task in tasks:
            if len(task.next_tasks) == 0:
                heapq.heappush(sequence, task)

        index = -1
        penalty = -1
        stack = []
        while len(sequence) > 0:
            current_task = heapq.heappop(sequence)
            current_index = current_task.index
            stack.append(current_index + 1)

            for i in current_task.prev_tasks:
                tasks[i].next_tasks.discard(current_index)
                if len(tasks[i].next_tasks) == 0:
                    heapq.heappush(sequence, tasks[i])

            current_penalty = max(0, total_time + current_task.deadline)
            if current_penalty > penalty:
                penalty = current_penalty
                index = current_index + 1
            
            total_time -= current_task.duration

with open('output.txt', 'w') as file:
    file.write(f"{index} {penalty}\n")
    file.write('\n'.join(map(str, reversed(stack))))