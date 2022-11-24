# CEBD-PROJET-JO

### Schema Relationnel
LesSportifs (<ins>numSp</ins>, nomSp, prenomSp, dateNaissance, categorieSp, pays)  
/* <nu,n,p,d,c,pa> Le sportif identifié par le numéro nu a le nom n, le prenom p, la date de naissance d, il fait partie de la categorie c et il répresente le pays p.*/  

LesEpreuves (<ins>numEp</ins>, nomEp, formeEp, categorieEp, nbSportifsEp, dateEp, nomDi)  
/* <nu,n,f,c,nb,d,nd> L'épreuve de forme f et catégorie c, qui fait partie de la discipline nd est identifiée par le numéro nu. Elle a un nombre nb de sportifs et elle se déroule à la date d. */   

LesParticipants (<ins>numP</ins>, nomP, prenomP, dateNaissance, categorie, pays)  
/* <nu,n,p,d,c,p> Le participant à une épreuve de categorie c, qui répresente le pays p, est identifié par le numéro nu, il a le nom n, le prénom p, la date de naissance d.*/  

LesEquipes (<ins>numEq</ins>)  
/* \<n\> Les équipes sont identifiées par le numéro n. */  

EstEquipier (<ins>numSp numEq</ins>)  
/* <ns,ne> Le sportif ns fait partie de l'équipe ne. */  

MedaillesOr (<ins>numP numEp</ins>)  
/* <np,ne> Le participant np a gagné une médaille d'or à l'épreuve ne. */  

MedaillesArgent (<ins>numP numEp</ins>)  
/* <np,ne> Le participant np a gagné une médaille d'argent à l'épreuve ne. */  

MedaillesBronze(<ins>numP numEp</ins>)  
/* <np,ne> Le participant np a gagné une médaille de bronze à l'épreuve ne. */  

LesInscriptions (<ins>numP numEp</ins>)  
/* <np, ne> Le participant np est inscrit à l'épreuve ne.  */  

LesDisciplines (<ins>nom</ins>)
/* <n> n est le nom d'une discipline. */ 

### Domaines
domaine(numSp) = domaine(numEp) = domaine(nbSportifsEp) = domaine(numP) = domaine(numEq) = domaine(or) = domaine(argent) = domaine(bronze) = entiers > 0;  
domaine(nomSp) = domaine(prenomSp) = domaine(categorie) = domaine(pays) = domaine(nomEp) = domaine(formeEp) = domaine(categorieEp) = domaine(nomDi) = chaînes de caractères;  
domaine(dateNaissance) = domaine(dateEp) = date.  

###  Contraintes d’intégrité
LesSportifs[numSp] ⊆ LesParticipants[numP]  
LesEquipes[numEq] ⊆ LesParticipants[numP]  
EstEquipier[numSp] ⊆ LesParticipants[numP]  
EstEquipier[numEq] ⊆ LesEquipes[numEq]  
LesParticipants[categorie] ⊆ LesEpreuves[categorieEp]  
MedaillesOr[numP]  ⊆ LesParticipants[numP]  
MedaillesOr[numEp] ⊆ LesEpreuves[numEp]  
MedaillesArgent[numP] ⊆ LesParticipants[numP]  
MedaillesArgent[numEp] ⊆ LesEpreuves[numEp]  
MedaillesBronze[numP] ⊆ LesParticipants[numP]    
MedaillesBronze[numEp] ⊆ LesEpreuves[numEp]   
LesInscriptions[numP] ⊆ LesParticipants[numP]   
LesInscriptions[numEp] ⊆ LesEpreuves[numEp]  
LesEpreuves[nomDi] ⊆ LesDisciplines[nom]  

On peut aussi ajouter les vues suivantes:
  - __nbEquipiers__ pour les Equipes qui affiche le nombre d'équipiers dans une équipe
  - __nbVictoires__ pour les Equipes qui affiche le nombre de victoires (nombres de médailles) d'une équipe
