def solution(N):
    # write your code in Python 3.6
    binary_N = bin(N)[2:]
    max_num = 0
    count = 0
    for i in binary_N:
        if i == "1":
            if count > max_num:
                max_num = count
            count = 0
        else:
            count += 1
    return max_num

if __name__ == '__main__':
    print(solution(1041))
    print(solution(15))
    print(solution(32))