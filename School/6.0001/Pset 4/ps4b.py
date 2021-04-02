# Problem Set 4B
# Name: Dylan Walker
# Collaborators: None
# Time Spent: 
# Late Days Used: 

import string, random, json

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]

def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            self.message_text (string, determined by input text)
        '''
        self.message_text = input_text


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text



    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by. -95<shift<95

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        # converts char into the ASCII value
        char = ord(char)
        # shifts char's ascii value by the given shift parameter
        # if the value of char is greater than 126, loops around to 31 and adds the remainder
        if char + shift > 126:
            char = 31 + (char + shift - 126)
        # if the value of char is less than 32, loops around to 127 and subtracts the difference
        elif char + shift < 32:
            char = 127 + (char + shift - 32)
        else:
            char = char + shift
        # converts the shifted char back into a character string to return
        char = chr(char)
        return char


    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to self.message_text.
        For each character in self.message_text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt self.message_text
                        len(pad) == len(self.message_text)
                        elements of pad are in the range (-95, 95)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        # converts the message text to a list
        message_text_num  = list(self.message_text)
        # encrypts each index of message_text_num with the index of pad due to the len(pad) == len(self.message_text)
        for shift_list in range(len(message_text_num)):
            message_text_num[shift_list] = self.shift_char(message_text_num[shift_list], pad[shift_list])
        return ''.join(message_text_num) 



class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!=None then len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        A PlaintextMessage object inherits from Message. It has three attributes:
            self.message_text (string, determined by input_text)
            self.pad (list of integers, determined by pad
                or generated from self.generate_pad() if pad==None)
            self.encrypted_message_text (string, input_text encrypted using self.pad)
        '''
        self.message_text = input_text
        if pad == None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad
        self.encrypted_message_text = Message.apply_pad(self, self.pad)


    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt self.message_text.

        The pad should be generated by making a new list and for each character
            in self.message_text chosing a random number in the range [0, 95) and
            adding that number to the list.

        Returns: (list of integers) the new one time pad
        '''
        temp_pad = []
        for pad_len in range(len(self.message_text)):
            temp_pad.append(random.randint(0, 95))
        return temp_pad


    def get_pad(self):
        '''
        Used to safely access self.pad outside of the class

        Returns: a COPY of self.pad
        '''
        self.pad_copy = self.pad.copy()
        return self.pad_copy


    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text


    def change_pad(self, new_pad):
        '''
        Changes self.pad of the PlaintextMessage, and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: nothing
        '''
        self.pad = new_pad
        self.encrypted_message_text = Message.apply_pad(self, self.pad)
        



class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
                            on the given file WORDLIST_FILENAME)
        '''
        self.message_text = input_text
        self.valid_words = load_words("words.txt")


    def decrypt_message(self, pad):
        '''
        Decrypts self.message_text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: the plaintext message
        '''
        # Making the pad used for decrypting 
        decrypt_pad = []
        # Multiplies each index of the pad list by negative 1 to apply the negative pad in order to decrypt the message
        for pad_len in range(len(pad)):
            decrypt_pad.append(pad[pad_len] * -1)
        # Uses the apply_pad method in the Message class with the new pad to decrypt the message and returns it
        decrypt_message = Message.apply_pad(self, decrypt_pad)
        return decrypt_message


    def decrypt_message_try_pads(self, pads):
        '''
        Finds the pad in pads which when used to decrypt self.message_text results
        in a plaintext with the most valid English words. In the event of ties return
        the first pad that results in the maximum number of valid English words.

        pads (list of lists of ints): A list of pads which might have been used
            to encrypt self.message_text

        Returns: (list of ints, string) a tuple of the best pad and the decrypted plaintext
        '''
        # making punctuations list for use later in the for loop
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # creates dict used later to keep track of each pad and it's number of valid words
        valid_words_dict = {}
        # for every pad in pads, gets the number of valid words from decrypting the text using the pad at the pad_num index in pads and adds the number of the pad and it's number of words to the dict
        for pad_num in range(len(pads)):
        # decrypting the message using the pad at index pad_num and making all letters lowercase
            decrypted_message = EncryptedMessage.decrypt_message(self, pads[pad_num]).lower()
        # making empty string for use in for loop to get rid of all punctuation and get a string with no punctuation
            decrypted_message_no = ""
            for char in decrypted_message:
                if char not in punctuations:
                    decrypted_message_no = decrypted_message_no + char
        # making a list of the decrypted message with no punctuation and a count variable to count the number of valid words
            decrypted_message_list = decrypted_message_no.split()
            count = 0
        # adds 1 to the count for every valid word that is in the decrypted message using the given pad
            for i in range(len(decrypted_message_list)):
                if decrypted_message_list[i] in self.valid_words:
                    count += 1
        # adding the pad index in pads with the count as a key-value pair to the dict
            valid_words_dict.update({pad_num:count})
        # creating lists and sorted lists for the keys and values of the dict
        valid_words_dict_keys = list(valid_words_dict.keys())
        valid_words_dict_vals = list(valid_words_dict.values())
        #print (valid_words_dict_keys, valid_words_dict_vals)
        sorted_valid_words_dict_vals = sorted(list(valid_words_dict.values()))
        # creating a variable for the position of the pad with the highest value
        position = valid_words_dict_vals.index(sorted_valid_words_dict_vals[len(sorted_valid_words_dict_vals) - 1])
        # getting the index of the best pad in the keys of the dict
        best_pad = valid_words_dict_keys[position]
        # creating a tuple of the best pad with the decrypted message of that pad
        return (pads[best_pad], EncryptedMessage.decrypt_message(self, pads[best_pad]))


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    
    input_text = get_story_string()
    pads = get_story_pads()
    message = EncryptedMessage(input_text)
    decrypted_message = message.decrypt_message_try_pads(pads)
    return decrypted_message[1]



if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    pass
