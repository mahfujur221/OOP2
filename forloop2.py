def removeEmptyElements(input_list):

    new_list = []

    for element in input_list:

        if element:

            new_list.append(element)

    return new_list

input_list = [5, 6, [], 3, [], [], 9, 11, []]

print(f"The original list is: {input_list}")

print(f"List after removing empty elements: {removeEmptyElements(input_list)}")

