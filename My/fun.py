learn_Python = True
alive = True
energy = 10
motivation = 5
cat_is_watching = True
coffee_supply = 3
keyboard_broken = False
internet_working = True
python_bug_detected = False
favorite_snack = 5
neighbor_is_dancing = False

while learn_Python:
    if alive:
        print("Ты жив — самое время учить Python!")
        energy -= 1  # Немного усталости
    elif energy <= 0:
        print("Энергия закончилась! Сделай перерыв, выпей кофе и продолжай.")
        if coffee_supply > 0:
            coffee_supply -= 1
            energy += 3
            print(f"Ты выпил кофе. Осталось {coffee_supply} чашек.")
        else:
            print("Кофе закончился! Теперь учишь Python на чистой воле.")
            break
    elif motivation <= 0:
        print("Мотивация упала до нуля. Представь себя разработчиком с котом на клавиатуре!")
        motivation += 2  # Поднимаем мотивацию
    elif cat_is_watching:
        print("Кот смотрит на тебя с осуждением: 'Ты точно пишешь код, а не смотришь мемы?'")
        if energy > 5:
            print("Кот решает спать, но всё ещё следит одним глазом.")
        else:
            print("Кот демонстративно ложится на клавиатуру. Что ж, теперь пауза.")
            break
    elif keyboard_broken:
        print("Клавиатура сломалась! Придётся программировать голосом.")
        break
    elif internet_working == False:
        print("Интернет отключился! Переходи к изучению теории Python.")
        break
    elif python_bug_detected:
        print("Ты нашёл баг в Python. Позвони Гвидо ван Россуму!")
        break
    elif favorite_snack <= 0:
        print("Закончились любимые перекусы! В голоде Python пишется хуже.")
        break
    elif neighbor_is_dancing:
        print("Сосед устроил дискотеку. Подключись к его колонке и запусти лекцию по Python.")
        neighbor_is_dancing = False  # Решение найдено
    elif energy < 3 and motivation > 2:
        print("Ты еле держишься, но желание стать разработчиком всё ещё горит!")
    elif alive and energy == 1 and motivation == 1:
        print("Ты на последнем издыхании, но всё равно учишь Python. Настоящий герой!")
        break
    else:
        print("Что-то пошло не так... Может, кот закрыл ноутбук?")
        break