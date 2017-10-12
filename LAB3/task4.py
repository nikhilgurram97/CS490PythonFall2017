from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

#opening and reading input text file
f=open('text.txt','r')
fr=str(f.read())

#Applying Sentence and Word Tokenization
a=sent_tokenize(fr)
b=word_tokenize(fr)
print'Sentence Tokenizaton:\n'
a1=a[0].split('\n')             #Sentences split into individual elements in a list
print(a1)
print'\n-----\n'
print'Word Tokenizaton:\n'
print b

#Applying POS
e=pos_tag(b)
e1=[v for v in e if v[1] != 'VBG']  #Eliminating Verbs
e2=" ".join([v[0] for v in e1])     #Combining elements of POS to a single sentence
print'\n-----\n'
print'Parts of Speech:\n'
print(e1)
print'\n-----\n'
print'Verb Eliminated Sentence:\n'
print(e2)

#Applying Lemmatization on remaining words
print'\n-----\n'
print'Lemmatization:\n'
l=WordNetLemmatizer()
b1=word_tokenize(e2)
for k in range(len(b1)):
    e1 = l.lemmatize(b1[k])
    print ("The word \'" + b1[k] + "\' in a Lemmatized Version: " + e1)

#Word Frequency of remaining words
fd=FreqDist(e2.split(' '))
print'\n-----\n'
print'Word Frequency:\n'
print(list(fd.most_common(1000)))

#Top 5 repeated words
print'\n-----\n'
print'Top 5 words:\n'
top5=list(fd.most_common(5))
top5d=dict(top5)
top5w=top5d.keys()
print(top5w)

#Finding sentences with most common words
print'\n-----\n'
print'Sentences with most common words:\n'
z1=[]
new=""
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')   #Function that finds existence of words in a sentence and returns boolean value
for i in range(2):
    for j in range(4):
        x=contains_word(a1[i], top5w[j])
        if (x==1):
            #print("\n"+a1[i])
            z1.append(a1[i])        #Appending the sentence to a lsit
            z=set(z1)               #Converting list to a set
            new=' '.join(z)         #Concatenating into a unique sentence
print(z)
print'\n-----\n'
print'Concatenated Sentences:\n'
print(new)