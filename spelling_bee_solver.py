import os.path
import pickle

PICKLE_PATH = "spelling_bee_words.pkl"

def load_words():
    pickleExists = os.path.exists(PICKLE_PATH)
    if not pickleExists:
        valid_words = set()
        with open('words_alpha.txt') as word_file:
            all_words = set(word_file.read().split())
            for word in all_words:
                if len(word) > 3:
                    valid_words.add(word)
        with open(PICKLE_PATH, 'wb') as file:
            pickle.dump(valid_words, file)
        return valid_words
    else:
        with open(PICKLE_PATH, 'rb') as file:
            return pickle.load(file)

def solve_spelling_bee():
    print("NYT Spelling Bee Solver")
    outer_chars = input("Input the outer letters of today's puzzle: ").lower()
    if len(outer_chars) != 6:
        print("Expected 6 letters.")
        return

    center_char = input("Enter special center letter: ").lower()
    if len(center_char) != 1:
        print("Expected 1 letter.")
        return

    all_words = load_words()

    char_set = outer_chars + center_char
    solution_words = []
    for word in all_words:
        if center_char not in word:
            continue
        is_solution = True
        for char in word:
            if char not in char_set:
                is_solution = False
                break
        if is_solution:
            solution_words.append(word)

    print("Here are solution words (some may not be recognized by NYT):")
    solution_words.sort()
    for word in solution_words:
        print(word)

if __name__ == '__main__':
    solve_spelling_bee()
