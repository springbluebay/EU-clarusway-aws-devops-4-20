CREATE TABLE phonebook_db.phonebook(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    number VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO phonebook_db.phonebook (name, number)
    VALUES
        ("Serdar", "1234567890"),
        ("Mustafa", "6785443232"),
        ("Ozkan", "6785443232"),
        ("Muhammed", "6785443232"),
        ("Vincenzo Altobelli", "876543554");