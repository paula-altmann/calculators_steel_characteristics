from console_variables_getters import get_float_value, get_int_value, get_str_value
import sys


print("Wprowadź poniższe dane aby wyliczyć nośność przekroju na rozciąganie lub warunek nośności. W zapisie dziesiętnym"
      " użyj kropki.")
while True:
    A = get_float_value("Podaj czynne pole przekroju [cm2] A = ")
    if A > 0:
        break
    else:
        print("Podane pole przekroju jest niedodatnie, wpisz poprawną wartość.")
while True:
    fy = get_int_value("Podaj wytrzymałość stali [MPa] fy = ")
    break

print()

while True:
    x = get_str_value("Aby policzyć nośność przekroju na rozciąganie - wpisz n, jeśli chcesz sprawdzić warunek "
                      "nośności - wpisz w: ")
    if x == "n" or x == "w":
        break
    print("Podałeś niewłaściwą literę. Aby policzyć nośność przekroju na rozciąganie - wpisz n, jeśli chcesz "
          "sprawdzić warunek nośności - wpisz w: ")

print()
F = A * fy / 10

if x == "n":
    print("Nośność przekroju na rozciąganie wynosi Nrd = ", F, " kN")
elif x == "w":
    while True:
        N = get_float_value("Podaj wartość obliczeniowej siły podłużnej, gdzie (+) siła rozciągająca, (-) siła "
                            "ściskająca;\nNed [kN] = ")
        if N > 0:
            w = (100 * N/F).__round__(2)
            if w < 100:
                print("Warunek nośności jest spełniony, wytężenie przekroju: ", w, "%.")
                break
            print("Warunek nośności nie został spełniony, wytężenie przekroju: ", w, "%")
            break
        elif N == 0:
            print("Żadna siła nie działa w przekroju.")
            break
        else:
            a = get_str_value("Podana siła jest ściskająca - czy chcesz wprowadzić siłę rozciągającą (wpisz t) czy "
                              "zrezygnować (wpisz z): ")
            if a == "t":
                continue
            elif a == "z":
                sys.exit(0)
            else:
                print("Podałeś niewłaściwą literę. Aby wprowadzić siłę rozciągającą - wpisz t, aby zrezygnować - wpisz z.")