
import string

def gematria_dict():
    return {i:v for i, v in enumerate(string.ascii_lowercase, 1)}

print(gematria_dict())