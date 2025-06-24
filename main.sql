SELECT 
  A,
  B,
  C,
  NOT (
    (A AND B) OR 
    (B AND (B OR C))
  ) AS Q
FROM 
  (SELECT 1 AS A, 0 AS B, 1 AS C) AS inputs;