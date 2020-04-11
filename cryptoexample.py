from cryptography.fernet import Fernet
# Put this somewhere safe!
key = open("key","rb")
f = Fernet(key.read())
token = open("token","rb")

pass
f.decrypt(token.read())#'A really secret message. Not for prying eyes.'
key.close()
token.close()