class ParkingLot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print("Masina a fost parcata cu succes.")
        else:
            print("Parcarea este plina. Nu exista locuri disponibile.")

    def leave(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            print("Masina a parasit parcare cu succes.")
        else:
            print("Parcarea este deja goala. Nu exista masini parcate.")

    def check_availability(self):
        print(f"Locuri libere: {self.available_spaces}/{self.total_spaces}")

# Exemplu
parking = ParkingLot(10)
parking.check_availability()
parking.park()
parking.check_availability()
parking.leave()
parking.check_availability()
