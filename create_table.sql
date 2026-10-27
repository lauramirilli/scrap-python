SELECT SYSDATE FROM DUAL;

CREATE TABLE quotes (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    quote_text VARCHAR2(1000) NOT NULL,
    author_name VARCHAR2(200) NOT NULL
);

INSERT INTO quotes (quote_text, author_name) VALUES ('Ser ou não ser', 'Shakespeare');

SELECT * FROM quotes;