palabra=input("ingrese una palabra")
if palabra==palabra[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")