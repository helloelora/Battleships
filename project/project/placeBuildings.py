import random
import gbVariables


def handle_hitMap(event):
    if event[0] == 0 or event[1] == 0:
        return gbVariables.nb_hit
    if gbVariables.nb_hit == 0:
        for z in gbVariables.coord_pa:
            if event == z or (event[0] + 1, event[1]) == z or (event[0] - 1, event[1]) == z or (event[0], event[1] + 1) == z or (event[0], event[1] - 1) == z or (event[0] - 1, event[1] - 1) == z or (event[0] + 1, event[1] - 1) == z or (event[0] + 1, event[1] + 1) == z or (event[0] - 1, event[1] + 1) == z:
                gbVariables.sg.Popup('Les bâtiments ne doivent pas se toucher',
                                     keep_on_top=True)
                return gbVariables.nb_hit
        for k in gbVariables.coord_crois:
            if event == k or (event[0] + 1, event[1]) == k or (event[0] - 1, event[1]) == k or (event[0], event[1] + 1) == k or (event[0], event[1] - 1) == k or (event[0] - 1, event[1] - 1) == k or (event[0] + 1, event[1] - 1) == k or (event[0] + 1, event[1] + 1) == k or (event[0] - 1, event[1] + 1) == k:
                gbVariables.sg.Popup('Les bâtiments ne doivent pas se toucher',
                                     keep_on_top=True)
                return gbVariables.nb_hit
        for a in gbVariables.coord_ct1:
            if event == a or (event[0] + 1, event[1]) == a or (event[0] - 1, event[1]) == a or (event[0], event[1] + 1) == a or (event[0], event[1] - 1) == a or (event[0] - 1, event[1] - 1) == a or (event[0] + 1, event[1] - 1) == a or (event[0] + 1, event[1] + 1) == a or (event[0] - 1, event[1] + 1) == a:
                gbVariables.sg.Popup('Les bâtiments ne doivent pas se toucher',
                                     keep_on_top=True)
                return gbVariables.nb_hit
        for b in gbVariables.coord_ct2:
            if event == b or (event[0] + 1, event[1]) == b or (event[0] - 1, event[1]) == b or (event[0], event[1] + 1) == b or (event[0], event[1] - 1) == b or (event[0] - 1, event[1] - 1) == b or (event[0] + 1, event[1] - 1) == b or (event[0] + 1, event[1] + 1) == b or (event[0] - 1, event[1] + 1) == b:
                gbVariables.sg.Popup('Les bâtiments ne doivent pas se toucher',
                                     keep_on_top=True)
                return gbVariables.nb_hit
        for c in gbVariables.coord_sm:
            if event == c or (event[0] + 1, event[1]) == c or (event[0] - 1, event[1]) == c or (event[0], event[1] + 1) == c or (event[0], event[1] - 1) == c or (event[0] - 1, event[1] - 1) == c or (event[0] + 1, event[1] - 1) == c or (event[0] + 1, event[1] + 1) == c or (event[0] - 1, event[1] + 1) == c:
                gbVariables.sg.Popup('Les bâtiments ne doivent pas se toucher',
                                     keep_on_top=True)
                return gbVariables.nb_hit
    gbVariables.window[event].update(
        button_color=change_color(gbVariables.nb_cases))
    gbVariables.nb_hit += 1
    return gbVariables.nb_hit


def verify_building_pos(event):
    if event[0] - gbVariables.stock_ev[0] == 1:
        if event[0] + (gbVariables.nb_cases - 2) > 10:
            gbVariables.sg.Popup('Mauvaise position', keep_on_top=True)
            return 404
        gbVariables.sens = -1
    elif event[0] - gbVariables.stock_ev[0] == -1:
        if event[0] - (gbVariables.nb_cases - 2) < 1:
            gbVariables.sg.Popup('Mauvaise position', keep_on_top=True)
            return 404
        gbVariables.sens = -2
    elif event[1] - gbVariables.stock_ev[1] == 1:
        if event[1] + (gbVariables.nb_cases - 2) > 10:
            gbVariables.sg.Popup('Mauvaise position', keep_on_top=True)
            return 404
        gbVariables.sens = 1
    elif event[1] - gbVariables.stock_ev[1] == -1:
        if event[1] - (gbVariables.nb_cases - 2) < 1:
            gbVariables.sg.Popup('Mauvaise position', keep_on_top=True)
            return 404
        gbVariables.sens = 2
    else:
        gbVariables.sg.Popup(
            'Les 2 points doivent etre collés', keep_on_top=True)
        return 404
    return gbVariables.sens


