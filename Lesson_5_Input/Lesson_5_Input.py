exit = "no"

while exit.lower() == "no":
    colors = input(
        'Write figures for colors Cyan(C), Magenta(M), Yellow(Y), Black(B) with scale from 0.0 to 1.0 (e.g., 0.5 0.6 0.7 0.8): '
    )

    if len(colors) < 15:
        print("wrong input")
    else:
        cyan = float(colors[0:3])
        magenta = float(colors[4:7])
        yellow = float(colors[8:11])
        black = float(colors[12:15])

        white = 1 - black
        red = 255 * white * (1 - cyan)
        green = 255 * white * (1 - magenta)
        blue = 255 * white * (1 - yellow)

        print(f'RGB: R:{int(red)} G:{int(green)} B:{int(blue)}')

    exit = input(
        "Did you finish? exit/e or no: "
    )


