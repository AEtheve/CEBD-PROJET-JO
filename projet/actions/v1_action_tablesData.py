
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog, QWidget, QTableWidget, QHeaderView
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesDataV1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_tablesData.ui", self)
        self.data = data

        # On met à jour l'affichage avec les données actuellement présentes dans la base
        self.refreshAllTablesV1()

    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################

    # Fonction de mise à jour de l'affichage d'une seule table
    def refreshTable(self, label, table, query):
        display.refreshLabel(label, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            table.setRowCount(0)
            display.refreshLabel(label, "Impossible d'afficher les données de la table : " + repr(e))
        else:
            display.refreshGenericData(table, result)


    # Fonction permettant de mettre à jour toutes les tables
    @pyqtSlot()
    def refreshAllTablesV1(self):
        tabs = self.data.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'V0_%' OR type='view'").fetchall()
        for tab in tabs:
            tabTest = QWidget()
            tabTest.setObjectName(tab[0])
            self.ui.tabWidget.addTab(tabTest, tab[0])
            table = QTableWidget(tabTest)
            table.setColumnCount(2)
            
            table.setGeometry(0, 0, 905, 447)
            
            cursor = self.data.cursor()
            result = cursor.execute('SELECT * FROM ' + tab[0])
            table.setColumnCount(len(result.description))
            table.setHorizontalHeaderLabels([i[0] for i in result.description])

            self.refreshTable(self.ui.label_error, table, 'SELECT * FROM ' + tab[0])
            table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        # TODO 1.4b : ajouter l'affichage des éléments de la vue LesAgesSportifs après l'avoir créée
        # TODO 1.5b : ajouter l'affichage des éléments de la vue LesNbsEquipiers après l'avoir créée
