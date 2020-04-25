import pickle
from core.Board import Board
from core.BoardSolver import BoardSolver
import random

def get_words():
    with open('data/words_en.pkl','rb') as f:
            words = pickle.load(f)
            return words

def get_random_words(words, length, count):
    p = filter(lambda w: len(w) == length, words)
    return random.sample(list(p), k = count)

def generate_puzzle(word, size):
    b = Board(size, size)
    b.fill_random()
    b.set_word(word)
    b.mess(word)
    bs = BoardSolver()
    m = bs.solve2(b, word)
    if m > 0:
        print(f"{b.get_tiles_str()}, {word}, {size}, {m}") 
        return (b.get_tiles_str(), word, size, size, len(word), m)

def generate():
    all_words = get_words()
    all_words = list(filter(lambda w: len(w) > 1, all_words))
    puzzles = []
    for s in range(3, 6, 1):
        max_word_length = min(s * s - 1, 12)
        for l in range(2, max_word_length, 1):
            words = get_random_words(all_words, l, 10)
            for w in words:
                puzzles.append(generate_puzzle(w, s))
    return puzzles

def save(puzzles, filename):
    l = [','.join(map(str, p)) for p in puzzles if p]
    open(filename, 'w').write('\n'.join(l))

def main():
    puzzles = generate()
    save(puzzles, "puzzles4.txt")
 
if __name__ == '__main__':
    main()
        