import random as ra
from matplotlib import pyplot as plt


class Simulation:
    def __init__(self):
        self.wartende_kunden     = 0
        self.uhrzeit             = 0.0
        self.ankunftszeit        = self.ZeitdifferenzAnkunft()
        self.abreisezeit         = float('inf')
        self.wartezeit           = 0

    def Zeitschritt(self):
        zeitpunkt_event = min(self.ankunftszeit, self.abreisezeit)
        self.wartezeit += self.wartende_kunden * (zeitpunkt_event - self.uhrzeit)
        self.uhrzeit = zeitpunkt_event16self.Ankunft() if self.ankunftszeit <= self.abreisezeit else self.Abreise()