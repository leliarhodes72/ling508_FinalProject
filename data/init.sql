CREATE DATABASE tarot;

USE tarot;

CREATE TABLE TarotCards (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    upright_meaning_id INT,
    reversed_meaning_id INT,
    numerology_id INT,
    element_id INT,
    astrological_body_id INT,
    FOREIGN KEY (upright_meaning_id) REFERENCES Meanings(id),
    FOREIGN KEY (reversed_meaning_id) REFERENCES Meanings(id),
    FOREIGN KEY (numerology_id) REFERENCES Numerology(id),
    FOREIGN KEY (element_id) REFERENCES Elements(id),
    FOREIGN KEY (astrological_body_id) REFERENCES AstrologicalBodies(id)
);

CREATE TABLE Meanings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    text TEXT NOT NULL
);

CREATE TABLE AstrologicalBodies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    significance TEXT
);

CREATE TABLE Elements (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    significance TEXT
);

CREATE TABLE Keywords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    word VARCHAR(255) NOT NULL
);