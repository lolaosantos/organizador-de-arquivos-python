import os
import shutil

# Caminho da pasta que você quer organizar
caminho = "c:/Users/Ramona7x/Downloads"

# Tipos de arquivos
tipos = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Documentos": [".docx", ".txt"]
}

# Criar pastas se não existirem
for pasta in tipos:
    caminho_pasta = os.path.join(caminho, pasta)
    if not os.path.exists(caminho_pasta):
        os.mkdir(caminho_pasta)

# Organizar arquivos
for arquivo in os.listdir(caminho):
    caminho_arquivo = os.path.join(caminho, arquivo)

    if os.path.isfile(caminho_arquivo):
        for pasta, extensoes in tipos.items():
            for extensao in extensoes:
                if arquivo.lower().endswith(extensao):
                    destino = os.path.join(caminho, pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"{arquivo} movido para {pasta}")

print("Organização concluída com sucesso!")                                                                                                                                                                                                                                                                                             