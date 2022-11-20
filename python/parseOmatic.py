def weightLoss(wr_content):

    # convert string to lower case
    string = wr_content["body"]
    string = string.lower()

    # get all the most common words from file
    with open('./content/most_common_words.txt', 'r') as f:
        unformated_words = f.readlines()
        common_words = []
        for word in unformated_words:
            word = word[:-1]
            word = word.lower()
            common_words.append(word)

    # remove lame-o characters
    string = string.replace('.', '')
    string = string.replace('\n', '')
    string = string.replace(',', '')
    string = string.replace('?', '')
    string = string.replace('!', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('"', '')

    # split into list of words
    string = string.split(' ')

    # remove the 500 most common words
    skinny_string = []
    for word in string:
        if word not in common_words:
            skinny_string.append(word)

    # make new list without duplicates
    no_dupes = list(dict.fromkeys(skinny_string))

    # get count for each word
    the_count = {}
    for word in no_dupes:
        amount = skinny_string.count(word)
        the_count[word] = amount

    # print all words with more than n occurances
    exclusive_words = []
    for word in the_count:
        if the_count[word] >= 3:
            exclusive_words.append(word)
            #print(word + ", " + str(the_count[word]))

    for word in exclusive_words:

        matched_indexes = []
        i = 0
        length = len(string)

        while i < length:
            if word == string[i]:
                #matched_indexes.append(i)
                try:
                    matched_indexes.append(string[i-1] + " " + string[i] + " " + string[i+1])
                except:
                    pass
            i += 1

        print(matched_indexes)