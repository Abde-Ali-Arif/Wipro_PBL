def sort_colors(colors):
    # Split the string into a list using the hyphen as a delimiter
    color_list = colors.split('-')
    
    # Sort the list alphabetically
    color_list.sort()
    
    # Join the sorted list back into a string with hyphens
    return "-".join(color_list)

# Testing with Sample Input 1
input = input("Enter colors in hyphen separated form: ")
print(f"Sorted colors : {sort_colors(input)}")