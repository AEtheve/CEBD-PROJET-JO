
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class AppFctAdd_Participant(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection, numEp, parent):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/gestion_inscriptions_insert.ui", self)
        self.data = data
        self.numEp = numEp
        self.parent = parent

        cursor = self.data.cursor()
        result = cursor.execute('''
        SELECT numSp
        FROM LesSportifs WHERE numSp NOT IN (SELECT numP FROM LesInscriptions WHERE numEp = ?)
        UNION
        SELECT numEq
        FROM LesEquipes WHERE numEq NOT IN (SELECT numP FROM LesInscriptions WHERE numEp = ?)
        ''', [numEp, numEp])

        for row in result:
            self.ui.comboBox.addItem(str(row[0]))
            
    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        pass

    def insert(self):
        try:
            cursor = self.data.cursor()
            cursor.execute('''
            INSERT INTO LesInscriptions (numEp, numP)
            VALUES (?, ?)
            ''', [self.numEp, self.ui.comboBox.currentText()])
            self.data.commit()
            

        except Exception:
            self.parent.refreshResult()
            self.close()
        else:
            self.parent.refreshResult()
            self.close()