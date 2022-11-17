# CEBD-PROJET-JO

### Schema Relationnel
LesSportifs (<ins>numSp</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)  
LesEpreuves (<ins>numEp</ins>, nomEp, formeEp, categorieEp, nbSportifsEp, dateEp, nomDi)  
LesParticipants (<ins>numP</ins>, nomSp, prenomSp, dateNaissance, categorie, pays)  
LesEquipes (<ins>numEq</ins>)  
EstEquipier (<ins>numSp numEq</ins>)  
MedaillesOr (<ins>numP numEp</ins>)  
MedaillesArgent (<ins>numP numEp</ins>)  
MedaillesBronze(<ins>numP numEp</ins>)  
LesInscriptions (<ins>numP numEp</ins>)  

### Domaines
domaine(numSp) = domaine(numEp) = domaine(nbSportifsEp) = domaine(numP) = domaine(numEq) = domaine(or) = domaine(argent) = domaine(bronze) = entiers > 0;  
domaine(nomSp) = domaine(prenomSp) = domaine(categorie) = domaine(pays) = domaine(nomEp) = domaine(formeEp) = domaine(categorieEp) = domaine(nomDi) = chaînes de caractères;  
domaine(dateNaissance) = domaine(dateEp) = date.  

###  Contraintes d’intégrité
LesSportifs[numSp] ⊆ LesParticipants[numP]  
LesEquipes[numEq] ⊆ LesParticipants[numP]  
EstEquipier[numSp] ⊆ LesParticipants[numP]  
EstEquipier[numEq] ⊆ LesEquipes[numEq]  
LesResultats[numP] ⊆ LesParticipants[numP]  
LesResultats[numEp] ⊆ LesEpreuves[numEp]  

On peut aussi ajouter les vues suivantes:
  - __nbEquipiers__ pour les Equipes qui affiche le nombre d'équipiers dans une équipe
  - __nbVictoires__ pour les Equipes qui affiche le nombre de victoires (nombres de médailles) d'une équipe
