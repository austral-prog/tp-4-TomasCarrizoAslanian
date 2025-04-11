def line():
    import math

    coef_a = float(input("Ingrese el coeficiente A:"))
    coef_b = float(input("Ingrese el coeficiente B:"))
    coef_X1 = float(input("Ingrese el coeficiente X1:"))
    coef_X2 = float(input("Ingrese el coeficiente X2:"))

    print(f"El coeficiente A de su ecuación de la recta es: {coef_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coef_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coef_X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coef_X2}")
    print()
    print(f"Para la siguiente ecuación: \n\tY = {coef_a}X + {coef_b}\n")

    Y1 = coef_a * coef_X1 + coef_b
    Y2 = coef_a * coef_X2 + coef_b

    print(f"Dados los siguientes puntos:")
    print(f"\tP1 ({coef_X1}, {Y1})")
    print(f"\tP2 ({coef_X2}, {Y2})")
    print()
    distancia = math.sqrt((coef_X2 - coef_X1)**2 + (Y2 - Y1)**2)
    print(f"La distancia entre ellos es: {distancia}")
