import mmap

def is_bst():
    with open('bst.in', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as m:
            n = int(m.readline())
            
            tree = [0] * (n + 1)
            left_borders = [0] * (n + 1)
            right_borders = [0] * (n + 1)
            left_borders[1], right_borders[1] = float('-inf'), float('inf')
            tree[1] = int(m.readline())

            for i in range(2, n + 1):
                value, parent, side = m.readline().decode().split()
                value, parent = int(value), int(parent)

                if side == 'L':
                    left_border, right_border = left_borders[parent], tree[parent] 
                else:
                    right_border, left_border = right_borders[parent], tree[parent]

                if not (left_border <= value < right_border):
                    return False
                
                tree[i], left_borders[i], right_borders[i] = value, left_border, right_border
                
            return True
        
def main():
    with open('bst.out', 'w') as file:
        if is_bst():
            file.write('YES')
        else:
            file.write('NO')

if __name__ == '__main__':
    main()