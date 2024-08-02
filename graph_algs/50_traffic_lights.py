import mmap
import heapq

class Light:
    def __init__(self, color, wait, B_time, P_time):
        self.color = color
        self.wait = wait
        self.B_time = B_time
        self.P_time = P_time

    def click(self):
        if self.color == b'B':
            self.color = b'P'
            self.wait = self.P_time
        else:
            self.color = b'B'
            self.wait = self.B_time

    def change_color(self, time):
        while self.wait <= time:
            time -= self.wait
            self.click()
        self.wait -= time

    def copy(self):
        return Light(self.color, self.wait, self.B_time, self.P_time)

    @staticmethod
    def count_time(light1, light2, time, dist):
        light_1 = light1.copy()
        light_2 = light2.copy()

        light_1.change_color(time)
        light_2.change_color(time)

        total_time = 0
        
        if light_1.color != light_2.color:
            if light_1.wait == light_2.wait:
                total_time += light_1.wait
                light_1.click()
                light_2.click()
            total_time += min(light_1.wait, light_2.wait)

        # while light_1.color != light_2.color:
        #     if light_1.wait < light_2.wait:
        #         total_time += light_1.wait
        #         light_2.wait -= light_1.wait
        #         light_1.click()
        #     elif light_1.wait > light_2.wait:
        #         total_time += light_2.wait
        #         light_1.wait -= light_2.wait
        #         light_2.click()
        #     else:
        #         total_time += light_1.wait
        #         light_1.click()
        #         light_2.click()

        return total_time + dist

def find_route_and_time(roads, lights, n, start, end):
    times = [float('inf')] * n
    processed = [False] * n
    parent = [-1] * n

    queue = [(0, start)] 

    while queue and not processed[end]:
        time, current_light= heapq.heappop(queue)
        if processed[current_light]:
            continue

        processed[current_light] = True
        for light, dist in roads[current_light]:
            t = Light.count_time(lights[light], lights[current_light], time, dist)
            if not processed[light] and times[light] > t + time:
                times[light] = t + time
                parent[light] = current_light
                heapq.heappush(queue, (t + time, light))

    route = []
    item = end
    while item != -1:
        route.append(item + 1)
        item = parent[item]

    return times[end], route

def main():
    with open('lights.inp', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            start, end = (int(item) - 1 for item in mfile.readline().split())
            n, m = map(int, mfile.readline().split())

            lights = [None for _ in range(n)]
            for i in range(n):
                data = mfile.readline().split()
                lights[i] = Light(data[0], int(data[1]), int(data[2]), int(data[3]))

            roads = [[] for _ in range(n)]
            for i in range(m):
                u, v, w = map(int, mfile.readline().split())
                roads[u - 1].append((v - 1, w))
                roads[v - 1].append((u - 1, w))

    time, route = find_route_and_time(roads, lights, n, start, end)

    with open('lights.out', 'w') as file:
        file.write(str(time) + '\n' + ' '.join(map(str, reversed(route))))

if __name__ == "__main__":
    main()