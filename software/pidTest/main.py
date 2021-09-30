import matplotlib.pyplot as plt

plt.title("график")
plt.xlabel("время")  # ось абсцисс
plt.ylabel("скорость")  # ось ординат
plt.grid()


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


pid = Pid(1.1, 1.1, 0, 0)
print(pid)

v = 0
v00, t0 = 10, 10

x = []
y = []
yc = []

for t in range(100):
    if t == t0:
        pid.target = v00

    V = pid.compute(v)
    V = max(-100, min(100, V))

    x.append(t)
    y.append(v)
    yc.append(pid.target)

    v += V

    print("t =", t, pid)


print(x)
print(y)

fig, axs = plt.subplots(2)
axs[0].plot(x,y)
axs[1].plot(x, yc)
plt.show()
