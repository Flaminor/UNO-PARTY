import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MenuJeux(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu de jeux vidéo")
        self.setGeometry(100, 100, 400, 300)

        titre = QLabel("Bienvenue dans notre menu de jeux vidéo !", self)
        titre.move(50, 50)
        titre.resize(300, 30)

        bouton_histoire = QPushButton("Histoire", self)
        bouton_histoire.move(50, 100)
        bouton_histoire.resize(300, 30)
        bouton_histoire.clicked.connect(lambda: self.selectionner_option("histoire"))

        bouton_partie_locale = QPushButton("Partie locale", self)
        bouton_partie_locale.move(50, 150)
        bouton_partie_locale.resize(300, 30)
        bouton_partie_locale.clicked.connect(lambda: self.selectionner_option("partie_locale"))

    def selectionner_option(self, option):
        if option == "histoire":
            print("Vous avez choisi l'option Histoire.")
            # Code pour lancer le mode histoire
        elif option == "partie_locale":
            print("Vous avez choisi l'option Partie locale.")
            # Code pour lancer le mode partie locale

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MenuJeux()
    menu.show()
    sys.exit(app.exec_())
