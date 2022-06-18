def encryption(text):
  print("\nYour plaintext is:", text)
  plainText = text
  distance = 4
  code = ""
  for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('~'):
      cipherValue = ord('!') + distance - (ord('~') - ordvalue + 1)
    code += chr(cipherValue)
  print("The encrypted text is:", code)
  return code