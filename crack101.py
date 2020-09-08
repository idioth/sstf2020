key1 = "u7fl(3JC=UkJGEhPk{q`/X5UzTI.t&A]2[rPM9"
cmp_key = "Dtd>=mhpNCqz?N!j(Z?B644[.$~96b6zjS*2t&"
result1 = ""

revkey = key1[::-1]
for i in range(len(key1)):
    result1 += chr(ord(cmp_key[i]) ^ ord(revkey[i]))

print(result1[::-1])

