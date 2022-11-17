# CEBD-PROJET-JO

### Schema Relationnel
LesSportifs (<ins>numSp</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)
LesEpreuves (<ins>numEp</ins>, nomEp, formeEp, categorieEp, nbSportifsEp, dateEp, nomDi)
LesParticipants (<ins>numP</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)
LesEquipes (<ins>numEq</ins>)
EstEquipier (<ins>numSp numEq</ins>)
LesResultats(<ins>numP numEp</ins>, or, argent, bronze)
