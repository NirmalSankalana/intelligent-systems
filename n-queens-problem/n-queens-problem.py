class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        # Find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))

        # prune down candidates to that place
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

        return []

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            solutions.append(self.state_to_string(state, n))
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            s = '.'*i + 'Q' + '.'*(n-i-1)
            ret.append(s)
        return ret
