CREATE DATABASE IF NOT EXISTS parque_diversoes;
USE parque_diversoes;

CREATE TABLE atracoes(
	id INT NOT NULL AUTO_INCREMENT KEY,
    nome VARCHAR(67),
    estado VARCHAR(67)
);
INSERT INTO  atracoes (nome , estado) VALUES ("maquina láele", "péssimo");
INSERT INTO  atracoes (nome , estado) VALUES ("maquina vacilossauro", "mediocre");
INSERT INTO  atracoes (nome , estado) VALUES ("maquina apodrecedora de cerebros", "ótimo para a função. naturalmente péssimo.");
SELECT * FROM atracoes