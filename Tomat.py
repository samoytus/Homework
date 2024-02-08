class Tomato:
    states = {
        'absence': 1,
        'blossom': 2,
        'green': 3,
        'red': 4
    }

    def __init__(self, _index):
        self._index = _index
        self._states = self.states["absence"]

    def grow(self):
        if self.states[self._index] < 4:
            self.states[self._index] += 1

    def is_riped(self):
        return self.states == "red"




