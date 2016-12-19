import re

import sys


vowels = "[ауоыиэяюёе]"
not_vowels = "[бвгджзйклмнпрстфхцчшщьъ]"
perfect_gerund_endings = r'(вшись|вши|в)$'
perfect_gerund_endings_for_search = '(а|я)' + perfect_gerund_endings
perfect_gerund_endings2 = r'(ившись|ывшись|ивши|ывши|ив|ыв)$'
reflexive = r'(сь|ся)$'
adjective = r'(ыми|ими|его|ого|ему|ому|ее|ие|ые|ое|ей|ий|ый|ой|ем|им|ым|ом|их|ых|ую|юю|ая|яя|ою|ею)$'
verb_group1 = r'(ете|ешь|нно|йте|ли|ем|ло|но|ет|ют|ны|ть|ла|на|й|л|н)$'
verb_group1_for_search = r'(а|я)' + verb_group1
verb_group2 = r'(ейте|уйте|ила|ыла|ена|ите|или|ыли|ило|ыло|ено|ует|уют|ены|ить|ыть|ишь|ей|уй|ил|ыл|им|ым|ен|ят|ит|ыт|ую|ю)$'
noun = r'(иями|ями|ами|ией|иям|ием|иях|ев|ов|ие|ье|ия|ья|еи|ии|ей|ой|ий|ям|ем|ам|ом|ию|ью|ах|ях|о|у|ы|ь|ю|и|е|й|я|а)$'
derivation = r'ость|ост$'
superlative = r'ейше|ейш$'
def getRvPartOfWord(word):
  res = re.search(vowels + '[а-я]\w*', word)
  if res is not None:
    return res.group(0)[1:]
  else:
    return ""

def findR1(word):
  res = re.search(vowels+not_vowels+'[а-я]*', word)
  if res is not None:
    return res.group(0)[2:]
  else:
    return ""

def findR2(word):
  res = re.search(vowels+not_vowels+'[а-я]*', findR1(word))
  if res is not None:
    return res.group(0)[2:]
  else:
    return ""

while True:
  word = input("Enter the word\n").lower()
  rv_part = getRvPartOfWord(word)

  #step1
  res1_1 = re.search(perfect_gerund_endings_for_search, rv_part)
  if res1_1 is None:
    res1_2 = re.search(reflexive, rv_part)
    if res1_2 is not None:
      word = re.sub(reflexive,'',word)
      rv_part = getRvPartOfWord(word)
    res1_3 = re.search(adjective, rv_part)
    if res1_3 is not None:
      word = re.sub(adjective,'',word)
      rv_part = getRvPartOfWord(word)
    else:
      res1_4 = re.search(verb_group1_for_search, rv_part)
      if res1_4 is not None:
        word = re.sub(verb_group1,'',word)
        rv_part = getRvPartOfWord(word)
      else:
        res1_5 = re.search(verb_group2,rv_part)
        if res1_5 is not None:
          word = re.sub(verb_group2,'',word)
          rv_part = getRvPartOfWord(word)
        else:
          res1_6 = re.search(noun,rv_part)
          if res1_6 is not None:
            word = re.sub(noun,'',word)
            rv_part = getRvPartOfWord(word)
  else:
    word = re.sub(perfect_gerund_endings,'',word)
    rv_part = getRvPartOfWord(word)
  #step2
  if rv_part.endswith('и'):
    word = word[:-1]
    rv_part = getRvPartOfWord(word)
  #step3
  r2_part = findR2(word)
  res3 = re.search(derivation, r2_part)
  if res3 is not None:
    word = re.sub(derivation,'',word)
    rv_part = getRvPartOfWord(word)
  #step4
  if rv_part.endswith('нн'):
    word = word[:-1]
  else:
    res4 = re.search(superlative, rv_part)
    if res4 is not None:
      word = re.sub(superlative,'',word)
    elif rv_part.endswith('ь'):
      word = word[:-1]
  print(word)



