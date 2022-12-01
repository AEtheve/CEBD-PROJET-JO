-- TODO 3.3 Créer un trigger pertinent

CREATE TRIGGER IF NOT EXISTS exaequo
BEFORE INSERT ON MedaillesOr FOR EACH ROW
WHEN
(
    SELECT numP
    FROM MedaillesOr
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille d''or pour cette épreuve');
END
WHEN
(
    SELECT numP
    FROM MedaillesArgent
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille d''argent pour cette épreuve');
END
WHEN
(
    SELECT numP
    FROM MedaillesBronze
    WHERE numEp = NEW.numEp
) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'Il y a déjà une médaille de bronze pour cette épreuve');
END;


