def all_pairs(key_pairs) -> bool:
    if key_pairs is None:
        return False
    for pair in key_pairs:
        if is_valid_pair(pair):
            continue
        else:
            return False
    return True


def is_valid_pair(pair) -> bool:
    if pair is None or (len(pair) != 0 and len(pair) != 2):
        return False
    return len(pair) == 0 or str.isalpha(pair[0]) and str.isalpha(pair[1])


def get_column(key_pairs, column) -> list:
    chars_in_column = []
    for pair in key_pairs:
        if len(pair) == 0:
            return []
        chars_in_column.append(pair[column])
    return chars_in_column


def contains_in_suffix(chars, initial_pos, c) -> bool:
    if chars is None or initial_pos < 0 or initial_pos >= len(chars):
        return False
    return c in chars[initial_pos:]


def unique(chars) -> bool:
    if chars is None:
        return False
    return len(set(chars)) == len(chars)


def is_valid(key_pairs) -> bool:
    if key_pairs is None:
        return False
    flat_values = []
    for pair in key_pairs:
        flat_values.extend(pair)
    return all_pairs(key_pairs) and unique(flat_values)


def invert(key_pairs):
    if len(key_pairs) == 1 and len(key_pairs[0]) == 0:
        return [[]]
    inverted_key_pairs = []
    if is_valid(key_pairs):
        for pair in key_pairs:
            inverted_key_pairs.append(swap(pair))
    return inverted_key_pairs


def swap(pair):
    return [pair[1], pair[0]]


def create_key(left, right) -> list:
    if left is None or right is None:
        raise TypeError("left or right is None")
    if len(left) == 0 or len(right) == 0:
        return [[]]
    key = []
    i = 0
    if len(left) >= len(right):
        for char in range(len(right)):
            key.append(create_key_pair(left[i], right[i]))
            i += 1
    else:
        for char in range(len(left)):
            key.append(create_key_pair(left[i], right[i]))
            i += 1
    return key


def create_key_pair(left, right):
    return [left, right]


def encode_char(key_pairs, c):
    if len(key_pairs) == 1 and len(key_pairs[0]) == 0:
        return -1
    for pair in key_pairs:
        if c == pair[0]:
            return pair[1]
    return -1


def encode_text(key_pairs, clear_text):
    if clear_text == "":
        return ""
    chars = list(clear_text)
    entry_alphabet = []
    for pair in key_pairs:
        entry_alphabet.extend(pair[0])
    if any(c not in entry_alphabet for c in chars):
        return None
    encoded_text = ""
    for char in chars:
        encoded_text += get_equivalent(char, key_pairs)
    return encoded_text


def get_equivalent(char, key_pairs):
    for pair in key_pairs:
        if char == pair[0]:
            return pair[1]


def decode_text(key_pairs, encoded_text):
    if encoded_text == "":
        return ""
    chars = list(encoded_text)
    exit_alphabet = []
    for pair in key_pairs:
        exit_alphabet.extend(pair[1])
    if any(c not in exit_alphabet for c in chars):
        return None
    decoded_text = ""
    for char in chars:
        decoded_text += get_equivalent_decode(char, key_pairs)
    return decoded_text


def get_equivalent_decode(char, key_pairs):
    return next((pair[0] for pair in key_pairs if char == pair[1]), None)

