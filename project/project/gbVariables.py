import PySimpleGUI as sg

sg.theme('LightBlue2')  # definition de la palette de couleur
row = col = 11

# affichage du menu
layout_menu = [[sg.Text('Welcome to my BattleShip !', justification='center', size=(50, 5), font=("Helvetica", 25), text_color='blue')],
               [sg.Button('Play', button_color=('white', 'red'), size=(5, 5)), sg.Button('Exit', button_color=('white', 'blue'), size=(5, 5))]]

# affichage tableau des scores a la fin
layout_end = [[sg.Text('Vous avez gagné ! Bravo', justification='center',
                       size=(30, 2), font=("Helvetica", 30), text_color='blue', key='EndText')],
              [sg.Text('Score Joueur', justification='center',
                       size=(30, 5), font=("Helvetica", 25), text_color='red', key='ScoreJ'), sg.Text('Score IA', justification='center',
                                                                                                      size=(30, 5), font=("Helvetica", 25), text_color='red', key='ScoreIA')]]

# affichage du jeu
layout_game = [
    [sg.Text(""*10), sg.Frame('Player', [[sg.Button(size=(4, 2), key=(i + 100, j + 100), pad=(0, 0), disabled=True) for i in range(col)] for j in range(row)]), sg.Text(""*20),
     sg.Frame('Opponent', [[sg.Button(size=(4, 2), key=(i + 200, j + 200), pad=(
         0, 0)) for i in range(col)] for j in range(row)]),
     sg.Text(""*10)],
    [sg.Button('Exit', button_color=('white', 'red'))]]

# affichage du menu de selection des batiments
layout_boats = [
    [sg.Text('Building positioning : hit 2 places to choice', justification='center',
             font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Porte Avion : 5 cases', justification='center',
             font=("Helvetica", 20), text_color='blue', key='Building')],
    [sg.Text(""*10), sg.Frame('Player', [[sg.Button(size=(4, 2), key=(i, j), pad=(0, 0))
                                          for i in range(col)] for j in range(row)]), sg.Text(""*20), ],
    [sg.Button('Exit', button_color=('white', 'red'))]]

layout = [[sg.Column(layout_menu, key='Menu', element_justification='center'), sg.Column(layout_boats, visible=False,
                                                                                         key='Start', element_justification='center'),
           sg.Column(layout_game, visible=False, key='Game'), sg.Column(layout_end, visible=False, key='End', element_justification='center')]]

window = sg.Window('Swapping the contents of a window',
                   layout)

# utilisé pour placement des batiments (compteur de touches)
nb_hit = 0

# nb de cases du batiment placé actuel
nb_cases = 5

# sens de placement du batiment (vertical / horizontal / diagonal)
sens = 0

# coordonnees batiments joueurs
coord_pa = []
coord_crois = []
coord_ct1 = []
coord_ct2 = []
coord_sm = []
first_ct = True

# coordonnes batiments ordinateur
coord_pa_ia = []
coord_crois_ia = []
coord_ct1_ia = []
coord_ct2_ia = []
coord_sm_ia = []

playerTurn = True

# score joueur et ia
score_player = [25]
score_ia = [25]

ia_shot = []

stock_ev = []
