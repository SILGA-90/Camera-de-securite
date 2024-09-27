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
    volume = 500
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen)
        self.MONITORING.clicked.connect(self.start_monitoring)
        self.VOLUME.clicked.connect(self.set_volume)
        self.EXIT.clicked.connect(self.close_window)
        self.VOLUMESLIDER.setVisible(False)
        self.VOLUMESLIDER.valueChanged.connect(self.set_volume_level)
        
        
    def start_monitoring(self):
        print('Moniteur démarré')
        webcam = cv2.VideoCapture(0)
        while True:
            _,im1 = webcam.read()
            _,im2 = webcam.read()
            diff = cv2.absdiff(im1,im2)
            gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),0)
            _,thresh = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh,None,iterations=3)
            contours,_= cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv2.contourArea(c) < 5000:
                    continue
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(im1,(x,y),(x+w,y+h),(0,255,2))
                cv2.imwrite('captured.jpg',im1)
                image = QImage('captured.jpg')
                pm = QPixmap.fromImage(image)
                self.CAMWINDOW.setPixmap(pm)
                winsound.Beep(self.volume,100)
            cv2.imshow("CAMERA DE SURVEILLANCE",im1)
    
            key = cv2.waitKey(10)
            if key == 27:
                break
        webcam.release()
        cv2.destroyAllWindows()
        
    def set_volume(self):
        self.VOLUMESLIDER.setVisible(True)
        
    def close_window(self):
        self.close()
        
    def set_volume_level(self):
        self.VOLUMELEVEL.setText(str(self.VOLUMESLIDER.value()//10))
        self.volume = self.VOLUMESLIDER.value() * 10
        cv2.waitKey(1000)
        self.VOLUMESLIDER.setVisible(False)
        
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