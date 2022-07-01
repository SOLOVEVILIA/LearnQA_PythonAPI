#Чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python3 -m pytest -s %my_test%.py
phrase = input("Enter a phrase no longer than 15 characters: ")

assert len(phrase) < 15, f'You entered a phrase with a length of {len(phrase)}'
