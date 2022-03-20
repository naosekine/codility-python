def solution(A, K):
    temp_arr = [0] * len(A)
    
    for idx in range(len(A)) :
        new_idx = (idx + K) % len(A)
        temp_arr[new_idx] = A[idx]
    
    return temp_arr

if __name__ == '__main__':
    print(solution([3, 8, 9, 7, 6], 3))
    print(solution([0, 0, 0], 1))
    print(solution([1, 2, 3, 4], 4))