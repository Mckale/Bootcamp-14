
def words(wordz):
    wordlist=wordz.split()
    freq=[wordlist.count(w) for w in wordlist]
    dictionary=dict(zip(wordlist,freq))
    
    d=""
    for i in dictionary:
        a=i
        b=dictionary[i]
        c=a+":"+ str(dictionary[i])
        d=d+c+'\n'
    print(d)
    return d

words("one one chicken chicken two fish fish white hen blue blue cow cow")
