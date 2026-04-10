def lei_de_ohm():
    print("Seja bem vindo à Lei de Ohm")
    print("\n")

    while True:
        print("Por favor, Digite apenas dois valores")

        valores = {}

        print("\n")

        valores["v"] = input("Preencha o valor de V(Tensão): ")
        valores["i"] = input("Preencha o valor de I(Corrente): ")
        valores["r"] = input("Preencha o valor de R(Resistência): ")

        print("\n", "-"*50, "\n")

        cont = 0
        nulo = ""
        caracter = False

        for i in valores:
            if valores[i] == "":
                    cont += 1
                    nulo = i
                    continue
            try:
                valores[i] = float(valores[i])
            except:
                print(f"Esse tipo de carácter é inválido: {valores[i]}")
                caracter = True
            
        if caracter:
            continue

        if cont < 1:
            print("Você digitou todos os valores!")
            continue
        if cont > 1:
            print(f"Você esqueçeu de digitar {cont-1} valor(es)!")
            continue

        try:
            if nulo == "r":
                resultado = valores["v"] / valores["i"]
            elif nulo == "i":
                resultado = valores["v"] / valores["r"]
            else:
                resultado = valores["i"] * valores["r"]

            valores[nulo] = resultado
            
            for i in valores:
                print(f"{i}: {valores[i]}")

        except ZeroDivisionError:
            print("Você não pode dividir por Zero")
            continue

        input("Precione 'enter' para voltar!")
        print("-"*50, "\n")
        break

def equilibrio_de_corrente():

    while True:
        print("Seja bem vindo à verificação de equilíbrio de corrente")

        print("\n")

        voltar = False

        corrente_entrada = input("Qual a corrente de entrada do nó: ")
        soma_correntes_saida = input("Qual a soma das correntes de saída do nó: ")

        valores = {
            "corrente de entrada": corrente_entrada,
            "soma das correntes de saída": soma_correntes_saida
        }

        print("\n")

        for i in valores:
            try:
                valores[i] = float(valores[i])
            except:
                print(f"O valor '{valores[i]}' em {i} é inválido!")
                print("-"*50)
                voltar = True
                continue
        if voltar:
            continue

        diferenca = valores["corrente de entrada"] - valores['soma das correntes de saída']
        string_diferenca = str(diferenca)
        diferenca = float(string_diferenca[:len(string_diferenca)-1])

        if abs(diferenca) <= 0.01:
            print("Nó equilibrado")
        else:
            print("Nó não equilibrado")
        
        input("Precione 'enter' para voltar!")
        print("-"*50, "\n")
        break

def equilibrio_de_tensao():

    while True:
        print("Seja bem vindo à verificação de equilíbrio de tensão")

        print("\n")

        voltar = False

        soma_tensoes = input("Qual é a soma das tensões de alimentação: ")
        soma_quedas_tensao = input("Qual á soma das quedas de tensão: ")

        valores = {
            "soma de tensões": soma_tensoes,
            "soma das quedas de tensão": soma_quedas_tensao
        }

        print("\n")

        for i in valores:
            try:
                valores[i] = float(valores[i])
            except:
                print(f"O valor '{valores[i]}' em {i} é inválido!")
                print("-"*50)
                voltar = True
                continue
        if voltar:
            continue

        diferenca = valores["soma de tensões"] - valores['soma das quedas de tensão']
        string_diferenca = str(diferenca)
        diferenca = float(string_diferenca[:len(string_diferenca)-1])

        if abs(diferenca) <= 0.01:
            print("Malha equilibrada")
        else:
            print("Malha não equilibrada")

        input("Precione 'enter' para voltar!")
        print("-"*50, "\n")
        break

print("Olá você está no painel de funções!")
print("\n")

while True:
        print("Digite apenas o número correspondente a função que deseja utilizar!")

        print("1 - Lei de Ohm")
        print("2 - Verificação de equilíbrio de corrente")
        print("3 - Verificação de equilíbrio de tensão")
        print("4 - Sair")
        op = input()

        print("-"*50, "\n")

        match op:
            case "1":
                lei_de_ohm()
                continue
            case "2":
                equilibrio_de_corrente()
                continue
            case "3":
                equilibrio_de_tensao()
                continue
            case "4":
                print("Obrigado por usar o painel de funções volte sempre!")
                break

        print("Opção inválida!")