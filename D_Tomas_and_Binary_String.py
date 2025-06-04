t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    val_s = int(s, 2)
    max_xor = -1
    ans_l1, ans_r1, ans_l2, ans_r2 = 1, n, 1, 1
    current_l1 = 1
    current_r1 = n
    for l2 in range(1, n + 1):
        for r2 in range(l2, n + 1):
            sub2_str = s[l2-1:r2]
            val_sub2 = int(sub2_str, 2)
            curr_xor = val_s ^ val_sub2
            if curr_xor > max_xor:
                max_xor = curr_xor
                ans_l1 = current_l1
                ans_r1 = current_r1
                ans_l2 = l2
                ans_r2 = r2
    print(ans_l1, ans_r1, ans_l2, ans_r2)
