CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS
$$
BEGIN
    RETURN QUERY
    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.phone
    FROM PhoneBook
    WHERE PhoneBook.name ILIKE '%' || pattern || '%'
       OR PhoneBook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_or_update_user(user_name TEXT, user_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = user_name) THEN
        UPDATE PhoneBook SET phone = user_phone WHERE name = user_name;
    ELSE
        INSERT INTO PhoneBook(name, phone) VALUES (user_name, user_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(user_list TEXT[][])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    name TEXT;
    phone TEXT;
BEGIN
    WHILE i <= array_length(user_list, 1) LOOP
        name := user_list[i][1];
        phone := user_list[i][2];

        IF phone ~ '^\+7\d{10}$' THEN
            CALL insert_or_update_user(name, phone);
        ELSE
            RAISE NOTICE 'Invalid phone for %: %', name, phone;
        END IF;

        i := i + 1;
    END LOOP;
END;
$$;

CREATE OR REPLACE FUNCTION get_users(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS
$$
BEGIN
    RETURN QUERY
    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.phone
    FROM PhoneBook
    ORDER BY PhoneBook.id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM PhoneBook WHERE name = identifier OR phone = identifier;
END;
$$;
