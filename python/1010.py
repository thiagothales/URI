codigo1, quantidade1, valor_peca1 = map(float, input().split(" ")) 
codigo2, quantidade2, valor_peca2 = map(float, input().split(" ")) 

total = (int(quantidade1)*float(valor_peca1)) + (int(quantidade2)* float(valor_peca2))

print("VALOR A PAGAR: R$ {0:.2f}".format(total))