import random
import turtle

rules = {
    "F": lambda: "FF+[+F-F-F]-[-F+F+F]" if random.random() > 0.5 else "FF-[-F+F+F]+[+F-F-F]"
}
axiom = "F"
iterations = 5
angle = 25
length = 5

# Modify the `generate_lsystem` function to handle callable rules
def stochastic_l_system(axiom, rules, iterations, angle, length):
    def generate_lsystem(axiom, rules, iterations):
        for _ in range(iterations):
            axiom = ''.join(rules[symbol]() if callable(rules.get(symbol)) else rules.get(symbol, symbol) for symbol in axiom)
        return axiom

    def draw_lsystem(word, angle, length):
        stack = []
        for symbol in word:
            if symbol == "F":
                turtle.forward(length)
            elif symbol == "+":
                turtle.left(angle)
            elif symbol == "-":
                turtle.right(angle)
            elif symbol == "[":
                stack.append((turtle.position(), turtle.heading()))
            elif symbol == "]":
                position, heading = stack.pop()
                turtle.penup()
                turtle.goto(position)
                turtle.setheading(heading)
                turtle.pendown()

    word = generate_lsystem(axiom, rules, iterations)
    turtle.speed(0)
    draw_lsystem(word, angle, length)
    turtle.done()

stochastic_l_system(axiom, rules, iterations, angle, length)