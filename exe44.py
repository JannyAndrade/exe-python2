print('\033[1;35mLOJAS GUANABARA\033[m')

compras = float(input('Preço das compras: R$'))
print('''\033[1;32mESCOLHA A FORMA DE PAGAMENTO
[ 1 ] a vista Dinheiro / Cheque 
[ 2 ] a vista Cartão  
[ 3 ] 2x no Cartão  
[ 4 ] 3x ou mais no Cartão\033[m''')
opcao = int(input('Qual sua opções? '))


if opcao == 1:
    desconto = (compras * 10) / 100
    valor_final = compras - desconto
    print('Sua compra de R${} vai custar R${} valor final.'.format(compras, valor_final))
elif opcao == 2:
    desconto = (compras * 5) / 100
    valor_final = compras - desconto
    print('Sua compra de R${} vai sair por R${} valor final.'.format(compras, valor_final))
elif opcao == 3:
    valor = compras / 2
    print('Sua compra  saíra  no valor normal de R${} com duas parcelas de R${}'.format(compras, valor))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas ? '))
    juros = compras * 20 / 100
    valor_final = compras + juros
    valor = compras / parcelas
    print('Sua compra de R${}  saíra  por R${} com {} parcelas de R${}'.format(compras, valor_final, parcelas, valor))
else:
    print('OPÇÃO INVÁLIDA')
























