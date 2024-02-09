def removeDuplicate(input_string):

    unique_chars = set(input_string)

    unique_string = "".join(unique_chars)

    print("Without Order:", unique_string)

    result_string = ""

    for char in input_string:

        if char not in result_string:

            result_string += char

        print("With Order:", result_string)


input_str = "mdmahfujurrahman"

removeDuplicate(input_str)

