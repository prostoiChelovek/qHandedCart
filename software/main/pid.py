class Pid:
    def __init__(self, p, i, d, target):
        self.i = i
        self.p = p
        self.d = d

        self.target = target

        self._last_error = 0
        self._Ie = 0

    def compute(self, current):
        e = self.target - current

        de = e - self._last_error
        self._Ie += e
        self._last_error = e

        return self.p * e \
             + self.i * self._Ie \
             + self.d * de

    def __str__(self):
        params = f"P: {self.p}, I: {self.i}, D: {self.d}"
        state = f"target: {self.target}, last_error: {self._last_error}, Ie: {self._Ie}"
        return f"PID: {{\n\t{params}\n\t{state}\n}}"
