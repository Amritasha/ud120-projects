#nltk documentation

from nltk.wsd import lesk
sent = ['I','went','to','the','bank','to','deposit','money','.']
print lesk(sent,'bank')
print

from nltk.corpus import wordnet as wn
for ss in wn.synsets('bank'):
    print ss,ss.definition()
print

print [(s,s.pos()) for s in wn.synsets('able')]
print
sent = 'people should be able to marry a person of their choice'.split()
print lesk(sent,'able')
print lesk(sent,'able',pos='a')
print
print lesk('John loves Mary'.split(),'loves')
print lesk('John loves Mary'.split(),'loves',synsets=[])