import ipdb
#!/usr/bin/env python3

def return_evens(num_list):
    # if the number in the list can be divided by 2 and have a remainder of 0 its an even number.
    # should i use range to set a number the list should go up to range(1,11)?  or is it any number that might be entered?
    # maybe i should do a if statement?
    # print(num_list) the range of this is range(1,10,2)
    # ipdb.set_trace()
    even_numbers=[ n for n in num_list if (n%2==0)]
    return even_numbers
return_evens(range(10))

def make_exclamation(sentence_list):
    # print(sentence_list)
    # for each string in the list .append "!" to the end 

    # maybe i should do a .split to spearate all the charaters in each string
    #  then .join once ive added the "!" to get them back together? is that option even a thing in python?
    exclamation_mark=[string+"!" for string in sentence_list]
    return exclamation_mark