def verify_ifOverlap(coord):
    for x in coord:
        for z in gbVariables.coord_pa:
            if x == z or (x[0] + 1, x[1]) == z or (x[0] - 1, x[1]) == z or (x[0], x[1] + 1) == z or (x[0], x[1] - 1) == z or (x[0] - 1, x[1] - 1) == z or (x[0] + 1, x[1] - 1) == z or (x[0] + 1, x[1] + 1) == z or (x[0] - 1, x[1] + 1) == z:
                return False
        for k in gbVariables.coord_crois:
            if x == k or (x[0] + 1, x[1]) == k or (x[0] - 1, x[1]) == k or (x[0], x[1] + 1) == k or (x[0], x[1] - 1) == k or (x[0] - 1, x[1] - 1) == k or (x[0] + 1, x[1] - 1) == k or (x[0] + 1, x[1] + 1) == k or (x[0] - 1, x[1] + 1) == k:
                return False
        for a in gbVariables.coord_ct1:
            if x == a or (x[0] + 1, x[1]) == a or (x[0] - 1, x[1]) == a or (x[0], x[1] + 1) == a or (x[0], x[1] - 1) == a or (x[0] - 1, x[1] - 1) == a or (x[0] + 1, x[1] - 1) == a or (x[0] + 1, x[1] + 1) == a or (x[0] - 1, x[1] + 1) == a:
                return False
        for b in gbVariables.coord_ct2:
            if x == b or (x[0] + 1, x[1]) == b or (x[0] - 1, x[1]) == b or (x[0], x[1] + 1) == b or (x[0], x[1] - 1) == b or (x[0] - 1, x[1] - 1) == b or (x[0] + 1, x[1] - 1) == b or (x[0] + 1, x[1] + 1) == b or (x[0] - 1, x[1] + 1) == b:
                return False
        for c in gbVariables.coord_sm:
            if x == c or (x[0] + 1, x[1]) == c or (x[0] - 1, x[1]) == c or (x[0], x[1] + 1) == c or (x[0], x[1] - 1) == c or (x[0] - 1, x[1] - 1) == c or (x[0] + 1, x[1] - 1) == c or (x[0] + 1, x[1] + 1) == c or (x[0] - 1, x[1] + 1) == c:
                return False
    return True


def change_color(nb_cases):
    if nb_cases == 5:
        color = ('black')
    if nb_cases == 4:
        color = ('yellow')
    if nb_cases == 3:
        color = ('green')
    if nb_cases == 2:
        color = ('purple')
    return color


def display_building(event):
    coord = []
    if gbVariables.sens == -1:
        coord.append((gbVariables.stock_ev[0] - 1, event[1]))
        for i in range(event[0], event[0] + (gbVariables.nb_cases - 1)):
            coord.append((i, event[1]))
        if verify_ifOverlap(coord) == False:
            gbVariables.sg.Popup(
                'Les bâtiments ne doivent pas se toucher', keep_on_top=True)
            gbVariables.window[(event[0], event[1])].update(
                button_color=('#FFFFFF', '#7186C7'))
            gbVariables.window[(event[0] - 1, event[1])
                               ].update(button_color=('#FFFFFF', '#7186C7'))
            return None
        for i in range(event[0], event[0] + (gbVariables.nb_cases - 1)):
            gbVariables.window[(i, event[1])].update(
                button_color=change_color(gbVariables.nb_cases))

    if gbVariables.sens == -2:
        coord.append((gbVariables.stock_ev[0] + 1, event[1]))
        for i in range(event[0], event[0] - (gbVariables.nb_cases - 1), -1):
            coord.append((i, event[1]))
        if verify_ifOverlap(coord) == False:
            gbVariables.sg.Popup(
                'Les bâtiments ne doivent pas se toucher', keep_on_top=True)
            gbVariables.window[(event[0], event[1])].update(
                button_color=('#FFFFFF', '#7186C7'))
            gbVariables.window[(event[0] + 1, event[1])
                               ].update(button_color=('#FFFFFF', '#7186C7'))
            return None
        for i in range(event[0], event[0] - (gbVariables.nb_cases - 1), -1):
            gbVariables.window[(i, event[1])].update(
                button_color=change_color(gbVariables.nb_cases))

    if gbVariables.sens == 1:
        coord.append((event[0], event[1] - 1))
        for i in range(event[1], event[1] + (gbVariables.nb_cases - 1)):
            coord.append((event[0], i))
        if verify_ifOverlap(coord) == False:
            gbVariables.sg.Popup(
                'Les bâtiments ne doivent pas se toucher', keep_on_top=True)
            gbVariables.window[(event[0], event[1])].update(
                button_color=('#FFFFFF', '#7186C7'))
            gbVariables.window[(event[0], event[1] - 1)
                               ].update(button_color=('#FFFFFF', '#7186C7'))
            return None
        for i in range(event[1], event[1] + (gbVariables.nb_cases - 1)):
            gbVariables.window[(event[0], i)].update(
                button_color=change_color(gbVariables.nb_cases))

    if gbVariables.sens == 2:
        coord.append((event[0], event[1] + 1))
        for i in range(event[1], event[1] - (gbVariables.nb_cases - 1), -1):
            coord.append((event[0], i))
        if verify_ifOverlap(coord) == False:
            gbVariables.sg.Popup(
                'Les bâtiments ne doivent pas se toucher', keep_on_top=True)
            gbVariables.window[(event[0], event[1])].update(
                button_color=('#FFFFFF', '#7186C7'))
            gbVariables.window[(event[0], event[1] + 1)
                               ].update(button_color=('#FFFFFF', '#7186C7'))
            return None
        for i in range(event[1], event[1] - (gbVariables.nb_cases - 1), -1):
            gbVariables.window[(event[0], i)].update(
                button_color=change_color(gbVariables.nb_cases))
    gbVariables.nb_hit = 0
    return coord


