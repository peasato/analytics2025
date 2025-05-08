print("Hello, world!")
# retorna o número de iteráveis de um iteravel (tradução porca)
len("Hello, world!")
# retorna o tipo de objeto
type("Hello, world!")
# retorna atributos de classe __XXX__ e métodos
dir("Hello, world!")
# returna ajuda sobre determinado método
help("Hello, world!".upper)
# usando o método upper num objeto string
print("Hello, world!".upper())
greettings = "Hello, world!"
print(greettings)
type(greettings)
dir(greettings)
print(greettings.lower())
# abaixo é atribuído 5 a x
x = 5
type(x)
# x é iterável?
# DICA: use a build-in function len
len("x")
# abaixo é atribuído 5 a x
x = True
# qual o tipo da variável x?
type("x")
# x é iterável?
len("true")
# abaixo é atribuído [1,2,'pim',4,5,'pim'] a x
x = [1,2,'pim',4,5,'pim']
# qual o tipo da variável x?
type("x")
# quantos métodos tem x?
# abaixo é atribuído [1,2,'pim',4,5,'pim'] a x
x = [1,2,'pim',4,5,'pim']

# qual o tipo da variável x?
print("Tipo de x:", type(x))  # <class 'list'>

# quantos métodos tem x?
print("Quantidade de métodos/atributos de x:", len(dir(x)))

# imprima a ajuda sobre o anti-penúltimo método de x
metodos = dir(x)
print("Ajuda sobre o método:", metodos[-3])
help(getattr(x, metodos[-3]))

# use o método remove de x para remover os 'pim's
x.remove('pim')  # Remove a primeira ocorrência
x.remove('pim')  # Remove a segunda ocorrência

# imprima x
print("x após remoção dos 'pim':", x)  # [1, 2, 4, 5]

# x é iterável?
try:
    len(x)
    print("x é iterável: True")
except TypeError:
    print("x é iterável: False")
    x = {
    "alunos": ['ted','bia','bob'],
    "notas":[7,5,9],
    "universidade": "UFTM",
    "ano": 2015
}

# qual o tipo da variável x?
print("Tipo de x:", type(x))  # <class 'dict'>

# quantos métodos tem x?
print("Quantidade de métodos/atributos de x:", len(dir(x)))

# mostre a ajuda sobre o método keys
help(x.keys)

# imprima o retorno do método keys
print("x.keys():", x.keys())  # dict_keys(['alunos', 'notas', 'universidade', 'ano'])

# mostre a ajuda sobre o método values
help(x.values)

# imprima o retorno do método values
print("x.values():", x.values())  # dict_values([['ted', 'bia', 'bob'], [7, 5, 9], 'UFTM', 2015])

# x é iterável?
try:
    len(x)
    print("x é iterável: True")
except TypeError:
    print("x é iterável: False")
    x = "progresso"
x = x.replace("progr", "suc")
print(x)  # saída: sucesso
# Exercício 1: Cálculo de Receita Total
preco_A = 50
preco_B = 30
preco_C = 20

qtd_A = 100
qtd_B = 150
qtd_C = 200

receita_total = (preco_A * qtd_A) + (preco_B * qtd_B) + (preco_C * qtd_C)
print("Receita total do mês: R$", receita_total)

# Exercício 2: Conversão de Moeda
valor_em_reais = 105.00
taxa_cambio = 5.25

valor_em_dolares = round(valor_em_reais / taxa_cambio, 2)
print("Valor em dólares: US$", valor_em_dolares)

# Exercício 3: Análise de Crescimento de Vendas
vendas_janeiro = 120000.00
vendas_fevereiro = 150000.00

crescimento_percentual = ((vendas_fevereiro - vendas_janeiro) / vendas_janeiro) * 100
print("Crescimento percentual:", round(crescimento_percentual, 2), "%")

# Exercício 4: Cálculo de Lucro Bruto
receita = 120000.00
custos = 75000.00

lucro_bruto = receita - custos
margem_lucro_bruto = (lucro_bruto / receita) * 100
print("Lucro bruto: R$", lucro_bruto)
print("Margem de lucro bruto:", round(margem_lucro_bruto, 2), "%")

# Exercício 5: Média de Satisfação do Cliente
notas = [8, 9, 7, 10, 6]

media_satisfacao = round(sum(notas) / len(notas), 1)
print("Média de satisfação do cliente:", media_satisfacao)