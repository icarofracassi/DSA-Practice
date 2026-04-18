while True:
  phrase = input()
  firstLetter = phrase[0]
  if firstLetter == "*":
    break
  breakedPhrase = phrase.split(" ")
  answer = True
  for word in breakedPhrase:
    wordLetter = work[0]
    if firstLetter.capitalize() != wordLetter.capitalize():
      answer = False
    if answer:
      print("Y")
    else:
      print("N")
