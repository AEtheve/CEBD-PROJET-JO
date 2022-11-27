
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class AppFct2_1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_2_1.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_2_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute('''
            SELECT numEq, AVG(age), COUNT(numP)
FROM  LesAgesSportifs R1 JOIN EstEquipier  USING (numSp) JOIN MedaillesOr R2 ON (R1.numSp = R2.numP)
GROUP BY numEq;
            ''')

        except Exception as e:
            self.ui.table_fct_2_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_2_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_2_1, result)