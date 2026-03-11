import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # N=3: check pairs 0,2 then 2,0 then 2,2
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'0\s*,\s*2', r'2\s*,\s*0', r'2\s*,\s*2'], lines)


@pytest.mark.T2
def test_main_2():
    # N=10: check pairs 0,9 then 9,0 then 9,9
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'0\s*,\s*9', r'9\s*,\s*0', r'9\s*,\s*9'], lines)


@pytest.mark.T3
def test_main_3():
    # N=1: only one pair 0,0
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    assert len(lines) == 1, f'Expected 1 line, got {len(lines)}'
    regex_test([r'0\s*,\s*0'], lines)


@pytest.mark.T4
def test_main_4():
    # N=4: check pairs 0,3 then 3,0 then 3,3
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'0\s*,\s*3', r'3\s*,\s*0', r'3\s*,\s*3'], lines)
