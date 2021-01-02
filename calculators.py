from console_variables_getters import get_int_value

x = -1
while x != 1:
    x = get_int_value("Z jakiego kalkulatora chcesz skorzystać?\n1: Sprawdzanie klasy przekroju stalowego\nTwój wybór: ")
    print("Dostępna liczba kalkulatorów to 1. Wprowadź wybór ponownie.\n")
