CREATE PROCEDURE reajuste(pct_increase DECIMAL(5, 2))
BEGIN
    
    UPDATE prato
    SET valor = valor * (1 + (pct_increase / 100));

END ;