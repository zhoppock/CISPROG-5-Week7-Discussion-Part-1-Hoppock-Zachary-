from encryption import encryption

text = input("Please input plaintext: ")

f = open("encrypt_file.txt","w")
f.write(encryption(text))
f.close()

f = open("encrypt_file.txt","r")
code = f.read()
print("\nYour encrypted file says:\n", code)
f.close()