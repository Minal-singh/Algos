# rabin karp algorithm

def rabin_karp(text, pattern):
    # hash function
    def hash_function(string):
        hash_value = 0
        for i in range(len(string)):
            hash_value += ord(string[i]) * (256 ** (len(string) - i - 1))
        return hash_value

    # hash value of pattern
    pattern_hash = hash_function(pattern)
    # hash value of text
    text_hash = hash_function(text[:len(pattern)])

    # loop through text
    for i in range(len(text) - len(pattern) + 1):
        # check if hash value of text and pattern are same
        if text_hash == pattern_hash:
            # check if text and pattern are same
            if text[i:i + len(pattern)] == pattern:
                return i
        # calculate hash value of next text
        if i < len(text) - len(pattern):
            text_hash -= ord(text[i])
            text_hash /= 256
            text_hash += ord(text[i + len(pattern)]) * (256 ** (len(pattern) - 1))

    return -1
