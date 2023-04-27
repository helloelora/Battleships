import random
import PySimpleGUI as sg


def all_buildings_sink(coord_pa, coord_crois, coord_ct1, coord_ct2, coord_sm):
    if len(coord_pa) == 10 and len(coord_crois) == 8 and len(coord_ct1) == 6 and len(coord_ct2) == 6 and len(coord_sm) == 4:
        return True
    return False


def score_isNull(score):
    if score[0] <= 0:
        return True
    return False


def handle_ia_turn(window, coord_pa, coord_crois, coord_ct1, coord_ct2, coord_sm, ia_shot, score_ia, score_player):
    endTurn = False
    while endTurn == False:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if (x, y) in ia_shot:
            continue
        liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        coord = "L'adversaire tire en " + liste[x - 1] + str(y)
        event, values = sg.Window(coord, [[sg.Text('Select one->'), sg.Listbox(['Raté', 'Touché', 'Coulé'], size=(30, 3), key='LB')],
                                          [sg.Button('Ok')]]).read(close=True)
        if event == 'Ok':
            if values["LB"][0] == "Raté":
                if (x, y) in coord_pa or (x, y) in coord_crois or (x, y) in coord_ct1 or (x, y) in coord_ct2 or (x, y) in coord_sm:
                    sg.popup('Vous avez triché', keep_on_top=True)
                    score_player[0] -= 10
                    score_isNull(score_player)
                    return False
                sg.popup('A votre tour de jouer', keep_on_top=True)
                window[(x + 100, y + 100)].update(button_color=('blue'))
                ia_shot.append((x, y))
                score_ia[0] -= 1
                return True
            if values["LB"][0] == "Touché":
                if (x, y) in coord_sm:
                    if len(coord_sm) == 3:
                        sg.popup('Vous avez triché',
                                 keep_on_top=True)
                        score_player[0] -= 10
                        return False
                    coord_sm.append((x, y, 1))
                if (x, y) in coord_pa:
                    if len(coord_pa) == 9:
                        sg.popup('Vous avez triché',
                                 keep_on_top=True)
                        score_player[0] -= 10
                        return False
                    coord_pa.append((x, y, 1))
                if (x, y) in coord_crois:
                    if len(coord_crois) == 7:
                        sg.popup('Vous avez triché',
                                 keep_on_top=True)
                        score_player[0] -= 10
                        return False
                    coord_crois.append((x, y, 1))
                if (x, y) in coord_ct1:
                    if len(coord_ct1) == 5:
                        sg.popup('Vous avez triché',
                                 keep_on_top=True)
                        score_player[0] -= 10
                        return False
                    coord_ct1.append((x, y, 1))
                if (x, y) in coord_ct2:
                    if len(coord_ct2) == 5:
                        sg.popup('Vous avez triché',
                                 keep_on_top=True)
                        score_player[0] -= 10
                        return False
                    coord_ct2.append((x, y, 1))
                sg.popup('Votre Adversaire a touché, il garde la main',
                         keep_on_top=True)
                ia_shot.append((x, y))
                window[(x + 100, y + 100)].update(button_color=('red'))
                return False
            if values["LB"][0] == "Coulé":
                sg.popup('Votre Adversaire a coulé, il garde la main',
                         keep_on_top=True)
                score_ia[0] -= 1
                if (x, y) in coord_sm:
                    coord_sm.append((x, y, 1))
                    score_ia[0] += 4
                if (x, y) in coord_pa:
                    coord_pa.append((x, y, 1))
                    score_ia[0] += 10
                if (x, y) in coord_crois:
                    coord_crois.append((x, y, 1))
                    score_ia[0] += 8
                if (x, y) in coord_ct1:
                    coord_ct1.append((x, y, 1))
                    score_ia[0] += 6
                if (x, y) in coord_ct2:
                    coord_ct2.append((x, y, 1))
                    score_ia[0] += 6
                ia_shot.append((x, y))
                window[(x + 100, y + 100)].update(button_color=('red'))
                return False


def handle_player_turn(sg, event, window, coord_pa_ia, coord_crois_ia, coord_ct1_ia, coord_ct2_ia, coord_sm_ia, score_player):
    score_player[0] -= 1
    if (event[0] - 200, event[1] - 200) in coord_sm_ia:
        window[event].update(button_color=('red'))
        if (event[0] - 200, event[1] - 200, 1) not in coord_sm_ia:
            coord_sm_ia.append((event[0] - 200, event[1] - 200, 1))
        if len(coord_sm_ia) == 4:
            sg.popup('Vous avez fait coulé le sous marin adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 4
        else:
            sg.popup('Vous avez touché un bâtiment adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 1
        return True
    if (event[0] - 200, event[1] - 200) in coord_pa_ia:
        window[event].update(button_color=('red'))
        if (event[0] - 200, event[1] - 200, 1) not in coord_pa_ia:
            coord_pa_ia.append((event[0] - 200, event[1] - 200, 1))
        if len(coord_pa_ia) == 10:
            sg.popup('Vous avez fait coulé le porte avion adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 10
        else:
            sg.popup('Vous avez touché un bâtiment adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 1
        return True
    if (event[0] - 200, event[1] - 200) in coord_crois_ia:
        window[event].update(button_color=('red'))
        if (event[0] - 200, event[1] - 200, 1) not in coord_crois_ia:
            coord_crois_ia.append((event[0] - 200, event[1] - 200, 1))
        if len(coord_crois_ia) == 8:
            sg.popup('Vous avez fait coulé le croiseur adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 8
        else:
            sg.popup('Vous avez touché un bâtiment adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 1
        return True
    if (event[0] - 200, event[1] - 200) in coord_ct1_ia:
        window[event].update(button_color=('red'))
        if (event[0] - 200, event[1] - 200, 1) not in coord_ct1_ia:
            coord_ct1_ia.append((event[0] - 200, event[1] - 200, 1))
        if len(coord_ct1_ia) == 6:
            sg.popup('Vous avez fait coulé un des ct adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 6
        else:
            sg.popup('Vous avez touché un bâtiment adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 1
        return True
    if (event[0] - 200, event[1] - 200) in coord_ct2_ia:
        window[event].update(button_color=('red'))
        if (event[0] - 200, event[1] - 200, 1) not in coord_ct2_ia:
            coord_ct2_ia.append((event[0] - 200, event[1] - 200, 1))
        if len(coord_ct2_ia) == 6:
            sg.popup('Vous avez fait coulé un des ct adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 6
        else:
            sg.popup('Vous avez touché un bâtiment adverse!\nVous Gardez la main!',
                     keep_on_top=True, auto_close=True, auto_close_duration=2)
            score_player[0] += 1
        return True
    sg.popup("Vous avez raté!\nTour de l'IA",
             keep_on_top=True, auto_close=True, auto_close_duration=2)
    window[event].update(button_color=('blue'))
    return False
