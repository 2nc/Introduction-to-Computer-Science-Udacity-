# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    ##
    # Your code here
    str1_letter = "abcdefghijklmnopqrstuvwxyz"
    list_total = []
    freq_list = []
    i = 0
    while i < 26:
        list_total.append(0.0)
        freq_list.append(0.0)
        i = i + 1
    index_message = 0
    while index_message < len(message):
        i = 0
        while i < 26:
            if message[index_message] == str1_letter[i]:
                list_total[i] = list_total[i] + 1
                break
            i = i + 1
        index_message = index_message + 1
    i = 0
    while i < 26:
        freq_list[i] = (list_total[i] + 0.0) / len(message)
        i = i + 1
    ##
    return freq_list



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
