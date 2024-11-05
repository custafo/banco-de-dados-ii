
CREATE FUNCTION calculate_points(purchase_amount DECIMAL(10, 2)) --receives decimal value of the purchase
RETURNS INT --returns an int
DETERMINISTIC --for optimization purposes on mysql
BEGIN
    DECLARE points INT;
    IF purchase_amount >= 10 THEN
        SET points = FLOOR(purchase_amount / 10); --rounding up points to full ints 
    ELSE
        SELECT 'Essa compra não gera pontos por estar abaixo de 10 reais' AS message;
    END IF;

    RETURN points;
END ;
