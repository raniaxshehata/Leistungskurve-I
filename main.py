import os
import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubble_sort

def main():
    # Laden der Daten
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']

    # Sortieren der Daten
    sorted_power_W = bubble_sort(power_W)

    # Erzeugen der Power-Curve Grafik
    plt.plot(sorted_power_W[::-1])
    plt.xlabel('Einzelbeobachtung (s)')
    plt.ylabel('Power (W)')
    plt.title('Power Curve')
    

    # Figures
    # Überprüfen, ob der figures-Ordner existiert, wenn nicht -> erstellen
    # Quelle: https://www.geeksforgeeks.org/python-os-makedirs-method/
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # Speichern der Grafik im figures-Ordner
    plt.savefig('figures/power_curve.png')
    plt.show()

if __name__ == "__main__":
    main()



