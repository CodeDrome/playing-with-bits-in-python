
def main():

    print("---------------------------------")
    print("| codedrome.com                 |")
    print("---------------------------------")
    print("| Playing With Bits in Python   |")
    print("| Part 1: Representing Integers |")
    print("---------------------------------\n")

    iterate_8_bit_ints()


def iterate_8_bit_ints():

    heading = "Decimal     Python Binary     Actual Binary     Interpretation"

    print(heading)
    print("-" * len(heading))

    for i in range(-128, 129, 8):

        # botch to iterate to 127
        if i == 128:
            i = 127

        bin_string = as_binary(i)

        print(f"{i:>7}", end="")
        print(f"{i:>18b}", end="")
        print(f"{bin_string:>18}", end="")
        print(f"{interpret_binary_string(bin_string):>19}")


def as_binary(x):

    # Generates a string of the correct Two's Complement 
    # representation of an 8-bit integer, not the
    # minus sign and positive number shown by Python.

    if(x < 0):
        x = 256 + x

    return("{0:b}".format(x).zfill(8))


def interpret_binary_string(bin_string):

    # Positive numbers have the MSB set to 0
    # and are 0 + the number represented by the other 7 bits.
    # Negative numbers have the MSB set to 1
    # and are -128 + the number represented by the other 7 bits.

    interpretation = ""
    offset = int(bin_string[1:], 2)

    if(bin_string[0] == "1"):
        interpretation += "-128 + "
    else:
        interpretation += "0 + "

    interpretation += str(offset)

    return interpretation


if __name__ == "__main__":

    main()
