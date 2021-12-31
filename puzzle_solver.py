import json

def main():
    data = None

    file_name = 'words_dictionary.json'

    print(f'> LOADING "{file_name}" <')
    with open(file_name) as f:
        data = json.load(f)

    if data:
        parsed_dict = parse_dict(data)
        ppd = preprocess_dict(parsed_dict)
        print(f'> DICTIONARY LOADED <')

        print('\nEnter your letters - Special letter must be entered first: ')
        letters = input().upper()
        print(f'\n> GENERATING WORDS FOR {show_letters(letters)} <')
        ppd2 = postprocess_dict(ppd, letters)
        word_list = ([v for _, vs in ppd2.items() for v in vs])
        word_list = sorted(word_list)

        print('\nPossible Solutions: ')
        print(word_list)
    
    else:
        print(f'> ERROR! "{file_name}" NOT LOADED <')


# tests whether any words in data are shorter than k letters long
# -- returns true iff at least one word in data is longer than k letters
# -- returns false otherwise
def any_words_shorter_than_k(data, k):
    return any([len(w) < k for w in data])


def show_letters(letters):
    s = f'[{letters[0]}] {" ".join(sorted(letters[1:]))}'
    return s

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
    w_norm = sorted(w.upper())
    return ''.join(w_norm)

if __name__ == '__main__':
    main()