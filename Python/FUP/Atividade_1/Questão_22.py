S = input("Digite uma string: ")
I = int(input("Digite o valor de I (indice inicial): "))
J = int(input("Dogite o valor de J(indice final): "))

if 0 <= I <= J < len(S):
    segmento = S[I:J+1]

    print(f"O seguimento S[{I} ... {J} é {segmento}]")

else:
    print("indices fornecidos são invalidos para a string fornecida")