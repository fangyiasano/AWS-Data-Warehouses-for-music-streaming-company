
CREATE DATABASE IF NOT EXISTS SparkifyDB;
USE SparkifyDB;


DROP TABLE IF EXISTS songplays;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS time;


CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender CHAR(1),
    level VARCHAR(10)
);


CREATE TABLE songs (
    song_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(100),
    artist_id VARCHAR(50) NOT NULL,
    year INT,
    duration FLOAT
);


CREATE TABLE artists (
    artist_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT
);


CREATE TABLE time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday VARCHAR(10)
);


CREATE TABLE songplays (
    songplay_id INT AUTO_INCREMENT PRIMARY KEY,
    start_time TIMESTAMP NOT NULL REFERENCES time(start_time),
    user_id INT NOT NULL REFERENCES users(user_id),
    level VARCHAR(10),
    song_id VARCHAR(50) NOT NULL REFERENCES songs(song_id),
    artist_id VARCHAR(50) NOT NULL REFERENCES artists(artist_id),
    session_id INT,
    location VARCHAR(100),
    user_agent VARCHAR(255)
);

SHOW TABLES;
