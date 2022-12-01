DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS MedaillesOr;
DROP TABLE IF EXISTS MedaillesArgent;
DROP TABLE IF EXISTS MedaillesBronze;
DROP TABLE IF EXISTS EstEquipier;
DROP TABLE IF EXISTS LesEquipes;
DROP TABLE IF EXISTS LesEpreuves;
DROP TABLE IF EXISTS LesSportifs;
DROP TABLE IF EXISTS LesDisciplines;
DROP VIEW IF EXISTS LesAgesSportifs;
DROP VIEW IF EXISTS LesNbsEquipiers;

DROP TRIGGER IF EXISTS exaequo_or;
DROP TRIGGER IF EXISTS exaequo_argent;
DROP TRIGGER IF EXISTS exaequo_bronze;
DROP TRIGGER IF EXISTS medailles_participant_argent;
DROP TRIGGER IF EXISTS medailles_participant_bronze;
DROP TRIGGER IF EXISTS categorie_participant;
DROP TRIGGER IF EXISTS num_sportif;
DROP TRIGGER IF EXISTS num_equipe;

