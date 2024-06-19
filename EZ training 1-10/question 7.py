def min_key_presses(s):
    count = 0
    i = 0
    while i < len(s):
        if s[i] == '0' and s[i + 1] == '0':
            count += 1  
            i += 2  
        else:
            count += 1  
            i += 1
    return count


s = input()
print(min_key_presses(s))
