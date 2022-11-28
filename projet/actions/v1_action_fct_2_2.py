
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class AppFct2_2(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_2_2.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_2_2, "")
        # execute data/fct_2_2.sql
#         try:
#             cursor = self.data.cursor()
#             result = cursor.execute('''
#             SELECT numEq, AVG(age), COUNT(numP)
# FROM  LesAgesSportifs R1 JOIN EstEquipier  USING (numSp) JOIN MedaillesOr R2 ON (R1.numSp = R2.numP)
# GROUP BY numEq;
#             ''')

#         except Exception as e:
#             self.ui.table_fct_2_1.setRowCount(0)
#             display.refreshLabel(self.ui.label_fct_2_1, "Impossible d'afficher les résultats : " + repr(e))
#         else:
#             display.refreshGenericData(self.ui.table_fct_2_1, result)
        try:
            cursor = self.data.cursor()
            result = cursor.execute('''
            WITH Or1 AS (SELECT pays, COUNT(*)  AS nbOr1
FROM LesSportifs  JOIN MedaillesOr ON (numSp = numP)
GROUP BY pays),
Or2 AS (SELECT  pays, COUNT(DISTINCT numEp) AS nbOr2
FROM MedaillesOr JOIN EstEquipier ON (numP = numEq)  JOIN LesSportifs USING (numSp)
WHERE numP < 1000
GROUP BY pays),
PaysOr AS (SELECT pays, COALESCE (nbOr1, 0) + COALESCE (nbOr2, 0) AS nbOr
FROM Or1 LEFT OUTER JOIN Or2 USING (pays)
UNION
SELECT pays, COALESCE (nbOr1, 0) + COALESCE (nbOr2, 0) AS nbOr
FROM Or2 LEFT OUTER JOIN Or1 USING (pays)
),
Argent1 AS (SELECT pays, COUNT(*)  AS nbArgent1
FROM LesSportifs  JOIN MedaillesArgent ON (numSp = numP)
GROUP BY pays),
Argent2 AS (SELECT  pays, COUNT(DISTINCT numEp) AS nbArgent2
FROM MedaillesArgent JOIN EstEquipier ON (numP = numEq)  JOIN LesSportifs USING (numSp)
WHERE numP < 1000
GROUP BY pays),
PaysArgent AS (SELECT pays, COALESCE (nbArgent1, 0) + COALESCE (nbArgent2, 0) AS nbArgent
FROM Argent1 LEFT OUTER JOIN Argent2 USING (pays)
UNION
SELECT pays, COALESCE (nbArgent1, 0) + COALESCE (nbArgent2, 0) AS nbArgent
FROM Argent2 LEFT OUTER JOIN Argent1 USING (pays)
),
Bronze1 AS (SELECT pays, COUNT(*)  AS nbBronze1
FROM LesSportifs  JOIN MedaillesBronze ON (numSp = numP)
GROUP BY pays),
Bronze2 AS (SELECT  pays, COUNT(DISTINCT numEp) AS nbBronze2
FROM MedaillesBronze JOIN EstEquipier ON (numP = numEq)  JOIN LesSportifs USING (numSp)
WHERE numP < 1000
GROUP BY pays),
PaysBronze AS (SELECT pays, COALESCE (nbBronze1, 0) + COALESCE (nbBronze2, 0) AS nbBronze
FROM Bronze1 LEFT OUTER JOIN Bronze2 USING (pays)
UNION
SELECT pays, COALESCE (nbBronze1, 0) + COALESCE (nbBronze2, 0) AS nbBronze
FROM Bronze2 LEFT OUTER JOIN Bronze1 USING (pays)
)
SELECT DISTINCT pays, COALESCE (nbOr, 0) AS nbOr,
                      COALESCE (nbArgent, 0) AS nbArgent,
                      COALESCE (nbBronze, 0) AS nbBronze
FROM LesSportifs LEFT OUTER JOIN PaysOr USING (pays)
                 LEFT OUTER JOIN PaysArgent USING (pays)
                  LEFT OUTER JOIN PaysBronze USING (pays)
                ORDER BY COALESCE (nbOr, 0) + COALESCE (nbArgent, 0) + COALESCE (nbBronze, 0) DESC,
                          COALESCE (nbOr, 0) DESC,
                          COALESCE (nbArgent, 0) DESC,
                          COALESCE (nbBronze, 0) DESC;
            ''')

        except Exception as e:
            self.ui.table_fct_2_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_2_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_2_2, result)