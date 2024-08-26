def encode(strs: list[str]) -> str:
    delim = "$"
    return "".join([str(len(s)) + delim + s for s in strs])


def decode(s: str) -> list[str]:
    l = []
    delim = "$"
    number_started = False
    i = 0
    
    while i < len(s):
        c = s[i]
        if c in "0123456789" and not number_started:
            number_started = True
            num = c
        elif c in "0123456789" and number_started:
            num += c
        elif c == delim and number_started:
            number_started = False
            num = int(num)
            l.append(s[i+1:i+1+num])
            i += num
        i += 1
    return l

slist = ["we","say",":","yes","!@#$%^&*()"]
e = encode(slist)
d = decode(e)
print(e)
print(d)
print (slist == decode(encode(slist)))
