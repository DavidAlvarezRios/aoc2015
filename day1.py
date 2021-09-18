# ( += 1 y ) -=1

test1 = "(())" # result: 0
test2 = "(()(()(" # result: 3
test3 = "))(((((" # result: 3
test4 = "())" # result: -1
test5 = ")())())" #result: -3
test6 = ")" # result: 1
test7 = "()())" # result: 5

def get_input(file_name: str) -> str:
    
    f = open(file_name, 'r')
    ret = f.read()
    f.close()

    return ret


def compute_floor_part1(seq: str) -> int:
    count = 0

    for el in seq:
        if el == '(':
            count += 1
        else:
            count -= 1

    return count

def compute_pos_basement_part2(seq: str) -> int:
    count = 0
    pos = 1

    for el in seq:
        if el == '(':
            count += 1
        else:
            count -= 1

        if count == -1:
            return pos
        pos += 1

    return -1

    

if __name__ == '__main__':
    # assert part 1
    assert compute_floor_part1(test1) == 0
    assert compute_floor_part1(test2) == 3
    assert compute_floor_part1(test3) == 3
    assert compute_floor_part1(test4) == -1
    assert compute_floor_part1(test5) == -3
    # assert part 2
    assert compute_pos_basement_part2(test6) == 1
    assert compute_pos_basement_part2(test7) == 5

    seq = get_input('input.txt')

    print("Result part 1: floor %d"% compute_floor_part1(seq))
    print("Result part 2: floor %d"% compute_pos_basement_part2(seq))


