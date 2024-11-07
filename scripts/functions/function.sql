
CREATE FUNCTION calcular_pontos(purchase_amount DECIMAL(10, 2))
RETURNS INT 
DETERMINISTIC 
BEGIN
    DECLARE points INT;
    IF purchase_amount >= 10 THEN
        SET points = FLOOR(purchase_amount / 10); 
    ELSE
        SET points = 0;
    END IF;

    RETURN points;
END ;
