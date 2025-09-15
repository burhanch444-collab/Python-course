try:
    n = int(input("Hi, Enter a number: "))
    print(n)

except ValueError as v:
    print("Heyyyy")
    print(v)    
except Exception as e:
    print(e)

print("Thank you")