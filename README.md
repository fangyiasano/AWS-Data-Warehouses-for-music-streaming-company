# AWS Data Warehouse for Music Streaming Company

## Project Overview

This project entails building an ETL pipeline that extracts music streaming data from AWS S3, stages it in AWS Redshift, and transforms it into a set of dimensional tables for the analytics team at Sparkify. This enables the team to gain insights into user activities on the music streaming app.

## Purpose

The database and ETL pipeline were designed to help the music streaming company analyze their data more effectively, focusing on understanding what songs users are listening to. With this data model, the company can optimize song selections, user engagement, and ultimately, their marketing strategies.

## Database Schema Design

The schema used for this project is the **Star Schema**, optimized for queries on song play analysis. This schema design provides a simple and intuitive way to query the data, focusing on read operations for analytics purposes.
<img width="831" alt="image" src="https://github.com/user-attachments/assets/e17fc8cd-43fe-401f-a5a1-9e64397a3eff">

### Fact Table
- **songplays** - Records in event data associated with song plays (page = 'NextSong')
  - `songplay_id` (INT) - ID of each user song play 
  - `start_time` (TIMESTAMP) - Timestamp of song play
  - `user_id` (INT) - ID of the user
  - `level` (VARCHAR) - User's level (free or paid)
  - `song_id` (VARCHAR) - ID of the song played
  - `artist_id` (VARCHAR) - ID of the artist
  - `session_id` (INT) - ID of the user session
  - `location` (VARCHAR) - User's location
  - `user_agent` (VARCHAR) - Agent used by the user to access the service

### Dimension Tables
- **users** - Users in the app
  - `user_id` (INT) - User ID
  - `first_name` (VARCHAR) - User first name
  - `last_name` (VARCHAR) - User last name
  - `gender` (VARCHAR) - User gender
  - `level` (VARCHAR) - User level (free or paid)

- **songs** - Songs in the music database
  - `song_id` (VARCHAR) - Song ID
  - `title` (VARCHAR) - Song title
  - `artist_id` (VARCHAR) - Artist ID for the song
  - `year` (INT) - Year of song release
  - `duration` (FLOAT) - Song duration in milliseconds

- **artists** - Artists in the music database
  - `artist_id` (VARCHAR) - Artist ID
  - `name` (VARCHAR) - Artist name
  - `location` (VARCHAR) - Location of the artist
  - `latitude` (FLOAT) - Latitude of the artist's location
  - `longitude` (FLOAT) - Longitude of the artist's location

- **time** - Timestamps of records in songplays broken down into specific units
  - `start_time` (TIMESTAMP) - Timestamp of the record
  - `hour` (INT) - Hour extracted from the timestamp
  - `day` (INT) - Day extracted from the timestamp
  - `week` (INT) - Week of the year extracted from the timestamp
  - `month` (INT) - Month extracted from the timestamp
  - `year` (INT) - Year extracted from the timestamp
  - `weekday` (INT) - The weekday extracted from the timestamp


## ETL Pipeline
The ETL pipeline follows these steps:

1. Extract data from S3: Load JSON input data (song data and log data) from S3.
2. Stage data in Redshift: Use the COPY command to load the data into staging tables on Redshift.
3. Transform data into star schema: Execute SQL statements to create the schema in Redshift and populate the fact and dimension tables.

To execute the ETL process, I created Python scripts that performed the following:

1. `create_tables.py`: Script to create fact and dimension tables for the star schema in Redshift.
2. `etl.py`: Script to load data from S3 into staging tables on Redshift and then process that data into the analytics tables.
3. `sql_queries.py`: Contains all the SQL queries executed in the other scripts.

## Example Queries

Below are some example queries that could be run to generate insights from the data:

### Query 1: Most Played Song
```sql
SELECT songs.title, COUNT(*) AS play_count
FROM songplays
JOIN songs ON songplays.song_id = songs.song_id
GROUP BY songs.title
ORDER BY play_count DESC
LIMIT 1;
```

### Query 2: Peak Usage Time by Hour
```sql
SELECT time.hour, COUNT(*) AS total_plays
FROM songplays
JOIN time ON songplays.start_time = time.start_time
GROUP BY time.hour
ORDER BY total_plays DESC
LIMIT 1;
