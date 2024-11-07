CREATE PROCEDURE sorteio ()
BEGIN

    DECLARE selected_client_id INT;

    SELECT id INTO selected_client_id
    FROM cliente
    ORDER BY RAND()
    LIMIT 1;

    UPDATE cliente
    SET pontos = pontos + 100
    WHERE id = selected_client_id;
    
END;