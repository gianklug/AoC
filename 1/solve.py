#!/usr/bin/python3
#print(sum([int(x[0]+x[-1]) for x in [__import__("re").sub(r"[^123456789]", "", n) for n in open("input", "r").readlines()] ]))
print(
    sum(
        [
            int(x[0] + x[-1])
            for x in [
                __import__("re").sub(r"[^123456789]", "", n)
                for n in open("input", "r").readlines()
            ]
        ]
    )
)

lines = []
for line in open("input", "r").readlines():
    for k,v in {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}.items():
        line = line.replace(k, f"{k[0]}{v}{k[-1]}")
    lines.append(line)


print(
    sum(
        [
            int(x[0] + x[-1])
            for x in [
                __import__("re").sub(r"[^123456789]", "", n)
                for n in lines
            ]
        ]
    )
)
