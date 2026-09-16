nota = int(input("Digite sua nota: "))

match nota: 
    case nota if nota < 5:
        print("Reprovado")
    case nota if nota == 5 | 6:
        print("Regular")
    case nota if nota == 7 | 8:
        print("Bom")
    case nota if nota == 9 | 10:
        print("Excelente")
