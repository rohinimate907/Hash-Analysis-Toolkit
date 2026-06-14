import re

from constants import HASH_TYPES
from constants import SECURITY_LEVEL


def identify_hash(hash_value):

    if not re.fullmatch(r"[0-9a-fA-F]+", hash_value):
        return None, None

    possible_types = HASH_TYPES.get(len(hash_value))

    if not possible_types:
        return [], []

    security = []

    for h in possible_types:
        security.append(
            (h, SECURITY_LEVEL.get(h, "Unknown"))
        )

    return possible_types, security