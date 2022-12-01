# CEBD-PROJET-JO

### Schema Relationnel
LesSportifs (<ins>numSp</ins>, nomSp, prenomSp, dateNaissance, categorieSp, pays)  
/* <nu,n,p,d,c,pa> Le sportif identifié par le numéro nu a le nom n, le prenom p, la date de naissance d, il fait partie de la categorie c et il répresente le pays p.*/  

LesEpreuves (<ins>numEp</ins>, nomEp, formeEp, categorieEp, nbSportifsEp, dateEp, nomDi)  
/* <nu,n,f,c,nb,d,nd> L'épreuve de forme f et catégorie c, qui fait partie de la discipline nd est identifiée par le numéro nu. Elle a un nombre nb de sportifs et elle se déroule à la date d. */   

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

LesSportifs[numSp] ∩ LesEquipes[numEq] = ∅
 
On peut aussi ajouter les vues suivantes:  
  - __nbEquipiers__ pour calculer le nombre d'equipiers d'une equipe  
 ```sql
  CREATE VIEW LesNbsEquipiers (  
    numEq,  
    nbEquipiers  
)   AS SELECT numEq, COUNT(numSp) AS nbEquipiers  
    FROM EstEquipier  
    GROUP BY numEq;
  ```
  
  - __LesAgesSportifs__ pour calculer l'age d'un sportif  
  ```sql 
  CREATE VIEW LesAgesSportifs(  
    numSp,    
    nomSp,  
    prenomSp,  
    age  
) AS SELECT  
    numSp,  
    nomSp,  
    prenomSp,  
    strftime('%Y', 'now') - strftime('%Y', dateNaissance)  
FROM LesSportifs;  
  ```
