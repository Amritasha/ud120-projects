import nltk
from nltk.corpus import stopwords

#nltk.download()
sw = stopwords.words("english")
print "length of list of stopwords", len(sw)
print sw[152]