from sys import argv

script, user_name, work = argv
prompt = "> "

print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a new question.")

print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("You work is work?")
work = input(prompt)

print(f"""
Aright, So you said {likes} about like me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.
And you work is {work}. Nice.
""")
