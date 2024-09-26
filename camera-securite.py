from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import cv2
import winsound

#Cette ligne charge le fichier de l’interface utilisateur (UI) nommé camera-securite.py. La fonction loadUiType est utilisée pour charger les fichiers .ui créés avec Qt Designer.
ui,_=loadUiType('security_cam.ui')

"""
Définition de la classe principale de l’application : MainApp hérite de QMainWindow et de l’interface utilisateur chargée. 
Le constructeur initialise la fenêtre principale et configure l’interface utilisateur.
"""
class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.MONITORING.clicked.connect(self.start_monitoring)
        self.VOLUME.clicked.connect(self.set_volume)
        self.EXIT.clicked.connect(self.close_window)
        
    def start_monitoring(self):
        print('Moniteur démarré')
        
    def set_volume(self):
        print('volume augmenté')
        
    def close_window(self):
        print('fenêtre fermé')
        
"""
Fonction principale : La fonction main crée une instance de l’application Qt (QApplication), crée une instance de MainApp, 
affiche la fenêtre principale et lance la boucle d’événements de l’application avec app.exec_()
"""   
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
#Exécution du script: Cette condition vérifie si le script est exécuté directement (et non importé comme module), et appelle la fonction main pour démarrer l’application
if __name__ == '__main__':
    main()