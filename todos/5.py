def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# Entrada de string
string = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(string)}")
