CREATE DATABASE configuratore_automobili; 

CREATE TABLE IF NOT EXISTS app_user (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    ruolo VARCHAR(20) NOT NULL DEFAULT 'user'
);