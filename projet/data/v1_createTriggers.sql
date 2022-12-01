CREATE TRIGGER IF NOT EXISTS exaequo_or
BEFORE INSERT ON MedaillesOr FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesOr
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille pour cette épreuve');
END/

CREATE TRIGGER IF NOT EXISTS exaequo_argent
BEFORE INSERT ON MedaillesArgent FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesArgent
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille pour cette épreuve');
END/

CREATE TRIGGER IF NOT EXISTS exaequo_bronze
BEFORE INSERT ON MedaillesBronze FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesBronze
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille pour cette épreuve');
END/

CREATE TRIGGER IF NOT EXISTS medailles_participant_argent
BEFORE INSERT ON MedaillesArgent FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesOr
    WHERE numP = NEW.numP AND numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Un participant peut gagner qu''une medaille pour une epreuve donée.');
END/

CREATE TRIGGER IF NOT EXISTS medailles_participant_bronze
BEFORE INSERT ON MedaillesBronze FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesOr
    WHERE numP = NEW.numP AND numEp = NEW.numEp
    UNION
    SELECT numP
    FROM MedaillesArgent
    WHERE numP = NEW.numP AND numEp = NEW.numEp

) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Un participant peut gagner qu''une medaille pour une epreuve donée.');
END/

CREATE TRIGGER IF NOT EXISTS categorie_participant
BEFORE INSERT ON LesInscriptions FOR EACH ROW
WHEN
(
    SELECT categorieSp
    FROM LesSportifs
    WHERE numSp = NEW.numP
) != (
    SELECT categorieEp
    FROM LesEpreuves
    WHERE numEp = NEW.numEp
)
BEGIN
    SELECT RAISE(ABORT, 'Un participant peut seulement s''inscrire a une epreuve qui correspond a sa categorie.');
END/

CREATE TRIGGER IF NOT EXISTS num_sportif
BEFORE INSERT ON LesSportifs FOR EACH ROW
WHEN
(
    NEW.numSp < 1000 OR NEW.numSp > 1500
)
BEGIN
    SELECT RAISE(ABORT, 'Le numéro du sportif doit être entre 1000 et 1500');
END/

CREATE TRIGGER IF NOT EXISTS num_equipe
BEFORE INSERT ON LesEquipes FOR EACH ROW
WHEN
(
    NEW.numEq < 1 OR NEW.numEq > 100
)
BEGIN
    SELECT RAISE(ABORT, 'Le numéro de l''equipe doit être entre 1 et 100');
END/

