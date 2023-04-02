def next_permutation(a):
    n = len(a)
    i = 0
    j = 0
    for i in range(n-2, -1, -1):
        if (a[i] < a[i + 1]):
            break
    if (i < 0) : 
        a.reverse()
    else:
        for j in range(n-1, i, -1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]

        st, end = i + 1, len(a)

        a[st:end] = a[st:end][::-1]

def prnt_nxt_prmttn(a):
    a = sorted(a)
    b = sorted(a, reverse=True)

    while a != b:
        print(''.join(a))
        next_permutation(a)
    print(''.join(a))
