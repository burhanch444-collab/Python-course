def main():
    try:
        n = int(input("Hi, Enter a number: "))
        print(n)
        return

    except Exception as e:
        print(e)
        return
    finally:
        print("Thank you")

main()        