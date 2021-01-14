peso = int(input(print("Qual é seu peso?")))
cm = int(input(print("Quantos centimestos de altura vc tem tem?")))
anos = int(input(print("Qual é sua idade?")))
basal = (66+(13.7 * peso)+(5.0 * cm)-(6.8 * anos))
kcal = basal+500+350+400
proteinas = 2*peso
carboidratos = 1*peso
gordura = 1*peso
print(f'voce precisa de {kcal} Kalorias \nProteinas:{proteinas} \nCarboidratos: {carboidratos} \nGordura: {gordura}')
print(f"kalorias para engordar.{basal*2}")