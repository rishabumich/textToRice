def main(input):
    for i in input:
        if i == '0':
            print("🍚", end='')
        else:
            print("🍙", end='')
    print("")

if __name__ == "__main__":
    main("01101000 01100101 01101100 01101100 01101111 00100000 01110011 01100001 01101110 01111001 01100001")