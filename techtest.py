#importing pyenchant as spellchecking library/source of truth for english (GB) dictionary  
import enchant
d = enchant.Dict("en_GB")
# input your longstring
sentense = input('please enter your string:')

def word_scan(text):
    words=[]
    # scan over slices of input text for words
    # sub_range is the selected range/lengths of input text where it will be checked against the dict
    for sub_range in range(len(text), 1, -1):
        # the sub_text is the start index of the range, and the (sub_range+sub_text) is the last index of the range
        for sub_text in range(0,len(text)-sub_range+1, 1):
            word = text[sub_text:sub_range+sub_text]
            # debug: print(f"sub_range: {sub_range} subtext: {sub_text} parsed_word: {word}")
            # compare against the dict and append all words found in the english (GB) dictionary into a list. 
            if d.check(word):
                words.append(word)
# The result should return false if the string cannot be segmented
    if len(words) == 0:
        return False
    return words

print(word_scan(sentense))

# explain about the complexity of the devised solution.
# The solution takes a spellchecking library(pyenchant==3.2.0) as the source of truth for english (GB) dictionary.
# The solution creates a window of certain lengths of character on the string using a for-in loop, and subsequently slices the words within the range
# the segmented  word will be compare against the source of truth and will add to the list of words if they are found within the dictionary
# Thereafter the window will move forward to the next position of the string that satisfied the range, the process will be repeated and word will be appended to the list if it is found in the dictionary 
# The process repeated until the range is equal to 1 charater and the string has been loop through completely.
#The result should return false if the string cannot be segmented into a dictionary word.
# have fun play around it :)



# 
# 
#  Function to segment given string into a space-separated
# sequence of one or more dictionary words
# input required string
# def wordFormation(sentense, out=""):

#     # if the end of the string is reached,
#     # print the output string
#     if not sentense:
#         print('result:'+out)

#     for i in range(1, len(sentense) + 1):
#         # consider all prefixes of the current string
#         prefix = sentense[:i]

#         # if the prefix is present in the dictionary, add it to the
#         # output string and recur for the remaining string
#         if d.check(prefix) and len(prefix)>1:
#             wordFormation(sentense[i:], out + " " + prefix)
# # Implementation in Python
# if __name__ == '__main__':
#     wordFormation(sentense)

