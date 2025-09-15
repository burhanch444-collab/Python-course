with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("python is persent in content")

else:
    print("No python is not persent in content")     
