import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, radians

def animate_lsystem(axiom, rules, iterations, angle, length):
    def generate_lsystem(axiom, rules, iterations):
        words = [axiom]
        for _ in range(iterations):
            axiom = ''.join(rules.get(symbol, symbol) for symbol in axiom)
            words.append(axiom)
        return words

    def draw_frame(word, angle, length, ax):
        stack = []
        x, y = 0, 0
        direction = 0
        positions = [(x, y)]
        for symbol in word:
            if symbol == "F":
                x += length * cos(radians(direction))
                y += length * sin(radians(direction))
                positions.append((x, y))
            elif symbol == "+":
                direction += angle
            elif symbol == "-":
                direction -= angle
            elif symbol == "[":
                stack.append((x, y, direction))
            elif symbol == "]":
                x, y, direction = stack.pop()
                positions.append((x, y))
        ax.clear()
        ax.plot(*zip(*positions), color="black")

    words = generate_lsystem(axiom, rules, iterations)
    fig, ax = plt.subplots()
    ax.axis("equal")

    def update(frame):
        draw_frame(words[frame], angle, length, ax)

    anim = FuncAnimation(fig, update, frames=len(words), repeat=False)
    anim.save("lsystem.gif", writer="pillow")
    plt.show()


