import multiprocessing
from functools import partial

from core.Board import Board

class BoardSolver:

    def opposite_direction(self, d):
        opposites = {0:2,1:3,2:0,3:1}
        return opposites[d]
    
    def all_posible_moves(self, board):
        moves = []
        e_row, e_col = board.get_empty_pos()
        for d in [0, 1, 2, 3]:
            r, c = board.adjacent_position(e_row, e_col, d)
            while board.inside(r,c):
                moves.append((r, c, d))
                r, c = board.adjacent_position(r, c, d)
        return moves

    def rate_state(self, state, word):
        return 1

    def best_states(self, states, count, word):
        rates = sorted([(s, self.rate_state(s, word)) for s in states])[:count]
        mean_distance = sum([r[1] for r in rates]) / len(rates)
        print(mean_distance)
        result = [r[0] for r in rates]
        return result

    def get_child(self, board, state, touch_r, touch_c, touch_d):
        board.set_tiles(state)
        board.touch_d(touch_r, touch_c, self.opposite_direction(touch_d))
        return board.get_tiles_str()            

    def get_childs(self, state, board):
        board.set_tiles(state)                    
        moves = self.all_posible_moves(board)
        childs = [self.get_child(board, state, r,c,d) for r,c,d in moves]        
        return childs

    def is_solved(self, state, board, word):
        board.set_tiles(state)
        return board.solved(word)

    def solve2(self, board, word):
        b = board.copy()
        depth = 0
        previous_states = set()
        states = set([b.get_tiles_str()])
        while len(states) > 0 and depth <= 7:
            #print(f"depth: {depth}, states: {len(states)}")
            depth += 1
            childs = [self.get_childs(s, b) for s in states]
            childs = set([item for sublist in childs for item in sublist])
            new_childs = childs - previous_states
            childs_solved = [self.is_solved(s, b, word) for s in new_childs]
            if any(childs_solved):
                return depth
            previous_states = previous_states | new_childs # best_new_states
            states = new_childs # best_new_states
        return -1

    def psolve2(self, board, word):        
        b = board.copy()
        depth = 0
        previous_states = set()
        states = set([b.get_tiles_str()])
        with multiprocessing.Pool() as pool:
            while len(states) > 0 and depth <= 10:
                #print(f"depth: {depth}, states: {len(states)}")
                depth += 1
                result = pool.imap(partial(self.get_childs, board = b), states, chunksize=10000)
                childs = set([item for sublist in result for item in sublist])
                new_childs = childs - previous_states
                childs_solved = pool.imap(partial(self.is_solved, board = b, word = word), new_childs, chunksize=10000)
                if any(childs_solved):
                    return depth
                previous_states.update(new_childs) # best_new_states
                states = new_childs # best_new_states
            return -1

    def solve(self, board, word):
        b = board.copy()
        depth = 0
        previous_states = []
        states = [b.get_tiles()]
        while len(states) > 0:
            print(f"depth: {depth}, states: {len(states)}")
            depth += 1
            new_states = []
            for state in states:
                b.set_tiles(state)                    
                moves = b.all_posible_moves()
                for r, c, d in moves:
                    b.touch_d(r, c, self.opposite_direction(d))
                    if b.__tiles not in previous_states:
                        if b.solved(word):
                            return depth
                        new_states.append(b.get_tiles())
                    b.set_tiles(state)
            
            #best_new_states = self.best_states(new_states, 500, word)
            
            previous_states += new_states # best_new_states
            states = new_states # best_new_states

