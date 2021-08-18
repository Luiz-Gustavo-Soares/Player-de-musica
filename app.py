import PySimpleGUI as sg
import os
import uteis.gerenciador_son


def md_display(name):  # imprime o nome da musica no visor ou auguma instrução
    nome, extecao = os.path.splitext(name)
    nome = os.path.basename(nome)
    window['name_music'].update(nome)


def md_icon(name_icon, new_icon1, new_icon2, on_off):
    if on_off:
        window[name_icon].update(filename=new_icon2)
    else:
        window[name_icon].update(filename=new_icon1)


cor = '#A70CB5'
icons = {'play_plause': './icon/play_pause.png', 'prox': './icon/prox.png', 'back': './icon/back.png',
         'img': './icon/disco.png', 'aleatorio': './icon/music_aleatorio.png',
         'aleatori_off': './icon/music_aleatorio_off.png', 'arquivo': './icon/icon_arquivo.png',
         'logo': './icon/logodisco.ico'}


music = uteis.gerenciador_son.musica()

sg.theme('DarkBlack')

layout = [[sg.Image(filename=icons['arquivo'], key='file', background_color='black', pad=(10, 0), enable_events=True),
           sg.Image(filename=icons['aleatori_off'], key='aleatorio', enable_events=True, tooltip='Aleatório on/off'),
           sg.Slider(key='volume', range=(1, 100), default_value=75, size=(10, 4),
                     orientation='h', background_color=cor,
                     trough_color='black', disable_number_display=True, enable_events=True,
                     border_width=1, pad=((55, 0), (0, 0)), tooltip='Volume')],
          [sg.Image(filename=icons['img'], background_color='black', pad=((24, 0), (40, 20)), size=(200, 200))],
          [sg.Text('', key='name_music', background_color='black', text_color=cor,
                   font=('', 10), pad=(28, 0), size=(24, 1), justification='center')],
          [sg.Canvas(size=(200, 1), pad=(22, 0), background_color=cor)],
          [sg.Image(filename=icons['back'], enable_events=True, key='back', background_color='black', pad=(12, 0)),
           sg.Image(filename=icons['play_plause'], enable_events=True, key='play', background_color='black'),
           sg.Image(filename=icons['prox'], enable_events=True, key='prox', background_color='black')]]


window = sg.Window(title='Player Música', layout=layout, background_color='black', icon=icons['img'])
while True:
    event, values = window.read(timeout=True)

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'play':
        md_display(music.play())

    elif event == 'prox':
        md_display(music.prox_music(True))

    elif event == 'back':
        md_display(music.prox_music(False))

    if event == 'volume':
        music.volume(float(values['volume']))

    if event == 'aleatorio':
        md_icon('aleatorio', icons['aleatori_off'], icons['aleatorio'], music.aleatorio())

    if event == 'file':
        pasta = sg.popup_get_folder('Selecione a pasta contendo as músicas', icon=icons['arquivo'])
        try:
            music.limpar_reproducao()
            for diretorio, subpasta, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    music.incerir_musicas(diretorio + '/' + arquivo, arquivo)
            md_display(music.play())
        except:
            md_display('Pasta não selecionada')

    if music.parado():
        md_display(music.prox_music(True))
