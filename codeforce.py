import sys
input = sys.stdin.read

def max_area_of_ones(s):
    n = len(s)
    doubled_s = s + s
    max_1_seq = 0
    current_seq = 0
    
    for char in doubled_s:
        if char == '1':
            current_seq += 1
            max_1_seq = max(max_1_seq, current_seq)
        else:
            current_seq = 0
    
    if max_1_seq == 0:
        return 0
    if max_1_seq >= n:
        return n * n
    
    return ((max_1_seq + 1) // 2) * n

def main():
    data = input().strip().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        s = data[i]
        results.append(str(max_area_of_ones(s)))
    print("\n".join(results))

