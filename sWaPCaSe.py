#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#Code

def swap_case(s):
    res=''
    for i in s:
        if i.islower():
            res+=i.upper()
        else:
            res+=i.lower()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
