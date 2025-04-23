import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, radians

def tornado_lsystem_gif(axiom, rules, iterations, angle, length, output_file="tornado.gif"):
    def generate_lsystem(axiom, rules, iterations):
        words = [axiom]
        for _ in range(iterations):
            axiom = ''.join(rules.get(c, c) for c in axiom)
            words.append(axiom)
        return words

    def draw_tornado_3d(word, angle, length, ax):
        x, y, z = 0, 0, 0
        yaw = 0
        positions = [(x, y, z)]
        widths = [5]

        for i, symbol in enumerate(word):
            if symbol == "F":
                # Spiral around Y axis
                spiral_radius = max(0.5, 10 - z * 0.1)  # tighter near top
                yaw += angle
                x = spiral_radius * cos(radians(yaw))
                y = spiral_radius * sin(radians(yaw))
                z += length * 0.5  # always goes upward
                positions.append((x, y, z))
                widths.append(max(0.5, widths[-1] * 0.95))
            elif symbol == "[":
                pass  # No branching for clean tornado
            elif symbol == "]":
                pass

        ax.clear()
        for i in range(len(positions) - 1):
            x1, y1, z1 = positions[i]
            x2, y2, z2 = positions[i + 1]
            ax.plot([x1, x2], [y1, y2], [z1, z2],
                    color=plt.cm.Greys(widths[i] / 5),
                    linewidth=widths[i])
        ax.view_init(elev=25, azim=45)
        ax.axis("off")

    words = generate_lsystem(axiom, rules, iterations)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        draw_tornado_3d(words[frame], angle, length, ax)

    anim = FuncAnimation(fig, update, frames=len(words), repeat=False)
    anim.save(output_file, writer="pillow")
    plt.close(fig)

# Tornado-like rule: no branching, just forward movement
rules = {
    "F": "FF"
}
axiom = "F"
tornado_lsystem_gif(axiom, rules, iterations=100, angle=20, length=1.2, output_file="tornado_2.gif")
