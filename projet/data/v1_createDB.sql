CREATE TABLE LesDisciplines
(
  nom VARCHAR2(25) NOT NULL,
  CONSTRAINT D_PK PRIMARY KEY (nom)
);

CREATE TABLE LesSportifs
(
  numSp NUMBER(4) NOT NULL,
  nomSp VARCHAR2(20) NOT NULL,
  prenomSp VARCHAR2(20) NOT NULL,
  pays VARCHAR2(20) NOT NULL,
  categorieSp VARCHAR2(10) NOT NULL,
  dateNaissance DATE NOT NULL,
  CONSTRAINT SP_PK PRIMARY KEY (numSp),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin'))
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3) NOT NULL,
  nomEp VARCHAR2(20) NOT NULL,
  formeEp VARCHAR2(13) NOT NULL,
  nomDi VARCHAR2(25) NOT NULL,
  categorieEp VARCHAR2(10) NOT NULL,
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
  numEq NUMBER(3) NOT NULL,
  CONSTRAINT NE_PK PRIMARY KEY (numEq),
  CONSTRAINT NE_CK1 CHECK (numEq > 0)
);

CREATE TABLE EstEquipier
(
  numSp NUMBER(4) NOT NULL,
  numEq NUMBER(3) NOT NULL,
  CONSTRAINT EE_PK PRIMARY KEY (numSp, numEq),
  CONSTRAINT EE_CK1 CHECK (numSp > 0),
  CONSTRAINT EE_CK2 CHECK (numEq > 0),
  CONSTRAINT EE_FK1 FOREIGN KEY (numSp) REFERENCES LesSportifs(numP),
  CONSTRAINT EE_FK2 FOREIGN KEY (numEq) REFERENCES LesEquipes(numEq)
);

CREATE TABLE MedaillesOr
(
  numP NUMBER(4) NOT NULL,
  numEp NUMBER(3) NOT NULL,
  CONSTRAINT MO_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MO_CK1 CHECK (numP > 0),
  CONSTRAINT MO_CK2 CHECK (numEp > 0),
  CONSTRAINT MB_FK1 FOREIGN KEY (numP) REFERENCES LesSportifs(numSp),
  CONSTRAINT MO_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

CREATE TABLE MedaillesArgent
(
  numP NUMBER(4) NOT NULL,
  numEp NUMBER(3) NOT NULL,
  CONSTRAINT MA_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MA_CK1 CHECK (numP > 0),
  CONSTRAINT MA_CK2 CHECK (numEp > 0),
  CONSTRAINT MB_FK1 FOREIGN KEY (numP) REFERENCES LesSportifs(numSp),
  CONSTRAINT MA_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);

CREATE TABLE MedaillesBronze
(
  numP NUMBER(4) NOT NULL,
  numEp NUMBER(3) NOT NULL,
  CONSTRAINT MB_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT MB_CK1 CHECK (numP > 0),
  CONSTRAINT MB_CK2 CHECK (numEp > 0),
  CONSTRAINT MB_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT MB_FK1 FOREIGN KEY (numP) REFERENCES LesSportifs(numSp)
);

CREATE TABLE LesInscriptions
(
  numP NUMBER(4) NOT NULL,
  numEp NUMBER(3) NOT NULL,
  CONSTRAINT I_PK PRIMARY KEY (numP, numEp),
  CONSTRAINT I_CK1 CHECK (numP > 0),
  CONSTRAINT I_CK2 CHECK (numEp > 0),
  CONSTRAINT I_FK2 FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp)
);


CREATE VIEW LesAgesSportifs(
    numSp ,
    nomSp,
    prenomSp,
    age
) AS SELECT
    numSp,
    nomSp,
    prenomSp,
    strftime('%Y', 'now') - strftime('%Y', dateNaissance)
FROM LesSportifs;


CREATE VIEW LesNbsEquipiers (
    numEq,
    nbEquipiers
)   AS SELECT numEq, COUNT(numSp) AS nbEquipiers
    FROM EstEquipier
    GROUP BY numEq;
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)

