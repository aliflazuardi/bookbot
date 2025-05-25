def count_words(sentences):
    words = sentences.split()
    return len(words)


def count_characters(sentences):
    chars = {}

    for c in sentences:
        if c.lower() not in chars:
            chars[c.lower()] = 1
        else:
            chars[c.lower()] += 1

    return chars


def sort_on(dict):
    return dict["num"]


def sort_char_count_dict(count_dict):
    counts = []

    for key, val in count_dict.items():
        counts.append({"char": key, "num": val})

    counts.sort(reverse=True, key=sort_on)

    return counts
