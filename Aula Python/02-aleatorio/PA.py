termo = int(input("Digite o primeiro termo: "))
qtd = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

i = 0
while i < qtd:
    i = i + 1
    print("a{} ... {}".format(i, termo))
    termo = termo + razao
    