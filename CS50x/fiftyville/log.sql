-- Keep a log of any SQL queries you execute as you solve the mystery.

-- First of all, .schema to find out all tables structures

-- July 28
-- Humphrey street

-- sqlite3 fiftyville.db
-- .schema

-- WHO THE THIEF IS
-- WHERE THE THIEF ESCAPED TO
-- WHO THIEFS ACCOMPLICE

-- - Tips
-- crime_scene_reports

-- once you know primary/keys to correlate tables
-- Maintain a list of suspects

-- Find crime scene data with data from problem set
SELECT description, year
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND Street = 'Humphrey Street';

-- two reports, one theft at 10:15am, one littering at 16:36
-- Interview with 3 witnesses today > lets check the interviews

SELECT id, name, transcript
FROM interviews
WHERE month = 7 AND day = 28 AND year = 2025;

-- Ruth, Eugene and Raymond
-- cars that left parking lot within 10 minutes from the theft -> 10:05 am to 10:25 am

SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2025
AND hour = 10 AND minute BETWEEN 5 AND 25
AND activity = 'exit';

-- find whom are these plates from

SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND year = 2025
    AND hour = 10 AND minute BETWEEN 5 AND 25
    AND activity = 'exit'
);

-- 1 LIST OF SUSPECTS THIEF: VANESSA, BARRY, IMAN, SOFIA, LUCA, DIANA, KELSEY, BRUCE

-- the thieft withdrew money from tha ATM machine on Leggett Street earlier that morning (28/07)

SELECT account_number
FROM atm_transactions
WHERE month = 7 AND day = 28 AND year = 2025
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Find whom are these account from
SELECT *
FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7 AND day = 28 AND year = 2025
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
    )
);

-- 1 LIST OF SUSPECTS THIEF: VANESSA, BARRY, IMAN, SOFIA, LUCA, DIANA, KELSEY, BRUCE
-- 2 LIST OF SUSPECTS THIEF: KENNY, IMAN, BENISTA, TAYLOR, BROOKE, LUCA, DIANA, BRUCE
-- INTERSECTION OF BOTH: IMAN, LUCA, DIANA, BRUCE

-- when they were leaving the bakery - before the car lefting the park - the thief called someone for less than minute

SELECT *
FROM phone_calls
WHERE month = 7 AND day = 28 AND year = 2025
AND duration < 60;

-- find who the caller is

SELECT *
FROM people
WHERE phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND year = 2025
    AND duration < 60
);

-- 1 LIST OF SUSPECTS THIEF: VANESSA, BARRY, IMAN, SOFIA, LUCA, DIANA, KELSEY, BRUCE
-- 2 LIST OF SUSPECTS THIEF: KENNY, IMAN, BENISTA, TAYLOR, BROOKE, LUCA, DIANA, BRUCE
-- 3 LIST OF SUSPECTS THIEF: KENNY, SOFIA, BENISTA, TAYLOR, DIANA, KELSEY, BRUCE, CARINA
-- INTERSECTION OF BOTH 3: DIANA, BRUCE

-- Find who they called to:

SELECT *
FROM people
WHERE phone_number IN (
    SELECT receiver
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND year = 2025
    AND duration < 60
    AND (caller = '(770) 555-1861' OR caller = '(367) 555-5533')
);

-- accomplise is either Philip (diana) with a passport number!! or Robin (Bruce) which does not have a passport number
-- guess is THIEF: DIANA, accomplish Philip, lets find where they were going to:

SELECT *
FROM people
WHERE id = 864400 or id = 847116;

-- the accomplice bhought a the earliest flight ticket from Fiftyville to another place by the next day (29/07)
-- find airport id from Fiftyville

SELECT *
FROM airports
WHERE city = 'Fiftyville';
-- id 8

SELECT *
FROM flights
WHERE month = 7 AND day = 29 AND year = 2025
AND origin_airport_id = 8
ORDER BY hour ASC
LIMIT 1;

-- DestinatioN airport 4, flight ID 36

SELECT *
FROM airports
WHERE id = '4';
-- destination was New York City
-- Lest just check if Robin (5773159633) or Diana (3592750733) where on the passenger list of that flight:
SELECT *
FROM passengers
WHERE flight_id = '36';

-- robin is, on seat 4A, DIANA is not :o oh no;
SELECT *
FROM people
WHERE passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id = '36'
    );
-- now i think it is bruce 100% and philip i'm not sure

-- accomplise is either Philip (diana) with a passport number!! or Robin (bruce) which does not have a passport number

SELECT *
FROM people
WHERE phone_number IN (
    SELECT receiver
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND year = 2025
    AND duration < 60
    AND caller = '(367) 555-5533'
);

-- robin is the accomplish
-- So, bruce, robin and new york
