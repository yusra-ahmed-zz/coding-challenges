
def get_unique_nums(n):

#    my_nums = [1,2,3,4,5,6,7,8,9,10]
#    unique_nums = []
#    count = 0
#
#    while count < n:
#        rand_num = random.choice(my_nums)
#        if rand_num not in unique_nums:
#            unique_nums.append(rand_num)
#            count = count + 1
#
#    return unique_nums

    nums = range(1, 11)
    lucky_nums = []
    
    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)
    
    return lucky_nums

def string_splitter(string, splitter):

    answer = []
    split_section = ""

    for letter in string:
        if letter == splitter:
            answer.append(split_section)
            split_section = ""

        else:
            split_section = split_section + letter

    answer.append(split_section)

return answer

def reverlist(l1):

    for i in range (len(l1)/2):
        temp = l1[i]
        l1[i] = l1[-i-1]
        l1[-1-1] = temp


def word_lengths(sentence_str):

    new_dict = {}
    new_sentence = sentence_str.split(" ")
    for word in new_sentence:
        word_length = len(word)
        if word_length not in new_dict:
            new_dict[word_length] = [word]
        else:
            new_dict[word_length].append(word)
    return new_dict









