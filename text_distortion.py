import requests, re

class TextDistorter:
    def __init__(self, word_list=None):
        """
        Text Distortion provides a technique to mask topic-related text units in a given text.
        Args:
            word_list: The list of text units (ordered by decreasing frequency) to be distorted. 
            If None, a list is loaded based on 'https://www.kilgarriff.co.uk/BNClists/variances'
        """
        self.word_list = word_list
        if not word_list:
            self.word_list = requests.get("https://www.kilgarriff.co.uk/BNClists/variances").text # load word list file
            self.word_list = [line.split()[0] for line in self.word_list.split("\n")[:-2]]             # parse words
            self.word_list = list(dict.fromkeys(self.word_list).keys())                                # remove duplicates

    def distort(self, text, k, multiple_asterisk=False, distort_char="*", digit_char="#"):
        """
        Distort topic-related text units in a given text.
        Args:
            k: The k-frequent words in the internal wordlist (these will be preserved in the masked text representation).
            multiple_asterisk: Flags which text distortion variant should be used (True = Multiple Asterisks, False = Single Asterisks).
            distort_char: The character used to mask topic-related text units.
            digit_char: The character used to mask text units comprising digits.
        """
        word_set = set(self.word_list[:k])
        for match in reversed(list(re.finditer(r"\b\w+\b", text))):
            match_string = match.group()
            if match_string.isdigit():
                text = text[:match.start()] + digit_char * (len(match_string) if multiple_asterisk else 1) + text[match.end():]
            elif match_string.lower() not in word_set:
                text = text[:match.start()] + distort_char * (len(match_string) if multiple_asterisk else 1) + text[match.end():]
        return text
