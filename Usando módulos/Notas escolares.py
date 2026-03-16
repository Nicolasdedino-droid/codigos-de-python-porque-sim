import sys
sys.path.append("/storage/emulated/0/Python/módulos")

from dinamic_mean import media

print("Digite as suas notas escolares!")

while True:
    nota = media()

    if nota < 6:
        print(f"Recuperação: {nota} pontos na média.")
        break
    elif nota > 10:
        print(f"Não pode haver nota maior que 10 (Sua pontuação foi {nota}). Repita o protocolo novamente.")
        continue
    
    elif nota > 6:
        print(f"Passou de ano: {nota} pontos na média.")
        break
