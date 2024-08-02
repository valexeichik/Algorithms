import mmap

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def get_first_min(self):
        if not self.head:
            return None
        return self.head.value
    
    def get_second_min(self):
        if not self.head or not self.head.next:
            return None
        return self.head.next.value
    
    def __len__(self):
        return self.size

def encode(frequencies):
    extra_queue = Queue()
    total = 0

    while len(frequencies) > 1:
        a1, a2 = frequencies.get_first_min(), frequencies.get_second_min()
        if len(extra_queue) > 1:
            b1, b2 = extra_queue.get_first_min(), extra_queue.get_second_min()
            if a2 <= b1 and a1 + a2 <= b1 + b2:
                frequencies.pop()
                frequencies.pop()
                extra_queue.append(a1 + a2)
                total += (a1 + a2)
            elif b1 <= a2 and a1 <= b2:
                frequencies.pop()
                extra_queue.pop()
                extra_queue.append(a1 + b1)
                total += (a1 + b1)
            else:
                extra_queue.pop()
                extra_queue.pop()
                extra_queue.append(b1 + b2)
                total += (b1 + b2)
        elif len(extra_queue) == 1:
            b1 = extra_queue.get_first_min()
            if a2 <= b1:
                frequencies.pop()
                frequencies.pop()
                extra_queue.append(a1 + a2)
                total += (a1 + a2)
            else:
                frequencies.pop()
                extra_queue.pop()
                extra_queue.append(a1 + b1)
                total += (a1 + b1)
        else:
            frequencies.pop()
            frequencies.pop()
            extra_queue.append(a1 + a2)
            total += (a1 + a2)

    while len(frequencies) > 0:
        a1 = frequencies.get_first_min()
        if len(extra_queue) == 1:
            b1 = extra_queue.pop()
            a1 = frequencies.pop()
            extra_queue.append(a1 + b1)
            total += (a1 + b1)
        else:
            b1, b2 = extra_queue.get_first_min(), extra_queue.get_second_min()
            if a1 <= b2:
                frequencies.pop()
                extra_queue.pop()
                extra_queue.append(a1 + b1)
                total += (a1 + b1)
            else:
                extra_queue.pop()
                extra_queue.pop()
                extra_queue.append(b1 + b2)
                total += (b1 + b2)

    while len(extra_queue) > 1:
        b1, b2 = extra_queue.pop(), extra_queue.pop()
        extra_queue.append(b1 + b2)
        total += (b1 + b2)

    return total

def main():
    with open('huffman.in', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())
            frequencies = Queue()
            for item in mfile.read().split():
                frequencies.append(int(item))

    sum = encode(frequencies)

    with open('huffman.out', 'w') as file:
        file.write(str(sum))

if __name__ == "__main__":
    main()