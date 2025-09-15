


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is persent in content. line no {lineno}")
        break
    lineno += 1

else:
    print("No python is not persent in content")     
