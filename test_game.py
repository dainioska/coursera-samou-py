import random

number = random.randint(0, 101)

while True:
    answer = input("Ivesk skaiciu:")
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print("Ivesk gera skaiciu:")
        continue
    user_answer = int(answer)

    if user_answer > number:
        print("Skaicius yra mazesnis:")
    elif user_answer < number:
        print("Skaicius yra didesnis:")
    else:
        print("Atspejai!!!")
        break