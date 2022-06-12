from decouple import config

passw = config("PASSWORD")
print(passw)