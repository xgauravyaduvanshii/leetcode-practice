-- 1527. Patients With a Condition (Easy)
-- https://leetcode.com/problems/patients-with-a-condition/
-- Submission 2200124856 -- Accepted, MySQL
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
