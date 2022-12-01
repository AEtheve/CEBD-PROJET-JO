
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class AppFctGestion_Resultats(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/gestion_resultats.ui", self)
        self.data = data
        
        cursor = self.data.cursor()
        result = cursor.execute("SELECT numEp FROM LesEpreuves")
        for row in result:
            self.ui.comboBox.addItem(str(row[0]))
            
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def edit_Or(self):
        exist = self.data.cursor().execute("SELECT numEp FROM MedaillesOr WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
        if exist is None:
            insert = self.data.cursor()
            insert.execute("INSERT INTO MedaillesOr(numEp, numP) VALUES (?, ?)", [self.ui.comboBox.currentText(), self.ui.SelectOr.currentText()])
            self.data.commit()
            self.refreshResult()
        else:
            update = self.data.cursor()
            update.execute("UPDATE MedaillesOr SET numP = ? WHERE numEp = ?", [self.ui.SelectOr.currentText(), self.ui.comboBox.currentText()])
            self.data.commit()
            self.refreshResult()
        

    def edit_Argent(self):
        exist = self.data.cursor().execute("SELECT numEp FROM MedaillesArgent WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
        if exist is None:
            insert = self.data.cursor()
            insert.execute("INSERT INTO MedaillesArgent(numEp, numP) VALUES (?, ?)", [self.ui.comboBox.currentText(), self.ui.SelectArgent.currentText()])
            self.data.commit()
            self.refreshResult()
        else:
            update = self.data.cursor()
            update.execute("UPDATE MedaillesArgent SET numP = ? WHERE numEp = ?", [self.ui.SelectArgent.currentText(), self.ui.comboBox.currentText()])
            self.data.commit()
            self.refreshResult()

    def edit_Bronze(self):
        exist = self.data.cursor().execute("SELECT numEp FROM MedaillesBronze WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
        if exist is None:
            insert = self.data.cursor()
            insert.execute("INSERT INTO MedaillesBronze(numEp, numP) VALUES (?, ?)", [self.ui.comboBox.currentText(), self.ui.SelectBronze.currentText()])
            self.data.commit()
            self.refreshResult()
        else:
            update = self.data.cursor()
            update.execute("UPDATE MedaillesBronze SET numP = ? WHERE numEp = ?", [self.ui.SelectBronze.currentText(), self.ui.comboBox.currentText()])
            self.data.commit()
            self.refreshResult()
    
    def refreshResult(self):
        try:
            self.ui.SelectOr.clear()
            self.ui.SelectArgent.clear()
            self.ui.SelectBronze.clear()
            
            MedailleOr = self.data.cursor().execute("SELECT numP FROM MedaillesOr WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
            MedailleArgent = self.data.cursor().execute("SELECT numP FROM MedaillesArgent WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
            MedailleBronze = self.data.cursor().execute("SELECT numP FROM MedaillesBronze WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchone()
            participants = self.data.cursor().execute("SELECT numP FROM LesInscriptions WHERE numEp = ?", [self.ui.comboBox.currentText()]).fetchall()

            if MedailleOr is not None:
                self.ui.SelectOr.addItem(str(MedailleOr[0]))
            if MedailleArgent is not None:
                self.ui.SelectArgent.addItem(str(MedailleArgent[0]))
            if MedailleBronze is not None:
                self.ui.SelectBronze.addItem(str(MedailleBronze[0]))

            if len(participants) > 0:
                for participant in participants:
                    if (MedailleOr is None or participant[0] != MedailleOr[0]) and participant[0] != MedailleArgent and participant[0] != MedailleBronze:
                        self.ui.SelectOr.addItem(str(participant[0]))
                    if (MedailleArgent is None or participant[0] != MedailleArgent[0]) and participant[0] != MedailleOr and participant[0] != MedailleBronze:
                        self.ui.SelectArgent.addItem(str(participant[0]))
                    if (MedailleBronze is None or participant[0] != MedailleBronze[0]) and participant[0] != MedailleOr and participant[0] != MedailleArgent:
                        self.ui.SelectBronze.addItem(str(participant[0]))

        except Exception as e:
            print(e)