f = open("files.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("files.txt") as f:
    print(f.read())