def ia_verify_horizontal_right(x, y, coord):
    for i in range(x, x + gbVariables.nb_cases[0]):
        coord.append((i, y))
    if verify_ifOverlap(coord) == True:
        if gbVariables.nb_cases[0] == 5:
            for i in range(x, x + gbVariables.nb_cases[0]):
                gbVariables.coord_pa_ia.append((i, y))
            gbVariables.nb_cases[0] = 4
            return True
        if gbVariables.nb_cases[0] == 4:
            for i in range(x, x + gbVariables.nb_cases[0]):
                gbVariables.coord_crois_ia.append((i, y))
            gbVariables.nb_cases[0] = 3
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == True:
            for i in range(x, x + gbVariables.nb_cases[0]):
                gbVariables.coord_ct1_ia.append((i, y))
            gbVariables.first_ct[0] = False
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == False:
            for i in range(x, x + gbVariables.nb_cases[0]):
                gbVariables.coord_ct2_ia.append((i, y))
            gbVariables.first_ct[0] = True
            gbVariables.nb_cases[0] = 2
            return True
        if gbVariables.nb_cases[0] == 2:
            for i in range(x, x + gbVariables.nb_cases[0]):
                gbVariables.coord_sm_ia.append((i, y))
            gbVariables.nb_cases[0] = 0
            return True
    return False


def ia_verify_horizontal_left(x, y, coord):
    for i in range(x, x - gbVariables.nb_cases[0], -1):
        coord.append((i, y))
    if verify_ifOverlap(coord) == True:
        if gbVariables.nb_cases[0] == 5:
            for i in range(x, x - gbVariables.nb_cases[0], -1):
                gbVariables.coord_pa_ia.append((i, y))
            gbVariables.nb_cases[0] = 4
            return True
        if gbVariables.nb_cases[0] == 4:
            for i in range(x, x - gbVariables.nb_cases[0], -1):
                gbVariables.coord_crois_ia.append((i, y))
            gbVariables.nb_cases[0] = 3
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == True:
            for i in range(x, x - gbVariables.nb_cases[0], -1):
                gbVariables.coord_ct1_ia.append((i, y))
            gbVariables.first_ct[0] = False
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == False:
            for i in range(x, x - gbVariables.nb_cases[0], -1):
                gbVariables.coord_ct2_ia.append((i, y))
            gbVariables.first_ct[0] = True
            gbVariables.nb_cases[0] = 2
            return True
        if gbVariables.nb_cases[0] == 2:
            for i in range(x, x - gbVariables.nb_cases[0], -1):
                gbVariables.coord_sm_ia.append((i, y))
            gbVariables.nb_cases[0] = 0
            return True
    return False


def ia_verify_vertical_down(x, y, coord):
    for i in range(y, y + gbVariables.nb_cases[0]):
        coord.append((x, i))
    if verify_ifOverlap(coord) == True:
        if gbVariables.nb_cases[0] == 5:
            for i in range(y, y + gbVariables.nb_cases[0]):
                gbVariables.coord_pa_ia.append((x, i))
            gbVariables.nb_cases[0] = 4
            return True
        if gbVariables.nb_cases[0] == 4:
            for i in range(y, y + gbVariables.nb_cases[0]):
                gbVariables.coord_crois_ia.append((x, i))
            gbVariables.nb_cases[0] = 3
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == True:
            for i in range(y, y + gbVariables.nb_cases[0]):
                gbVariables.coord_ct1_ia.append((x, i))
            gbVariables.first_ct[0] = False
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == False:
            for i in range(y, y + gbVariables.nb_cases[0]):
                gbVariables.coord_ct2_ia.append((x, i))
            gbVariables.first_ct[0] = True
            gbVariables.nb_cases[0] = 2
            return True
        if gbVariables.nb_cases[0] == 2:
            for i in range(y, y + gbVariables.nb_cases[0]):
                gbVariables.coord_sm_ia.append((x, i))
            gbVariables.nb_cases[0] = 0
            return True
    return False


