def rev_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)

s = str(input())
onc = rev_words(s)

print(onc)