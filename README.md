# CEBD-PROJET-JO

### Schema Relationnel
LesSportifs (<ins>numSp</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)  
LesEpreuves (<ins>numEp</ins>, nomEp, formeEp, categorieEp, nbSportifsEp, dateEp, nomDi)  
LesParticipants (<ins>numP</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)  
LesEquipes (<ins>numEq</ins>)  
EstEquipier (<ins>numSp numEq</ins>)  
LesResultats(<ins>numP numEp</ins>, or, argent, bronze)

### Domaines
domaine(numSp) = domaine(numEp) = domaine(nbSportifsEp) = domaine(numP) = domaine(numEq) = domaine(or) = domaine(argent) = domaine(bronze) = entiers > 0;  
domaine(nomSp) = domaine(prenomSp) = domaine(categorie) = domaine(pays) = domaine(nomEp) = domaine(formeEp) = domaine(categorieEp) = domaine(nomDi) = chaînes de caractères;  
domaine(dateNaissance) = domaine(dateEp) = date.  