def ia_verify_vertical_up(x, y, coord):
    for i in range(y, y - gbVariables.nb_cases[0], -1):
        coord.append((x, i))
    if verify_ifOverlap(coord) == True:
        if gbVariables.nb_cases[0] == 5:
            for i in range(y, y - gbVariables.nb_cases[0], -1):
                gbVariables.coord_pa_ia.append((x, i))
            gbVariables.nb_cases[0] = 4
            return True
        if gbVariables.nb_cases[0] == 4:
            for i in range(y, y - gbVariables.nb_cases[0], -1):
                gbVariables.coord_crois_ia.append((x, i))
            gbVariables.nb_cases[0] = 3
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == True:
            for i in range(y, y - gbVariables.nb_cases[0], -1):
                gbVariables.coord_ct1_ia.append((x, i))
            gbVariables.first_ct[0] = False
            return True
        if gbVariables.nb_cases[0] == 3 and gbVariables.first_ct[0] == False:
            for i in range(y, y - gbVariables.nb_cases[0], -1):
                gbVariables.coord_ct2_ia.append((x, i))
            gbVariables.first_ct[0] = True
            gbVariables.nb_cases[0] = 2
            return True
        if gbVariables.nb_cases[0] == 2:
            for i in range(y, y - gbVariables.nb_cases[0], -1):
                gbVariables.coord_sm_ia.append((x, i))
            gbVariables.nb_cases[0] = 0
            return True
    return False


def place_buildings_ia():
    gbVariables.nb_cases = [5]
    gbVariables.first_ct = [True]
    while gbVariables.nb_cases[0] != 0:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if x + (gbVariables.nb_cases[0] - 1) <= 10:
            coord = []
            if ia_verify_horizontal_right(x, y, coord) == True:
                continue
        if x - (gbVariables.nb_cases[0] - 1) >= 1:
            coord = []
            if ia_verify_horizontal_left(x, y,  coord) == True:
                continue
        if y + (gbVariables.nb_cases[0] - 1) <= 10:
            coord = []
            if ia_verify_vertical_down(x, y, coord) == True:
                continue
        if y - (gbVariables.nb_cases[0] - 1) >= 1:
            coord = []
            if ia_verify_vertical_up(x, y, coord) == True:
                continue


def place_buildings_on_map_player():
    liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for k in range(1, 11):
        gbVariables.window[(100, k + 100)].update(k)
        for j in range(k+1):
            gbVariables.window[(k + 100, 100)].update(liste[j - 1])
    for i in range(0, 11):
        gbVariables.window[(i + 100, 100)
                           ].update(button_color=('blue', 'lightblue'))
        gbVariables.window[(100, i + 100)
                           ].update(button_color=('blue', 'lightblue'))
    for coord in gbVariables.coord_pa:
        gbVariables.window[(coord[0] + 100, coord[1] + 100)].update(
            button_color=change_color(5))
    for coord in gbVariables.coord_crois:
        gbVariables.window[(coord[0] + 100, coord[1] + 100)].update(
            button_color=change_color(4))
    for coord in gbVariables.coord_ct1:
        gbVariables.window[(coord[0] + 100, coord[1] + 100)].update(
            button_color=change_color(3))
    for coord in gbVariables.coord_ct2:
        gbVariables.window[(coord[0] + 100, coord[1] + 100)].update(
            button_color=change_color(3))
    for coord in gbVariables.coord_sm:
        gbVariables.window[(coord[0] + 100, coord[1] + 100)].update(
            button_color=change_color(2))


def place_buildings_on_map_ia():
    liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for k in range(1, 11):
        gbVariables.window[(200, k + 200)].update(k)
        for j in range(k+1):
            gbVariables.window[(k + 200, 200)].update(liste[j - 1])
    for i in range(0, 11):
        gbVariables.window[(i + 200, 200)
                           ].update(button_color=('blue', 'lightblue'))
        gbVariables.window[(200, i + 200)
                           ].update(button_color=('blue', 'lightblue'))


def handle_score_page():
    if gbVariables.score_ia[0] > gbVariables.score_player[0]:
        end_txt = "L'ordinateur a gagné! Vous ferez mieux la prochaine fois!"
    else:
        end_txt = "Vous avez gagné! Bravo!"
    gbVariables.window['EndText'].update(end_txt)
    gbVariables.window['ScoreJ'].update(
        "Score joueur: " + str(gbVariables.score_player[0]))
    gbVariables.window['ScoreIA'].update(
        "Score IA: " + str(gbVariables.score_ia[0]))
