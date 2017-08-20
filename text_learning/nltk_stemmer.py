from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
print stemmer.stem('responsive')
print stemmer.stem('respond')
print stemmer.stem('amritasha')
print stemmer.stem('mobile')
print stemmer.stem('medicine')
print stemmer.stem('switch')
print stemmer.stem('cupboard')