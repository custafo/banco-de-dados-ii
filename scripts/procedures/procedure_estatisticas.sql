CREATE PROCEDURE estatisticas()
BEGIN

    SELECT p.nome AS produto_mais_vendido,
           SUM(v.quantidade) AS total_vendido,
           SUM(v.valor * v.quantidade) AS valor_gerado,

           (SELECT MONTH(dia) 
            FROM venda
            WHERE id_prato = v.id_prato
            GROUP BY MONTH(dia)
            ORDER BY SUM(quantidade) DESC
            LIMIT 1) AS mes_maior_venda,

           (SELECT MONTH(dia) 
            FROM venda
            WHERE id_prato = v.id_prato
            GROUP BY MONTH(dia)
            ORDER BY SUM(quantidade) ASC
            LIMIT 1) AS mes_menor_venda
           
    FROM venda v
    JOIN prato p ON v.id_prato = p.id
    GROUP BY v.id_prato
    ORDER BY total_vendido DESC
    LIMIT 1;

    SELECT p.nome AS produto_menos_vendido,
           SUM(v.quantidade) AS total_vendido,
           SUM(v.valor * v.quantidade) AS valor_gerado,
           
           (SELECT MONTH(dia) 
            FROM venda
            WHERE id_prato = v.id_prato
            GROUP BY MONTH(dia)
            ORDER BY SUM(quantidade) DESC
            LIMIT 1) AS mes_maior_venda,
            
           (SELECT MONTH(dia) 
            FROM venda
            WHERE id_prato = v.id_prato
            GROUP BY MONTH(dia)
            ORDER BY SUM(quantidade) ASC
            LIMIT 1) AS mes_menor_venda
           
    FROM venda v
    JOIN prato p ON v.id_prato = p.id
    GROUP BY v.id_prato
    ORDER BY total_vendido ASC
    LIMIT 1;

END;