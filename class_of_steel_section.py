import math
from console_variables_getters import get_int_value

# pobieranie danych
def get_float_value(index, t_value):
    while True:
        try:
            x = float(input("Podaj wartość " + index + " [mm] = "))
            if index == "c" and x <= t_value:
                print("Podane c jest mniejsze od t - wprowadź poprawną wartość.")
                continue
            return x
        except ValueError:
            print("Podałeś niewłaściwą wartość, wpisz ją ponownie.")


def section_force():
    while True:
        x = input("Przekrój ściskany czy zginany? [wpisz s/z]: ").lower()
        if x == "z" or x == "s":
            return x
        print("Podałeś niewłaściwą literę. Wpisz z jeśli przekrój jest zginany, wpisz s jeśli przekrój jest ściskany.")


def class_of_section(b, E, y1, y2, y3):
    if b <= y1 * E:
        return 1
    elif b <= y2 * E:
        return 2
    elif b <= y3 * E:
        return 3
    else:
        return 4


def test_two_variables(c, t, fy):
    b = c/t
    E = math.sqrt((235/fy))
    return b, E


print("Wprowadź poniższe dane aby wyliczyć klasę elementu. W zapisie dziesiętnym użyj kropki.")
t = get_float_value("t", None)
c = get_float_value("c", t)
fy = get_int_value("Podaj wytrzymałość stali [MPa] fy = ")
a = section_force()

# policzenie c/t oraz epsilon
b, E = test_two_variables(c, t, fy)

# sprawdzenie warunków
if a == "z":
    k = class_of_section(b, E, 72, 83, 124)
else:
    k = class_of_section(b, E, 33, 38, 42)

# klasa przekroju
print("Klasa wprowadzonego przekroju: ", k)