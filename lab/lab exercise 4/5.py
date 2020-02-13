def rev_slicing(s):
    return s[::-1]

input_str = str(input('enter a string to reverse :'))

if __name__ == "__main__":
    print('The reversed String is', rev_slicing(input_str))