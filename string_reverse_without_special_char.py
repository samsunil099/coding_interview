'''
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that 
special characters are not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.  
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
'''

string = input("Input string: ")
text=list(string)
index=0
for i in range(len(text)-1,int(len(text)/2),-1):
    if text[i].isalpha():
        temp=text[i]
        while True:
            if text[index].isalpha():
                text[i]=text[index]
                text[index]=temp
                break
            else:
                index+=1
                break
    """ if text[i].isalpha()==False:
        continue
    elif text[index].isalpha()==False:
        index+=1
    else:
        temp=text[i]
        text[i]=text[index]
        text[index]=temp """

print("Output :","".join(text))
        