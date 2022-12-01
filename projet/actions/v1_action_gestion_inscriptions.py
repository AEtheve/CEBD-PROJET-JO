
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from actions.v1_action_add_participant import AppFctAdd_Participant

class AppFctGestion_Inscriptions(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/gestion_inscriptions.ui", self)
        self.data = data
        
        cursor = self.data.cursor()
        result = cursor.execute("SELECT numEp FROM LesEpreuves")
        for row in result:
            self.ui.comboBox.addItem(str(row[0]))
            
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshSelected(self):
        if self.ui.tableWidget.selectionModel().hasSelection():
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton_3.setEnabled(False)

    def removeInscription(self):
            rows = sorted(set(index.row() for index in self.ui.tableWidget.selectedIndexes()))
            for row in rows:
                numEp = self.ui.comboBox.currentText()
                numP = self.ui.tableWidget.item(row, 0)
                if numP is not None:
                    numP = numP.text()    
                    cursor = self.data.cursor()
                    cursor.execute("DELETE FROM LesInscriptions WHERE numEp = ? AND numP = ?", [numEp, numP])
                    self.data.commit()
            self.refreshResult() 

    def OpenAddParticipant(self):
        self.fenetre = AppFctAdd_Participant(self.data, self.ui.comboBox.currentText(), self)
        self.fenetre.show()
        
    def refreshResult(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                    '''
                    SELECT  DISTINCT numEq, pays
                    FROM LesEquipes R1 JOIN LesInscriptions R2 ON (R1.numEq = R2.numP)
					JOIN EstEquipier USING (numEq) JOIN LesSportifs USING (numSp)
					WHERE numEp = ?
                    UNION
                    SELECT  numSp, pays
                                        FROM LesSportifs R1 JOIN LesInscriptions R2 ON (R1.numSp = R2.numP)
                                        WHERE numEp = ?;
                    ''',
                    [self.ui.comboBox.currentText(), self.ui.comboBox.currentText()])
        except Exception as e:
            print(e)
        else:
            i = display.refreshGenericData(self.ui.tableWidget, result)
            display.refreshLabel(self.ui.label, "<b>Nombre d'inscriptions</b>: " + str(i))

            nomEpreuve = cursor.execute("SELECT nomEp FROM LesEpreuves WHERE numEp = ?", [self.ui.comboBox.currentText()])
            nomEpreuve = nomEpreuve.fetchone()
            display.refreshLabel(self.ui.label_2, "<b>Epreuve</b>: " + str(nomEpreuve[0]))