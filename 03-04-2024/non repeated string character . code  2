def non_repeated_characters(input_string):
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char, count in char_count.items():
        if count == 1:
            print(char, end=' ')
            
input_str = "character"
print("Input:", input_str)
print("Output:")
non_repeated_characters(input_str)
