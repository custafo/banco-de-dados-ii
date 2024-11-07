CREATE VIEW cliente_do_mes AS
SELECT 
    c.id, c.nome, COUNT(v.id) AS total_compras
FROM 
    cliente c 
JOIN 
    venda v ON c.id=v.id_cliente
WHERE
    MONTH(v.dia) >= MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
    AND YEAR(v.dia) >= YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
ORDER BY
    total_compras DESC
LIMIT 1
;