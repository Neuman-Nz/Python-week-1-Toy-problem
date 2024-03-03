def alphabet_string(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = ''
    
#Calculation of the number of times each letter are going to be repeated
    repeat_count = N // 26
    remainder = N % 26
    
#Generation of the string with repeated letters
    for i in range(26):
        if i < remainder:
            string += alphabet[i] * (repeat_count + 1)
        else:
            string += alphabet[i] * repeat_count
    
    return string

print(alphabet_string(30))