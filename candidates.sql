CREATE DATABASE resume_db;
USE resume_db;
CREATE TABLE candidates(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),skill_score FLOAT,ai_score FLOAT,final_score FLOAT);