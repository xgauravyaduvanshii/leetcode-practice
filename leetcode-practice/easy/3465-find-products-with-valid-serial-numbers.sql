-- 3465. Find Products with Valid Serial Numbers (Easy)
-- https://leetcode.com/problems/find-products-with-valid-serial-numbers/
-- Submission 2200136408 -- Accepted, MySQL
-- NOTE: the first submission (2200135902) was Wrong Answer 16/19: the
-- pattern matched "ASN4321-8765", but a serial must not sit inside a
-- longer alphanumeric token. BINARY REGEXP and COLLATE fixes failed
-- with charset errors (binary vs utf8mb4_general_ci; utf8mb4_bin vs
-- the utf8mb3 column; utf8mb3_bin vs the utf8mb4 pattern literal).
-- The working fix converts the column to utf8mb4 and applies COLLATE
-- utf8mb4_bin to both sides for a case-sensitive match, with boundary
-- guards so a 5th digit (e.g. SN1234-56789) also disqualifies.
SELECT product_id, product_name, description
FROM products
WHERE CONVERT(description USING utf8mb4) COLLATE utf8mb4_bin
    REGEXP '([^A-Za-z0-9_]|^)SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9_]|$)' COLLATE utf8mb4_bin
ORDER BY product_id;
