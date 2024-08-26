def encode(strs: list[str]) -> str:
    new_str = ""
    for s in strs:
        new_str += "[" + s + "]"
    return new_str


def decode(s: str) -> list[str]:
    l = []
    count = 0
    for i, c in enumerate(s):
        if c == "[":
            if count == 0:
                start = i + 1
            count += 1
        elif c == "]":
            if count == 1:
                end = i
                l.append(s[start:end])
            count -= 1
    return l

# This only works if the brackets are balanced.