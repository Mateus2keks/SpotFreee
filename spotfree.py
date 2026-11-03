import tkinter as tk
import os 
import time
import pygame

os.system("clear")
pygame.mixer.init()
pygame.init()
# -Busca a pasta com as musicas - o arquivo tem que estar no mesmo arquivo que que a pasta com as musicas !!
pasta_atual = os.path.dirname(os.path.abspath(__file__)) + "/musica"
os.makedirs(pasta_atual,exist_ok=True)

quantidade = os.listdir(pasta_atual)
musica_pausada = False
m = 0
volume = 0.0
n = -1
lista_musicas = []
# - Pega as musicas da pasta e guarda em uma lista-
for num in quantidade:
    n += 1
    lista_musicas.append(num)
    print(n,lista_musicas,"aaaa")
print("--- Testando com música na mesma pasta ---")

musica_atual = lista_musicas[m]

#janela e suas config
janela = tk.Tk()
janela.title("SpotFree")
janela.geometry("300x300")

# - Avisa quando a musica acaba pra tocar a proxima! -
FIM_DA_MUSICA = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(FIM_DA_MUSICA)

#Funçoes e comandos
# -Botao de play da musica-
def play():
    global musica_atual
    pygame.mixer.music.set_volume(volume)
    print(musica_atual)
    caminho_da_musica =  pasta_atual + f"/{musica_atual}" 

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(caminho_da_musica)
        print(f"'{caminho_da_musica}' carregada com sucesso!")
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Erro: Não encontrei o arquivo '{caminho_da_musica}' nesta pasta.")
        print("Verifique se o nome está idêntico (letras maiúsculas/minúsculas importam!).")
    print("Play")

# -Verifica quando acaba a musica para tocar a proxima !-
def verificar_eventos():
    global m
    global musica_atual
    global volume
    # -Volume-
    volume = volu.get() / 100
    pygame.mixer.music.set_volume(volume)
    esta_tocando = pygame.mixer.music.get_busy()
    for evento in pygame.event.get(): 
        if not esta_tocando and not musica_pausada:
            pygame.mixer.music.stop()
            print("musica acabou")
            m+=1
            if m < len(lista_musicas):
                musica_atual = lista_musicas[m]
                play()  # Toca a próxima música automaticamente
            else:
                print("Fim da playlist!")
            
    janela.after(100,lambda: verificar_eventos())

# -Botao de pause, Ele pausa no trexo da musica que esta tocando e nn volta pro inicio !!-
def pause():
    global musica_pausada

    if musica_pausada == True:
        print('b')
        pygame.mixer.music.unpause()
        print("dentro do if")
        musica_pausada = False
    else:
        print('a')
        pygame.mixer.music.pause()
        musica_pausada = True
    print("Pause")

# -Botao para pular para frente a musica !-
def pular_frente():
    global musica_atual
    global m
    m += 1
    pygame.mixer_music.pause
    musica_atual = lista_musicas[m]
    pygame.mixer_music.unpause()
    play()

# -Notao para pular para a atras a musica !-
def pular_atras():
    global musica_atual
    global m
    m -= 1
    pygame.mixer_music.pause
    musica_atual = lista_musicas[m]
    pygame.mixer_music.unpause()
    play()


# -Definiçoes e suas posiçoes-
frame_lista = tk.Frame(janela)
frame_lista.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

# -Lista com as musicas !-
frame_lista.rowconfigure(0, weight=1)
frame_lista.columnconfigure(0, weight=1)
caixa_lista = tk.Listbox(frame_lista, font=("Arial", 11), height=10)
caixa_lista.grid(row=0, column=0, sticky="nsew")

barra_rolagem = tk.Scrollbar(frame_lista, orient="vertical", command=caixa_lista.yview)
barra_rolagem.grid(row=0, column=1, sticky="ns") 
caixa_lista.config(yscrollcommand=barra_rolagem.set)

for num in lista_musicas:
    caixa_lista.insert("end", num)

# -Barra de volume-
volu = tk.Scale(
    orient="vertical",
    from_=0,
    to=100
)
volu.grid(column=1,row=1)


# -Botoes !-
# -Play-
botao_play = tk.Button(
    janela,
    text="Play,",
    command=play,
    bg="purple",
    fg="White",
    font=("Arial",13)
)
botao_play.grid(column=1,row=4)

# -Pular para frente-
botao_frente = tk.Button(
    janela,
    text="Proxima",
    command=lambda: pular_frente(),
    bg="black",
    fg="White",
    font=("Arial",13)
)
botao_frente.grid(column=1,row=3)

# -Pular para atras-
botao_atras = tk.Button(
    janela,
    text="Anterior",
    command=lambda: pular_atras(),
    bg="black",
    fg="White",
    font=("Arial",13)
)
botao_atras.grid(column=0,row=3)

# -Pause-
botao_pause = tk.Button(
    janela,
    text="Pause",
    command=pause,
    bg="red",
    fg="White",
    font=("Arial",13)
)
botao_pause.grid(column=0,row=4)

janela.after(100,lambda: verificar_eventos())
janela.mainloop()
