from textdistortion import TextDistorter

distorter = TextDistorter()

text = '''
Stylometry grew out of earlier techniques of analyzing texts for evidence of authenticity, author identity, and other questions.
The modern practice of the discipline received publicity from the study of authorship problems in English Renaissance drama. 
Researchers and readers observed that some playwrights of the era had distinctive patterns of language preferences, 
and attempted to use those patterns to identify authors of uncertain or collaborative works. Early efforts were not always successful: 
in 1901, one researcher attempted to use John Fletcher's preference for "⁠ ⁠’em", the contractional form of "them", 
as a marker to distinguish between Fletcher and Philip Massinger in their collaborations—- but he mistakenly employed an edition 
of Massinger's works in which the editor had expanded all instances of "⁠ ⁠’em" to "them".
'''

print(distorter.distort(text, k=100),
      distorter.distort(text, k=500),
      distorter.distort(text, k=500, multiple_asterisk=True),
      distorter.distort(text, k=1000),
      sep="\n")
