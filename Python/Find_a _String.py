# print the number of times that the substring occurs in the given string
def count_substring(string, sub_string):
    count=0;
    sub_length=len(sub_string)-1
    for i in range(0,(len(string)-sub_length)):
        t=sub_length+i+1
        s=string[i:t]
        if s ==sub_string:
            count=count+1
        
    return count

