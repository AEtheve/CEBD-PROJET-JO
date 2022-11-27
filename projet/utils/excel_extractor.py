import sqlite3
from sqlite3 import IntegrityError

import pandas

def read_excel_file_V0(data:sqlite3.Connection, file):
    # Lecture de l'onglet du fichier excel LesSportifsEQ, en interprétant toutes les colonnes comme des strings
    # pour construire uniformement la requête
    df_sportifs = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_sportifs = df_sportifs.where(pandas.notnull(df_sportifs), 'null')

    cursor = data.cursor()
    for ix, row in df_sportifs.iterrows():
        try:
            query = "insert into V0_LesSportifsEQ values ({},'{}','{}','{}','{}','{}',{})".format(
                row['numSp'], row['nomSp'], row['prenomSp'], row['pays'], row['categorieSp'], row['dateNaisSp'], row['numEq'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)

    # Lecture de l'onglet LesEpreuves du fichier excel, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_epreuves = pandas.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_epreuves = df_epreuves.where(pandas.notnull(df_epreuves), 'null')

    cursor = data.cursor()
    for ix, row in df_epreuves.iterrows():
        try:
            query = "insert into V0_LesEpreuves values ({},'{}','{}','{}','{}',{},".format(
                row['numEp'], row['nomEp'], row['formeEp'], row['nomDi'], row['categorieEp'], row['nbSportifsEp'])

            if (row['dateEp'] != 'null'):
                query = query + "'{}')".format(row['dateEp'])
            else:
                query = query + "null)"
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(f"{err} : \n{row}")

#TODO 1.3a : modifier la lecture du fichier Excel pour lire l'ensemble des données et les intégrer dans le schéma de la BD V1
def read_excel_file_V1(data:sqlite3.Connection, file):
    # Lecture de l'onglet du fichier excel LesDisciplines, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_disciplines = pandas.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_disciplines = df_disciplines.where(pandas.notnull(df_disciplines), 'null')

    cursor = data.cursor()
    for ix, row in df_disciplines.iterrows():
        try:
            query = "insert into LesDisciplines values ('{}')".format(row['nomDi'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)

    # Lecture de l'onglet du fichier excel LesParticipants, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    #
    # df_participants1 = pandas.read_excel(file, sheet_name='LesInscriptions', dtype=str)
    # df_participants1 = df_participants1.where(pandas.notnull(df_participants1), 'null')
    #
    # cursor = data.cursor()
    # for ix, row in df_participants1.iterrows():
    #     try:
    #         query = "insert into LesParticipants values ({})".format(row['numIn'])
    #         # On affiche la requête pour comprendre la construction. A enlever une fois compris.
    #         print(query)
    #         cursor.execute(query)
    #     except IntegrityError as err:
    #         print(err)

    # Lecture de l'onglet du fichier excel LesSportifs, en interprétant toutes les colonnes comme des strings
    # pour construire uniformement la requête
    df_sportifs = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_sportifs = df_sportifs.where(pandas.notnull(df_sportifs), 'null')

    cursor = data.cursor()
    for ix, row in df_sportifs.iterrows():
        try:
            query = "insert into LesSportifs values ({},'{}','{}','{}','{}','{}')".format(
                row['numSp'], row['nomSp'], row['prenomSp'], row['pays'], row['categorieSp'], row['dateNaisSp'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)

    # Lecture de l'onglet du fichier excel LesEpreuves, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_epreuves = pandas.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_epreuves = df_epreuves.where(pandas.notnull(df_epreuves), 'null')

    cursor = data.cursor()
    for ix, row in df_epreuves.iterrows():
        try:
            query = "insert into LesEpreuves values ({},'{}','{}','{}','{}',{},".format(
                row['numEp'], row['nomEp'], row['formeEp'], row['nomDi'], row['categorieEp'], row['nbSportifsEp'])

            if (row['dateEp'] != 'null'):
                query = query + "'{}')".format(row['dateEp'])
            else:
                query = query + "null)"
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(f"{err} : \n{row}")
    #
    # Lecture de l'onglet du fichier excel LesEquipes, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_equipes = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_equipes = df_equipes.where(pandas.notnull(df_equipes), 'null')

    cursor = data.cursor()
    for ix, row in df_equipes.iterrows():
        try:
            query = "insert into LesEquipes values ({})".format(row['numEq'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)
    #
    # Lecture de l'onglet du fichier excel EstEquipier, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête

    df_estEquipier = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_estEquipier = df_estEquipier.where(pandas.notnull(df_estEquipier), 'null')

    cursor = data.cursor()
    for ix, row in df_estEquipier.iterrows():
        try:
            query = "insert into EstEquipier values ({},{})".format(row['numSp'], row['numEq'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)
    #
    # Lecture de l'onglet du fichier excel MedaillesOr, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête

    # df_medaillesOr = pandas.read_excel(file, sheet_name='MedaillesOr', dtype=str)
    # df_medaillesOr = df_medaillesOr.where(pandas.notnull(df_medaillesOr), 'null')
    #
    # cursor = data.cursor()
    # for ix, row in df_medaillesOr.iterrows():
    #     try:
    #         query = "insert into MedaillesOr values ({},{})".format(row['numP'], row['numEp'])
    #         # On affiche la requête pour comprendre la construction. A enlever une fois compris.
    #         print(query)
    #         cursor.execute(query)
    #     except IntegrityError as err:
    #         print(err)
    #
    # # Lecture de l'onglet du fichier excel MedaillesArgent, en interprétant toutes les colonnes comme des string
    # # pour construire uniformement la requête
    #
    # df_medaillesArgent = pandas.read_excel(file, sheet_name='MedaillesArgent', dtype=str)
    # df_medaillesArgent = df_medaillesArgent.where(pandas.notnull(df_medaillesArgent), 'null')
    #
    # cursor = data.cursor()
    # for ix, row in df_medaillesArgent.iterrows():
    #     try:
    #         query = "insert into MedaillesArgent values ({},{})".format(row['numP'], row['numEp'])
    #         # On affiche la requête pour comprendre la construction. A enlever une fois compris.
    #         print(query)
    #         cursor.execute(query)
    #     except IntegrityError as err:
    #         print(err)
    #
    # # Lecture de l'onglet du fichier excel MedaillesBronze, en interprétant toutes les colonnes comme des string
    # # pour construire uniformement la requête
    #
    # df_medaillesBronze = pandas.read_excel(file, sheet_name='MedaillesBronze', dtype=str)
    # df_medaillesBronze = df_medaillesBronze.where(pandas.notnull(df_medaillesBronze), 'null')
    #
    # cursor = data.cursor()
    # for ix, row in df_medaillesBronze.iterrows():
    #     try:
    #         query = "insert into MedaillesBronze values ({},{})".format(row['numP'], row['numEp'])
    #         # On affiche la requête pour comprendre la construction. A enlever une fois compris.
    #         print(query)
    #         cursor.execute(query)
    #     except IntegrityError as err:
    #         print(err)
    #
    # Lecture de l'onglet du fichier excel LesInscriptions, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête

    df_inscriptions = pandas.read_excel(file, sheet_name='LesInscriptions', dtype=str)
    df_inscriptions = df_inscriptions.where(pandas.notnull(df_inscriptions), 'null')

    cursor = data.cursor()
    for ix, row in df_inscriptions.iterrows():
        try:
            query = "insert into LesInscriptions values ({},{})".format(row['numIn'], row['numEp'])
            # On affiche la requête pour comprendre la construction. A enlever une fois compris.
            print(query)
            cursor.execute(query)
        except IntegrityError as err:
            print(err)