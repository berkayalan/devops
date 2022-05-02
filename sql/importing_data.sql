COPY name_basics(nconst,primary_name,birth_year,death_year,primary_profession,known_for_titles)  
FROM '/Applications/PostgreSQL 13/name.basics.v1.csv' DELIMITER ',' CSV HEADER;


