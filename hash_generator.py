import hashlib


def generate_hashes(text):

    hashes = {
        "MD5": hashlib.md5(text.encode()).hexdigest(),
        "SHA1": hashlib.sha1(text.encode()).hexdigest(),
        "SHA256": hashlib.sha256(text.encode()).hexdigest(),
        "SHA512": hashlib.sha512(text.encode()).hexdigest()
    }

    return hashes