from event_game import *


def main():
    while True:
        event, values = gbVariables.window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Play':
            gbVariables.stock_ev = event
            event_play()
        if gbVariables.window['Start'].visible == True and isinstance(event[0], int):
            if event_start_game(event) == False:
                continue
        if gbVariables.window['Game'].visible == True and isinstance(event[0], int):
            event_ingame(event)
    gbVariables.window.close()


if __name__ == "__main__":
    main()
