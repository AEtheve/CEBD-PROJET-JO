import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


# Classe permettant d'afficher la fonction à compléter 3
class AppFctComp1Partie1(QDialog):

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_1.ui", self)
        self.data = data
        cursor = self.data.cursor()
        result = cursor.execute("SELECT DISTINCT categorieEp FROM V0_LesEpreuves")
        for row in result:
            self.ui.comboBox.addItem(row[0])

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        display.refreshLabel(self.ui.label_fct_comp_1, "")
        categorie = self.ui.comboBox.currentText()
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT numEp, nomEp, formeEp, nomDi, categorieEp, nbSportifsEp, strftime('%Y-%m-%d',dateEp) FROM V0_LesEpreuves WHERE categorieEp = ?",
                [categorie])
        except Exception as e:
            self.ui.table_fct_comp_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            i = display.refreshGenericData(self.ui.table_fct_comp_1, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_comp_1, "Aucun résultat")
