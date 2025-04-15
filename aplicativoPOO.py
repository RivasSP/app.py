class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Cantinho da Prosa'
restaurante_praca.categoria = 'Comida mineira'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurante_praca.ativo)
