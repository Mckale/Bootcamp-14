

from collections import Counter




def words(Words_to_count):
    if Words_to_count != '':
        splited_words = Words_to_count.split()
        counted_words= Counter(splited_words)
        counted_words.keys()
        for key, value in counted_words.items():
            print(key, value)


            
words("one one chicken chicken two fish fish white hen blue blue cow cow")
