# https://codefights.com/challenge/6xQ39k7XWedRPdgmi

small = {
  "one" : 1,
  "two" : 2,
  "three": 3,
  "four" : 4,
  "five" : 5,
  "six" : 6,
  "seven" : 7,
  "eight" : 8,
  "nine" : 9,
  "ten" : 10,
  "eleven" : 11,
  "twelve" : 12,
  "thirteen" : 13,
  "fourteen" : 14,
  "fifteen" : 15,
  "sixteen" : 16, 
  "seventeen" : 17, 
  "eighteen" : 18, 
  "ninteen" : 19
}

tens = {
  "twenty" : 20,
  "thirty" : 30,
  "forty" : 40,
  "fifty" : 50,
  "sixty" : 60,
  "seventy" : 70,
  "eighty" : 80,
  "ninety" : 90
}

def wordsnumbers(n):
  words = n.split()
  num = 0
  
  for i,word in enumerate(words):
    is_last = (i == len(words)-1)
    if word in small:
      num = handle_small(num, word, is_last)
    if word in tens:
      next_word = None if is_last else words[i+1]
      num = handle_tens(num, word, next_word)
    if word == "hundred":
      num = handle_hundred(num, word, words[i-1])
    if word == "thousand":
      num = handle_thousand(num, word, words[i-1])

  return num

def handle_small(num, word, is_last):
  if is_last:
    num = num + small[word]
  
  # if not is_last, let hundred/thousand subroutine take care
  # of this case

  return num

def handle_tens(num, word, next_word):
  # if next_word is None then just add the tens
  # if next_word is in small, just add the tens and let small do the next
  # if next_word is hundred/thousand, let the other subroutines do their job
  if next_word != "hundred" and next_word != "thousand":
    return num + tens[word]

def handle_hundred(num, word, prev):
  prev_int = small[prev] if prev in small else tens[prev]

  return num + (100*prev_int)

def handle_thousand(num, word, prev):
  prev_int = small[prev] if prev in small else tens[prev]

  return num + (1000*prev_int)
