import turtle
import random



def l_system(axiom, rules, iterations, angle, length):
    def generate_lsystem(axiom, rules, iterations):
        words = [axiom]
        for _ in range(iterations):
            axiom = ''.join(rules.get(symbol, symbol) for symbol in axiom)
            words.append(axiom)
        return words

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

    words = generate_lsystem(axiom, rules, iterations)
    for i, word in enumerate(words):
        print(f"Iteration {i}: {word}")
    turtle.speed(0)
    draw_lsystem(words[-1], angle, length)
    turtle.done()

rules = {
    "F": "F[+F]F[-F]F"
}
axiom = "F"
iterations = 5
angle = 25
length = 5

l_system(axiom, rules, iterations, angle, length)

