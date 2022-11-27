CREATE TABLE LesDisciplines
(
  nom VARCHAR2(25),
  CONSTRAINT D_PK PRIMARY KEY (nom)
);

CREATE TABLE LesParticipants
(
  numP NUMBER(4),
  nomP VARCHAR2(20),
  prenomP VARCHAR2(20),
  dateNaissance DATE,
  categorie VARCHAR2(10),
  pays VARCHAR2(20),
  CONSTRAINT P_PK PRIMARY KEY (numP),
  CONSTRAINT P_CK1 CHECK (numP > 0),
  CONSTRAINT P_CK2 CHECK (categorie IN ('feminin','masculin','mixte'))
);

CREATE TABLE LesSportifs
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaissance DATE,
  CONSTRAINT SP_PK PRIMARY KEY (numSp),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_FK1 FOREIGN KEY (numSp) REFERENCES LesParticipants(numP)
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0),
  CONSTRAINT EP_FK1 FOREIGN KEY (nomDi) REFERENCES LesDisciplines(nom)
);


CREATE TABLE LesEquipes
(
  numEq NUMBER(3),
  CONSTRAINT NE_PK PRIMARY KEY (numEq),
  CONSTRAINT NE_CK1 CHECK (numEq > 0),
  CONSTRAINT NE_FK1 FOREIGN KEY (numEq) REFERENCES LesParticipants(numP)
);

CREATE TABLE EstEquipier
(
  numSp NUMBER(4),
  numEq NUMBER(3),
  CONSTRAINT EE_PK PRIMARY KEY (numSp, numEq),
  CONSTRAINT EE_CK1 CHECK (numSp > 0),
  CONSTRAINT EE_CK2 CHECK (numEq > 0),
  CONSTRAINT EE_FK1 FOREIGN KEY (numSp) REFERENCES LesParticipants(numP),
  CONSTRAINT EE_FK2 FOREIGN KEY (numEq) REFERENCES LesEquipes(numEq)
);

CREATE TABLE MedaillesOr
(
  numP NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT MO_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MO_CK1 CHECK (numP > 0),
  CONSTRAINT MO_CK2 CHECK (numEp > 0),
  CONSTRAINT MO_FK1 FOREIGN KEY (numP) REFERENCES LesParticipants(numP),
  CONSTRAINT MO_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

CREATE TABLE MedaillesArgent
(
  numP NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT MA_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MA_CK1 CHECK (numP > 0),
  CONSTRAINT MA_CK2 CHECK (numEp > 0),
  CONSTRAINT MA_FK1 FOREIGN KEY (numP) REFERENCES LesParticipants(numP),
  CONSTRAINT MA_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

CREATE TABLE MedaillesBronze
(
  numP NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT MB_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MB_CK1 CHECK (numP > 0),
  CONSTRAINT MB_CK2 CHECK (numEp > 0),
  CONSTRAINT MB_FK1 FOREIGN KEY (numP) REFERENCES LesParticipants(numP),
  CONSTRAINT MB_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

CREATE TABLE LesInscriptions
(
  numP NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT I_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT I_CK1 CHECK (numP > 0),
  CONSTRAINT I_CK2 CHECK (numEp > 0),
  CONSTRAINT I_FK1 FOREIGN KEY (numP) REFERENCES LesParticipants(numP),
  CONSTRAINT I_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);
-- TODO 1.4a : ajouter la définition de la vue LesAgesSportifs
-- TODO 1.5a : ajouter la définition de la vue LesNbsEquipiers
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)
