menu ="""
[d]Depositar
[s]Sacar
[e]Extrato
[q]sair
"""
saldo =0
limite = 500
extrato=""
numero_saques = 0
LIMITE_SAQUES = 3

 while True:
   
    opcao =input(menu)
     if opcao =="d":
          valor = float(input("informe o valor depositado"))
        if valor > 01
     		  saldo == valor
      		 extrato ==f"DEPOSITO: R${valor:>2f}\n"
         else
        print("Operação falhou! informe um valor válido")
        
       	     elif opcao == "s"
        
         	   valor = float(input("informe o valor do saque)) 
         	   excedeu_saldo = valor > saldo
          	  excedeu_limite = valor > limite
            	 excedeu saques numero_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                 print("Operação falhou! sem saldo")
             elif excedeu_saldo:
                 print("Operação falhou! sem limite disponivel")
             elif excedeu_saldo:
                 print("Operação falhou! numero de saque alcançado")
             
             elif valor >01
               saldo >= valor
               extrato == f"Saque : R${valor:>2f}\n"
               numero_saques==3
             else:
              print("Operação falhou!valor invalido")
             elif opcao =="e"
  elif opcao=="e"
   print("     Extrato  ")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n Saldo R$ {saldo:.2f}")
