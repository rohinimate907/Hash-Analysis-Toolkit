SECURITY_LEVEL = {
    "MD5": "Weak",
    "NTLM": "Weak",
    "LM": "Very Weak",
    "SHA1": "Weak",
    "SHA224": "Moderate",
    "SHA256": "Strong",
    "SHA384": "Strong",
    "SHA512": "Very Strong"
}

HASH_TYPES = {
    32: ["MD5", "NTLM", "LM"],
    40: ["SHA1"],
    56: ["SHA224"],
    64: ["SHA256"],
    96: ["SHA384"],
    128: ["SHA512"]
}