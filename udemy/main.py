a, b, c = map(int, input().split())
ans = []

if a >= b:
    if a >= c:
        ans.append(a)
        if b >= c:
            ans.append(b)
            ans.append(c)
        else:
            ans.append(c)
            ans.append(b)
    elif c > a:
        ans.append(c)
        if a >= b:
            ans.append(a)
            ans.append(b)
        else:
            ans.append(b)
            ans.append(a)
else:
    if b >= c:
        ans.append(b)
        if a >= c:
            ans.append(a)
            ans.append(c)
        else:
            ans.append(c)
            ans.append(a)
    else:
        ans.append(c)
        if a >= b:
            ans.append(a)
            ans.append(b)
        else:
            ans.append(b)
            ans.append(a)

print("".join(map(str, ans)))
