import json


def main():
    data = None

    with open('words_dictionary.json') as f:
        data = json.load(f)
        # print(data)

    if data:
        parsed_dict = parse_dict(data)
        # print(any_words_shorter_than_k(parsed_dict, 4))
        ppd = preprocess_dict(parsed_dict)
        # print(ppd)

        print('Enter your letters: ')
        letters = input()
        ppd2 = postprocess_dict(ppd, letters)
        word_list = ([v for _, vs in ppd2.items() for v in vs])
        word_list = sorted(word_list)
        print(word_list)

def any_words_shorter_than_k(data, k):
    return any([len(w) < k for w in data])

def parse_dict(data):
    parsed = [k for k in data.keys() if len(k) >= 4]
    return parsed

def preprocess_dict(data):
    word_set = {}
    for w in data:
        w_norm = normalize_word(w)
        if not w_norm in word_set.keys():
            word_set[w_norm] = []
        word_set[w_norm].append(w)
    return word_set

# first letter is center letter
def postprocess_dict(data, letters):
    word_set = {}
    center = letters[0]
    letter_set = set(letters)
    for w in data:
        if all([c in letter_set for c in w]) and (center in w):
            word_set[w] = data[w]
    return word_set

def normalize_word(w):
    w = w.lower()
    w_norm = sorted(w)
    return ''.join(w_norm)

if __name__ == '__main__':
    main()