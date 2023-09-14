# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        pass
        # get access to all the words in th list 
        # check if all the letters in word are in a word in the list
        
        new_word = ""
        anagram_list = []
        for list_word in list_of_words:
            for letter in list_word:
                if letter in self.word:
                    new_word += letter
                else: 
                    new_word = "remove"
            if "remove" in new_word:    
                new_word = ""
            else:
                if len(self.word) == len(new_word):
                    anagram_list.append(new_word)
                new_word = ""
        return anagram_list

# test = Anagram("word")
# test.match( ["hello", "goodbye"])

# test2 = Anagram("listen")
# test2.match(['enlists', 'google', 'inlets', 'banana'])

# import ipdb; ipdb.set_trace()
