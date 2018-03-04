from argon2 import PasswordHasher

hash = PasswordHasher().hash("pass")
PasswordHasher().verify(hash, "pass")