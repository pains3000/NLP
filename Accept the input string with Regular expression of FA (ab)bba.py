def FA(s):
    size = 0
    # Scan complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"
    # After checking that it contains only 'a' & 'b', check its length (should be at least 3)
    if size >= 3:
        # Check the last 3 elements
        if s[size - 3] == 'b':
            if s[size - 2] == 'b':
                if s[size - 1] == 'a':
                    return "Accepted"  # If all conditions are met
                else:
                    return "Rejected"  # Else of 4th if
            else:
                return "Rejected"  # Else of 3rd if
        else:
            return "Rejected"  # Else of 2nd if
    else:
        return "Rejected"  # Else of 1st if

# Test inputs
inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']
for i in inputs:
    print(FA(i))
