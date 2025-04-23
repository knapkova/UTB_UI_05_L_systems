import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, radians

def lsystem(axiom, rules, iterations, angle, length, output_file="lsystem.gif"):
    def generate_lsystem(axiom, rules, iterations):
        words = [axiom]
        for i in range(iterations):
            axiom = ''.join(rules.get(symbol, symbol) for symbol in axiom)
            words.append(axiom)
            print(f"Iteration {i + 1}: {axiom}")
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
        ax.axis("equal")
        ax.axis("off")

    words = generate_lsystem(axiom, rules, iterations)
    fig, ax = plt.subplots()
    ax.axis("equal")
    ax.axis("off")

    def update(frame):
        draw_frame(words[frame], angle, length, ax)

    anim = FuncAnimation(fig, update, frames=len(words), repeat=False)
    anim.save(output_file, writer="pillow")
    plt.close(fig)

hilbert_rules = {
    "A": "-BF+AFA+FB-",
    "B": "+AF-BFB-FA+"
}
hilbert_axiom = "A"
lsystem(
    axiom=hilbert_axiom,
    rules=hilbert_rules,
    iterations=5,
    angle=90,
    length=5,
    output_file="results/hilbert_curve.gif"
)

plant_rules = {
    "X": "F-[[X]+X]+F[+FX]-X",
    "F": "FF"
}
plant_axiom = "X"
lsystem(
    axiom=plant_axiom,
    rules=plant_rules,
    iterations=6,
    angle=25,
    length=5,
    output_file="results/fractal_plant.gif"
)

dragon_rules = {
    "X": "X+YF+",
    "Y": "-FX-Y"
}
dragon_axiom = "FX"
iterations = 10
angle = 90
length = 5

lsystem(
    axiom=dragon_axiom,
    rules= dragon_rules,
    iterations = iterations,
    angle = angle,
    length = length,
    output_file="results/dragon_curve.gif")

rules = {
    "F": "FF-[-F+F+F]+[+F-F-F]"
}
axiom = "F"
iterations = 5
angle = 25
length = 5

lsystem(axiom, rules, iterations, angle, length, output_file="results/new.gif")