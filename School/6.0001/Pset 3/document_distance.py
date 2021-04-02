# 6.0001 Spring 2020
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands, tammam, mjulian

# Problem Set 3
# Name: Dylan Walker
# Collaborators: None
# Time Spent: 3:30

import string

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other


### Problem 1: Prep Data ###
# Make a *small* change to separate the data by ALL whitespace
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        list of strings holding the file contents where
            each string was separated by whitespace (\t, \n, or space) in the file
    """
    in_file = open(filename, 'r')
    line = in_file.read()
    in_file.close()
    # remove leading and trailing white space, make lowercase
    line = line.strip().lower()
    # remove punctuation
    for char in string.punctuation:
        line = line.replace(char, "")
    # split the string at all whitespace
    return line.split()  # TODO your code here

### Problem 2: Find Bigrams ###
def find_bigrams(words):
    """
    Args:
        words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters.
    Returns:
        list of bigrams from input text list. If there are fewer than 2 words, returns an empty list.
    """
    # setting up return list
    bigram_list = []
    # adds the word at index wordcount from words as well as the word in front of it to the bigram_list
    for wordcount in range(len(words) - 1):
        bigram_list.append(str(words[wordcount] + " " + words[wordcount + 1]))
    return bigram_list

### Problem 3: Word Frequency ###
def compute_frequencies(words):
    """
    Args:
        words: list of words (or bigrams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word (or bigram) in words and the corresponding int
        is the frequency of the word (or bigram) in words
    """
    # setting up return dictionary
    freqdict = {}
    # detecting if the word is already in freqdict, and if it isn't then adding the word and setting the value(frequency) equal to 1
    for freq1 in range(len(words)):
        if words[freq1] not in freqdict.keys():
            freqdict[words[freq1]] = 1
    # making list of keys for reference in for loop
    freq_keys = list(freqdict.keys())
    # setting the values(frequencies) in freqdict equal to the frequency in the list of words
    for freq2 in range(len(freqdict)):
        freqdict[freq_keys[freq2]] = words.count(freq_keys[freq2])
    return freqdict

### Problem 4: Similarity ###
def get_similarity_score(freq_dict1, freq_dict2, use_difference=False):
    """
    The keys of freq_dict1 and freq_dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of words or bigrams for one text
        freq_dict2: frequency dictionary of words or bigrams for another text
        use_difference: Boolean, optional parameter. Defaults to False.
          If this is True, return how different the texts are, 100*(DIFF/ALL), instead.
    Returns:
        int, a percentage between 0 and 100, inclusive
        representing how similar the texts are to each other

        The difference in text frequencies = DIFF is the sum of the values
        from these three scenarios:
        * If a word or bigram occurs in freq_dict1 and freq_dict2 then
          get the difference in frequencies
        * If a word or bigram occurs only in freq_dict1 then take the
          frequency from freq_dict1
        * If a word or bigram occurs only in freq_dict2 then take the
          frequency from freq_dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both freq_dict1 and freq_dict2.
        Returns 100*(1-(DIFF/ALL)) rounded to the nearest whole number if use_difference
          is False, otherwise returns 100*(DIFF/ALL)
    """
    diff = 0
    all = 0
    # making list of both dict's keys
    dict1_keys = list(freq_dict1.keys())
    dict2_keys = list(freq_dict2.keys())
    # detecting the common words in both dicts and taking the absolute value of their differences and adding it to diff, and if the word/bigram is not in both then adding the frequency
    # also adding the frequencies of dict1 to all
    for all1 in range(len(dict1_keys)):
        all += freq_dict1[dict1_keys[all1]]
        if dict1_keys[all1] in dict2_keys:
            diff += abs(freq_dict1[dict1_keys[all1]] - freq_dict2[dict2_keys[dict2_keys.index(dict1_keys[all1])]])
        else:
            diff += freq_dict1[dict1_keys[all1]]
    # detecting if it's not a common word and then adding it to diff and adding dict2's frequencies to all
    for all2 in range(len(dict2_keys)):
        all += freq_dict2[dict2_keys[all2]]
        if dict2_keys[all2] not in dict1_keys:
            diff += freq_dict2[dict2_keys[all2]]
    # using the different equations provided depending on if use_difference is True or False
    if use_difference == False:
        return round(((100 * (1-(diff / all)))))
    else:
        return round((100 * (diff / all)))

### Problem 5: Most Frequent Word(s) ###
def compute_most_frequent(freq_dict1, freq_dict2):
    """
    The keys of freq_dict1 and freq_dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) (or bigram(s)) in the input dictionaries

    The most frequent word:
        * Is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum of the
          freqencies as the combined word frequency.
        * Need not be in both dictionaries, i.e it can be exclusively in
          freq_dict1, freq_dict2, or shared by freq_dict1 and freq_dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered (a to z) list of all these words.
    """
    # getting the key lists of dict1 and dict2
    freq_dict1_keys = list(freq_dict1.keys())
    freq_dict2_keys = list(freq_dict2.keys())
    # setting up the return list
    highest_value_list = []
    # seeing if there are commonalities between the two lists and if they are then adding that value to dict1
    for val in range(len(freq_dict1)):
        if freq_dict1_keys[val] in freq_dict2_keys:
            freq_dict1[freq_dict1_keys[val]] += freq_dict2[freq_dict1_keys[val]]
    # sorting the dictionaries and getting lists of their keys to refer to later
    sorted_freq_dict1 = dict(sorted(freq_dict1.items(), key=lambda item: item[1]))
    sorted_freq_dict2 = dict(sorted(freq_dict2.items(), key=lambda item: item[1]))
    sorted_freq_dict1_keys = list(sorted_freq_dict1.keys())
    sorted_freq_dict2_keys = list(sorted_freq_dict2.keys())
    # setting variable to see if the combined variables/sorted last value of the index of dict 1 is greater than the last index of the sorted list of dict 2
    yesno = 0
    # setting abstraction variables for the last indexes of each dictionary
    dict1_last_index = sorted_freq_dict1_keys[len(sorted_freq_dict1_keys) - 1]
    dict2_last_index = sorted_freq_dict2_keys[len(sorted_freq_dict2_keys) - 1]
    # seeing if the value of the last index of the sorted dict1 is greater than the index of the sorted dict2 and if they are then on the last iteration of the for loop returning the list
    for i in range(len(sorted_freq_dict1) - 1):
        if sorted_freq_dict1[sorted_freq_dict1_keys[i]] == sorted_freq_dict1[dict1_last_index] and sorted_freq_dict1[dict1_last_index] > sorted_freq_dict2[dict2_last_index]:
            highest_value_list.append(sorted_freq_dict1_keys[i])
            yesno = 1
        elif i == len(sorted_freq_dict1) and yesno == 1:
            return sorted(highest_value_list)
    # seeing if the value of the last index of the sorted dicts and if they are then appending both values as they are the highest
    if sorted_freq_dict1[dict1_last_index] == sorted_freq_dict2[dict2_last_index]:
        highest_value_list.append(dict1_last_index)
        highest_value_list.append(dict2_last_index)
    # if the value of the last sorted index of dict1 is bigger than the last sorted index of dict 2 then adding the last sorted index of dict1 to the list
    elif sorted_freq_dict1[dict1_last_index] > sorted_freq_dict2[dict2_last_index]:
        highest_value_list.append(dict1_last_index)
    # the only remaining case is that the value of the last sorted index of dict2 is greater than that of dict1, so then that value is appended to the highest value list
    else:
        highest_value_list.append(dict2_last_index)
    # return the highest value(s)
    return sorted(highest_value_list)

### Problem 6: Finding closest artist ###
def find_closest_artist(artist_to_songfiles, mystery_lyrics, use_bigrams=False):
    """
    Args:
        artist_to_songfiles:
            dictionary that maps string:list of strings
            where each string key is an artist name
            and the corresponding list is a list of filenames (including the extension),
            each holding lyrics to a song by that artist
        mystery_lyrics: list of single word strings
            Can be more than one or two words (can also be an empty list)
            assume each string is made of lowercase characters
        use_bigrams: Boolean, optional parameter. Default set to False.
            If it is True, bigrams of text in files
            and bigrams of mystery_lyrics should be used in analysis instead
            of single words
    Returns:
        list of artists (in alphabetical order) that best match the mystery lyrics
        (i.e. list of artists that share the highest average similarity score (rounded to the nearest integer))

    The best match is defined as the artist(s) whose songs have the highest average
    similarity score (after rounding) with the mystery lyrics
    If there is only one such artist, then this function should return a singleton list
    containing only that artist.
    However, if all artists have an average similarity score of zero with respect to the
    mystery_lyrics, then this function should return an empty list. When no artists
    are included in the artist_to_songfiles, this function returns an empty list.
    """
    # setting up the result list, the dictionary of artists' names as keys and their mean score as the values, and a dummy dictionary to use as freq_dict2 for compute_most_frequent
    result_artist_list = []
    mean_artist_dict = {}
    dummy_dict = {"z" : 0}
    # detecting if the length of either artist_to_songfiles or mystery_lyrics is 0 and returning an empty list
    if len(artist_to_songfiles) == 0 or len(mystery_lyrics) == 0:
        return result_artist_list
    # getting a list of the keys(artists) of the dictionary of artists and their songs
    artist_to_songfiles_keys = list(artist_to_songfiles.keys())
    # finds mean similarity score for each artist
    for artist_count in range(len(artist_to_songfiles)):
        artist_similarity_list = []
        # for each song for an artist gets similarity score and is added to the artists' similarity list which is used to calculate the mean for each artist at the end
        for song_count in range(len(artist_to_songfiles[artist_to_songfiles_keys[artist_count]])):
            song_list = list(artist_to_songfiles[artist_to_songfiles_keys[artist_count]])
            song_loaded = load_file(song_list[song_count])
            # if using bigrams, finding them for the song and the mystery lyrics and either way, appending their similarity score to the artists' similarity list
            if use_bigrams:
                bigrams = find_bigrams(song_loaded)
                bigrams1 = find_bigrams(mystery_lyrics)
                song_frequency = compute_frequencies(bigrams)
                mystery_frequency = compute_frequencies(bigrams1)
                sim_score = get_similarity_score(song_frequency, mystery_frequency)
                artist_similarity_list.append(sim_score)
            else:
                song_frequency = compute_frequencies(song_loaded)
                mystery_frequency = compute_frequencies(mystery_lyrics)
                sim_score = get_similarity_score(song_frequency, mystery_frequency)
                artist_similarity_list.append(sim_score)
        # getting mean sim score for each artist and appending to greater dict of artists' means and their names 
        mean_artist_dict[artist_to_songfiles_keys[artist_count]] = int(round(((sum(artist_similarity_list))) / len(artist_similarity_list)))
    # seeing if all of the values of the dictionary are 0, and if any of them aren't then using the compute_most_frequent function to get a list of the most similar artist(s)
    for zerocount in range(len(mean_artist_dict)):
        if list(mean_artist_dict.values())[zerocount] > 0:
            return compute_most_frequent(mean_artist_dict, dummy_dict)
    # if all of the values are equal to 0, then returns an empty list
    return []

if __name__ == "__main__":
    pass
    # # Uncomment the following lines to test your implementation
    # # Tests Problem A: Prep Data
    test_directory = "tests/student_tests/"
    world, friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #print(world) ## should print ['hello', 'world', 'hello']
    #print(friend) ## should print ['hello', 'friends']
    #
    # # Tests Problem B: Find Bigrams
    world_bigrams, friend_bigrams = find_bigrams(world), find_bigrams(friend)
    #print(world_bigrams) ## should print ['hello world', 'world hello']
    #print(friend_bigrams) ## should print ['hello friends']
    #
    # # Tests Problem C: Get frequency
    world_word_freq, world_bigram_freq = compute_frequencies(world), compute_frequencies(world_bigrams)
    friend_word_freq, friend_bigram_freq = compute_frequencies(friend), compute_frequencies(friend_bigrams)
    #print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    #print(world_bigram_freq) ## should print {'hello world': 1, 'world hello': 1}
    #print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    #print(friend_bigram_freq) ## should print {'hello friends': 1}
    #
    # # Tests Problem D: Similarity
    word_similarity = get_similarity_score(world_word_freq, friend_word_freq)
    bigram_similarity = get_similarity_score(world_bigram_freq, friend_bigram_freq)
    #print(word_similarity) ## should print 40
    #print(bigram_similarity) ## should print 0
    #
    # # Tests Problem E: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = compute_most_frequent(freq1, freq2)
    #print(most_frequent) ## should print ["hello", "world"]
    #
    # # Tests Problem F: Find closest matching artist
    test_directory = "tests/student_tests/"
    artist_to_songfiles_map = {
    "artist_1": [test_directory + "artist_1/song_1.txt", test_directory + "artist_1/song_2.txt", test_directory + "artist_1/song_3.txt"],
    "artist_2": [test_directory + "artist_2/song_1.txt", test_directory + "artist_2/song_2.txt", test_directory + "artist_2/song_3.txt"],
    }
    mystery_lyrics = load_file(test_directory + "mystery_lyrics/mystery_1.txt") # change which number mystery lyrics (1-5)
    #print(find_closest_artist(artist_to_songfiles_map, mystery_lyrics)) # should print ['artist_1']
