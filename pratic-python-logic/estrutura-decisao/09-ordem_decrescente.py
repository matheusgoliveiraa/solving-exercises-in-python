primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))

if (primeiro_numero < terceiro_numero):
    primeiro_numero, terceiro_numero = terceiro_numero, primeiro_numero
elif (primeiro_numero < segundo_numero):
    primeiro_numero, segundo_numero = segundo_numero, primeiro_numero
elif (segundo_numero < terceiro_numero):
    segundo_numero, terceiro_numero = terceiro_numero, segundo_numero

print(f'A ordem decrescente e {primeiro_numero}, {segundo_numero}, {terceiro_numero}')



