import gbVariables
from placeBuildings import *
from gameLogic import *


def event_ingame(event):
    if gbVariables.playerTurn == True:
        gbVariables.playerTurn = handle_player_turn(sg, event, gbVariables.window, gbVariables.coord_pa_ia, gbVariables.coord_crois_ia,
                                                    gbVariables.coord_ct1_ia, gbVariables.coord_ct2_ia, gbVariables.coord_sm_ia, gbVariables.score_player)
        if gbVariables.playerTurn == False:
            while gbVariables.playerTurn == False:
                if score_isNull(gbVariables.score_ia) == True or score_isNull(gbVariables.score_player) == True or all_buildings_sink(gbVariables.coord_pa, gbVariables.coord_crois, gbVariables.coord_ct1, gbVariables.coord_ct2, gbVariables.coord_sm) == True:
                    gbVariables.window['Game'].update(visible=False)
                    gbVariables.window['End'].update(visible=True)
                    break
                gbVariables.playerTurn = handle_ia_turn(gbVariables.window, gbVariables.coord_pa, gbVariables.coord_crois,
                                                        gbVariables.coord_ct1, gbVariables.coord_ct2, gbVariables.coord_sm, gbVariables.ia_shot, gbVariables.score_ia, gbVariables.score_player)
    if score_isNull(gbVariables.score_ia) == True or score_isNull(gbVariables.score_player) == True or all_buildings_sink(gbVariables.coord_pa_ia, gbVariables.coord_crois_ia, gbVariables.coord_ct1_ia, gbVariables.coord_ct2_ia, gbVariables.coord_sm_ia) == True or gbVariables.window['End'].visible == True:
        gbVariables.window['Game'].update(visible=False)
        gbVariables.window['End'].update(visible=True)
        handle_score_page()


def event_play():
    gbVariables.window['Menu'].update(visible=False)
    gbVariables.window['Start'].update(visible=True)
    liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for k in range(1, 11):
        gbVariables.window[(0, k)].update(k)
        for j in range(k+1):
            gbVariables.window[(k, 0)].update(liste[j - 1])
    for i in range(0, 11):
        gbVariables.window[(i, 0)].update(
            button_color=('blue', 'lightblue'))
        gbVariables.window[(0, i)].update(
            button_color=('blue', 'lightblue'))


def event_start_game(event):
    if gbVariables.nb_hit == 1:
        gbVariables.sens = verify_building_pos(event)
        if gbVariables.sens == 404:
            return False
    gbVariables.stock_ev = event
    gbVariables.nb_hit = handle_hitMap(event)
    if gbVariables.nb_hit == 2:
        if gbVariables.nb_cases == 5:
            gbVariables.coord_pa = display_building(event)
            if gbVariables.coord_pa == None:
                gbVariables.nb_hit = 0
                gbVariables.coord_pa = []
                return False
            gbVariables.nb_cases = 4
            gbVariables.window['Building'].update('Croiseur: 4 cases')
        elif gbVariables.nb_cases == 4:
            gbVariables.coord_crois = display_building(event)
            if gbVariables.coord_crois == None:
                gbVariables.nb_hit = 0
                gbVariables.coord_crois = []
                return False
            gbVariables.nb_cases = 3
            gbVariables.window['Building'].update(
                "Torpilleur: 3 cases")
            gbVariables.first_ct = True
        elif gbVariables.nb_cases == 3:
            if gbVariables.first_ct == True:
                gbVariables.coord_ct1 = display_building(event)
                if gbVariables.coord_ct1 == None:
                    gbVariables.nb_hit = 0
                    gbVariables.coord_ct1 = []
                    return False
                gbVariables.first_ct = False
                gbVariables.window['Building'].update(
                    'Torpilleur: 3 cases')
            else:
                gbVariables.coord_ct2 = display_building(event)
                if gbVariables.coord_ct2 == None:
                    gbVariables.nb_hit = 0
                    gbVariables.coord_ct2 = []
                    return False
                gbVariables.first_ct = True
                gbVariables.window['Building'].update(
                    'Sous marin : 2 cases')
                gbVariables.nb_cases = 2
        else:
            gbVariables.coord_sm = display_building(event)
            if gbVariables.coord_sm == None:
                gbVariables.nb_hit = 0
                gbVariables.coord_sm = []
                return False
            gbVariables.window['Start'].update(visible=False)
            gbVariables.window['Game'].update(visible=True)
            place_buildings_ia()
            place_buildings_on_map_player()
            place_buildings_on_map_ia()
            return False
    return True
