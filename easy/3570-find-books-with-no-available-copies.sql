-- 3570. Find Books with No Available Copies (Easy)
-- https://leetcode.com/problems/find-books-with-no-available-copies/
-- Submission 2200136970 -- Accepted, MySQL
SELECT b.book_id, b.title, b.author, b.genre, b.publication_year,
    COUNT(r.record_id) AS current_borrowers
FROM library_books b
JOIN borrowing_records r ON b.book_id = r.book_id AND r.return_date IS NULL
GROUP BY b.book_id, b.title, b.author, b.genre, b.publication_year, b.total_copies
HAVING COUNT(r.record_id) = b.total_copies
ORDER BY current_borrowers DESC, b.title ASC;
