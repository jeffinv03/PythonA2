# Name: Jeffin Varghese
# UTEID: jjv2349
#
# On my honor, Jeffin Varghese, this programming assignment is my own work
# and I have not provided this code to any other student.

from collections import Counter

class WordleSolver:

    def __init__(self):
        self.__all_words = set()
        self.__possible_words = set()
        self.get_words()
        self.reset()
    
    def reset(self):
        self.__possible_words = set(self.__all_words)

    def get_guess(self, feedback):
        """
        Make a guess for the current round of Wordle.
        :param feedback: A list of strings representing the guesses so far
        and the feedback for those guesses in the current game of Wordle.
        If feedback is empty then this is the first guess.
        The order of the elements of feedback is [feedback_1, guess_1,
        feedback_2, guess_2, ...]
        All strings are length 7.
        The feedback strings consist of G, O, and -.
        G for GREEN, correct letter in correct spot.
        O for letter in word but not in right spot.
        - for letter not in word.
        :return: A string that is in __all_words and is the next guess.
        """

        if not feedback:
            # Make first guess using most common letters in all words
            letter_counts = Counter("".join(self.__all_words))
            guess = "".join([letter_counts.most_common()[i][0] for i in range(7)])
        else:
            # Update possible words based on feedback
            self.__possible_words = set(filter(lambda w: self.__matches_feedback(w, feedback), self.__possible_words))
            # Make next guess using most common letters in possible words
            letter_counts = Counter("".join(self.__possible_words))
            guess = "".join([letter_counts.most_common()[i][0] for i in range(7)])
        return guess

    def get_words(self):
        """ Read the words from the dictionary file and place them
        in the __all_words instance variable.
        We assume the  required files are in the current working directory
        and is named all_words_5.txt. We also assume all words are
        seven letters long, one word per line.
        Returns a set of strings with all the words from the file.
        """
        with open('all_words_7.txt', 'r') as data_file:
            all_lines = data_file.readlines()
            for line in all_lines:
                self.__all_words.append(line.strip())

    def show_words(self):
        """
        Debugging method to check file was read in correctly.
        :return: None
        """
        print(len(self.__all_words))
        for word in self.__all_words:
            print(word)

    def __matches_feedback(self, word, feedback):
        for i, letter in enumerate(word):
            if feedback[i] == "G" and letter != feedback[i]:
                return False
            if feedback[i] == "-" and letter in feedback:
                return False
            if feedback[i] == "O" and (letter in feedback or letter == feedback[i]):
                return False
        return True
'''
CS109 Students, include your write up (15/50 points) here at the end of your class.
'''
