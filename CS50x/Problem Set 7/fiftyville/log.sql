-- All you know is that the theft took place on July 28, 2023 and that it took place on Humphrey Street.

-- SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28;
SELECT description FROM crime_scene_reports WHERE id = 295;

    -- 1015 280723, Humphrey Street Bakery, 3 witnesses interviewed


-- SELECT * FROM interviews WHERE month = 7 AND day = 28;
SELECT transcript FROM interviews WHERE id = 161 OR id = 162 OR id = 163;

    -- 1015-1025 left bakery parking lot
    -- Morning < 1015 Leggett Street ATM withdrawal
    -- Planned to take flight on 290723, earliest flight out of Fiftyville, call < 1 minute


-- SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28;
SELECT hour, minute, activity, license_plate FROM bakery_security_logs WHERE id >= 260 AND id <= 267;

    -- | 10   | 16     | exit     | 5P2BI95       |
    -- | 10   | 18     | exit     | 94KL13X       |
    -- | 10   | 18     | exit     | 6P58WS2       |
    -- | 10   | 19     | exit     | 4328GD8       |
    -- | 10   | 20     | exit     | G412CB7       |
    -- | 10   | 21     | exit     | L93JTIZ       |
    -- | 10   | 23     | exit     | 322W7JE       |
    -- | 10   | 23     | exit     | 0NTHK55       |


-- SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
SELECT account_number, amount FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

    -- | 28500762       | 48     |
    -- | 28296815       | 20     |
    -- | 76054385       | 60     |
    -- | 49610011       | 50     |
    -- | 16153065       | 80     |
    -- | 25506511       | 20     |
    -- | 81061156       | 30     |
    -- | 26013199       | 35     |


-- SELECT * FROM airports;
SELECT * FROM airports WHERE city = 'Fiftyville';

    -- +----+--------------+-----------------------------+------------+
    -- | id | abbreviation |          full_name          |    city    |
    -- +----+--------------+-----------------------------+------------+
    -- | 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
    -- +----+--------------+-----------------------------+------------+


SELECT * FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29 AND hour < 12;

    -- +----+-------------------+------------------------+------+-------+-----+------+--------+
    -- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
    -- +----+-------------------+------------------------+------+-------+-----+------+--------+
    -- | 36 | 8                 | 4                      | 2023 | 7     | 29  | 8    | 20     |
    -- | 43 | 8                 | 1                      | 2023 | 7     | 29  | 9    | 30     |
    -- +----+-------------------+------------------------+------+-------+-----+------+--------+


-- SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;
SELECT caller, receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;

    -- | (130) 555-0289 | (996) 555-8899 |
    -- | (499) 555-9472 | (892) 555-8872 |
    -- | (367) 555-5533 | (375) 555-8161 |
    -- | (499) 555-9472 | (717) 555-1342 |
    -- | (286) 555-6063 | (676) 555-6554 |
    -- | (770) 555-1861 | (725) 555-3243 |
    -- | (031) 555-6622 | (910) 555-3251 |
    -- | (826) 555-1652 | (066) 555-9701 |
    -- | (338) 555-6650 | (704) 555-2131 |


SELECT * FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');

    -- +----------------+-----------+---------------+
    -- | account_number | person_id | creation_year |
    -- +----------------+-----------+---------------+
    -- | 49610011       | 686048    | 2010          |
    -- | 26013199       | 514354    | 2012          |
    -- | 16153065       | 458378    | 2012          |
    -- | 28296815       | 395717    | 2014          |
    -- | 25506511       | 396669    | 2014          |
    -- | 28500762       | 467400    | 2014          |
    -- | 76054385       | 449774    | 2015          |
    -- | 81061156       | 438727    | 2018          |
    -- +----------------+-----------+---------------+


SELECT * FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29 AND hour < 12);

    -- +-----------+-----------------+------+
    -- | flight_id | passport_number | seat |
    -- +-----------+-----------------+------+
    -- | 36        | 7214083635      | 2A   |
    -- | 36        | 1695452385      | 3B   |
    -- | 36        | 5773159633      | 4A   |
    -- | 36        | 1540955065      | 5C   |
    -- | 36        | 8294398571      | 6C   |
    -- | 36        | 1988161715      | 6D   |
    -- | 36        | 9878712108      | 7A   |
    -- | 36        | 8496433585      | 7B   |
    -- | 43        | 7597790505      | 7B   |
    -- | 43        | 6128131458      | 8A   |
    -- | 43        | 6264773605      | 9A   |
    -- | 43        | 3642612721      | 2C   |
    -- | 43        | 4356447308      | 3B   |
    -- | 43        | 7441135547      | 4A   |
    -- +-----------+-----------------+------+


