from collections import defaultdict

def recursive_deletion(current_index, max_index, count, current_sum, sequence, values_count, K):
    if count == K:
        values_count[current_sum] -= 1
        if values_count[current_sum] == 0:
            del values_count[current_sum]
    else:
        recursive_deletion(current_index, max_index, count + 1, current_sum + sequence[current_index], sequence, values_count, K)
        if current_index < max_index:
            recursive_deletion(current_index + 1, max_index, count, current_sum, sequence, values_count, K)

def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        input_sequence = sorted(map(int, input().strip().split()))
        values_count = defaultdict(int)
        for x in input_sequence:
            values_count[x] += 1
        sequence = [input_sequence[0] // K] + [0] * (N - 1)
        values_count[input_sequence[0]] -= 1
        if values_count[input_sequence[0]] == 0:
            del values_count[input_sequence[0]]
        for n in range(1, N):
            sequence[n] = next(iter(values_count.keys())) - (K - 1) * sequence[0]
            if n < N - 1:
                recursive_deletion(0, n, 1, sequence[n], sequence, values_count, K)
        print(' '.join(map(str, sequence)))

if __name__ == '__main__':
    solve()