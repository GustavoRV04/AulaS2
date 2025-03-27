from datetime import datetime

data_nasc = input("Digite sua dt de nascimento (dd/mm/yyyy): ")
nascimento = datetime.strptime(data_nasc, "d%/%m/%Y")
hoje = datetime.today()
idade = hoje.year - nascimento.year

print(f"voce tem {idade} anos atualmente.")

if idade >= 18:
    print("Pode tirar a cnh")