SELECT *
  from people
 WHERE id IN

    (SELECT person_id
       FROM bank_accounts
      WHERE account_number IN

        (SELECT account_number
           FROM atm_transactions
          WHERE month = 7 AND
                  day = 28 AND
         atm_location = 'Leggett Street' AND
     transaction_type = 'withdraw')) AND

license_plate IN

    (SELECT license_plate
       FROM bakery_security_logs
      WHERE id >= 260 AND
            id <= 267) AND

phone_number IN

    (SELECT caller
       FROM phone_calls
      WHERE month = 7 AND
              day = 28 AND
         duration < 60) AND

passport_number IN

    (SELECT passport_number
       FROM passengers
      WHERE flight_id IN

        (SELECT id
           FROM flights
          WHERE origin_airport_id = 8 AND
                            month = 7 AND
                              day = 29 AND
                             hour < 12));

    -- +--------+-------+----------------+-----------------+---------------+
    -- |   id   | name  |  phone_number  | passport_number | license_plate |
    -- +--------+-------+----------------+-----------------+---------------+
    -- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
    -- +--------+-------+----------------+-----------------+---------------+


SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE id = (SELECT flight_id FROM passengers WHERE passport_number = '5773159633'));

    -- +---------------+       -- forgot its first flight, id is 36...
    -- |     city      |
    -- +---------------+
    -- | New York City |
    -- +---------------+


SELECT * FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE caller = '(367) 555-5533' AND month = 7 AND day = 28 AND duration < 60);

    -- +--------+-------+----------------+-----------------+---------------+
    -- |   id   | name  |  phone_number  | passport_number | license_plate |
    -- +--------+-------+----------------+-----------------+---------------+
    -- | 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
    -- +--------+-------+----------------+-----------------+---------------+


-- Grey out table when information has been retrieved
--
--CREATE TABLE crime_scene_reports (
--    id INTEGER,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    street TEXT,
--    description TEXT,
--    PRIMARY KEY(id)
--);
--CREATE TABLE interviews (
--    id INTEGER,
--    name TEXT,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    transcript TEXT,
--    PRIMARY KEY(id)
--);
--CREATE TABLE atm_transactions (
--    id INTEGER,
--    account_number INTEGER,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    atm_location TEXT,
--    transaction_type TEXT,
--    amount INTEGER,
--    PRIMARY KEY(id)
--);
--CREATE TABLE bank_accounts (
--    account_number INTEGER,
--    person_id INTEGER,
--    creation_year INTEGER,
--    FOREIGN KEY(person_id) REFERENCES people(id)
--);
--CREATE TABLE airports (
--    id INTEGER,
--    abbreviation TEXT,
--    full_name TEXT,
--    city TEXT,
--    PRIMARY KEY(id)
--);
--CREATE TABLE flights (
--    id INTEGER,
--    origin_airport_id INTEGER,
--    destination_airport_id INTEGER,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    hour INTEGER,
--    minute INTEGER,
--    PRIMARY KEY(id),
--    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
--    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
--);
--CREATE TABLE passengers (
--    flight_id INTEGER,
--    passport_number INTEGER,
--    seat TEXT,
--    FOREIGN KEY(flight_id) REFERENCES flights(id)
--);
--CREATE TABLE phone_calls (
--    id INTEGER,
--    caller TEXT,
--    receiver TEXT,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    duration INTEGER,
--    PRIMARY KEY(id)
--);
--CREATE TABLE people (
--    id INTEGER,
--    name TEXT,
--    phone_number TEXT,
--    passport_number INTEGER,
--    license_plate TEXT,
--    PRIMARY KEY(id)
--);
--CREATE TABLE bakery_security_logs (
--    id INTEGER,
--    year INTEGER,
--    month INTEGER,
--    day INTEGER,
--    hour INTEGER,
--    minute INTEGER,
--    activity TEXT,
--    license_plate TEXT,
--    PRIMARY KEY(id)
--);

