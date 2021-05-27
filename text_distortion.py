import requests, re

word_list = requests.get("https://www.kilgarriff.co.uk/BNClists/variances").text # load word list file
word_list = [line.split()[0] for line in word_list.split("\n")[:-2]]             # parse words
word_list = list(dict.fromkeys(word_list).keys())                                # remove duplicates

def text_distortion(text, k=300, multiple_asterisk=False):
    """
            Text Distortion: A simple function to mask topic-related text units in a given text.
            ------------------------------------------------------------------------------------
            :param text: The given text.
            :param k: The k-frequent words in the internal wordlist (these will be preserved in the masked text representation).
            :param multiple_asterisk: Flags which text distortion variant should be used (True = Multiple Asterisks, False = Single Asterisks).
            :return: masked text representation.
            ------------------------------------------------------------------------------------
            """
    word_set = set(word_list[:k])
    for match in reversed(list(re.finditer(r"\b\w+\b", text))):
        match_string = match.group()
        if match_string.isdigit():
            text = text[:match.start()] + "#" * (len(match_string) if multiple_asterisk else 1) + text[match.end():]
        elif match_string.lower() not in word_set:
            text = text[:match.start()] + "*" * (len(match_string) if multiple_asterisk else 1) + text[match.end():]
    return text


text = '''
Stylometry grew out of earlier techniques of analyzing texts for evidence of authenticity, author identity, and other questions.
The modern practice of the discipline received publicity from the study of authorship problems in English Renaissance drama. 
Researchers and readers observed that some playwrights of the era had distinctive patterns of language preferences, 
and attempted to use those patterns to identify authors of uncertain or collaborative works. Early efforts were not always successful: 
in 1901, one researcher attempted to use John Fletcher's preference for "⁠ ⁠’em", the contractional form of "them", 
as a marker to distinguish between Fletcher and Philip Massinger in their collaborations—- but he mistakenly employed an edition 
of Massinger's works in which the editor had expanded all instances of "⁠ ⁠’em" to "them".
'''

print(text_distortion(text, k=100),
      text_distortion(text, k=500),
      text_distortion(text, k=500, multiple_asterisk=True),
      text_distortion(text, k=1000),
      sep="\n")