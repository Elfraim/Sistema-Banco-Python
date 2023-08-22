menu ="""
[1]Depositar
[2]Sacar
[3]Extrato
[4]sair
"""
saldo =0
limite = 1000
extrato=""
numero_saques = 0
LIMITE_SAQUES = 10

 while True:
   
    opcao =input(menu)
     if opcao =="1":
          deposito = float(input("informe o valor depositado"))
        if valor > 01
     		  saldo == deposito
      		 extrato ==f"DEPOSITO: R${deposito:>2f}\n"
         else
        print("Operação falhou! informe um valor válido")
        
       	     elif opcao == "2"
        
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
  elif opcao=="3"
   print("     Extrato  ")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n Saldo R$ {saldo:.2f}")
    elif opcao =="4"
       break
