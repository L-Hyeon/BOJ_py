import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  vowels = {'a', 'e', 'i', 'o', 'u'}
  while (S != "end"):
    isAcceptable = True
    hasVowel = False
    pre = ''
    isPreVowel = None
    isPrepreVowel = None

    for s in S:
      if (hasVowel == False and s in vowels):
        hasVowel = True
      if (isPrepreVowel == isPreVowel == (s in vowels)):
        isAcceptable = False
        break
      if (pre == s and not (s == 'e' or s == 'o')):
        isAcceptable = False
        break
      isPrepreVowel = isPreVowel
      isPreVowel = (s in vowels)
      pre = s

    if (hasVowel and isAcceptable):
      print(f"<{S}> is acceptable.")
    else:
      print(f"<{S}> is not acceptable.")

    S = input().strip()

do()
