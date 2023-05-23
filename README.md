# Sparkify Data Warehouse - My Project Journey

## Project Overview

I've been given the responsibility to migrate our growing database of songs and user activity logs onto the cloud. My task involved designing an ETL pipeline that takes data from S3, stages it in Redshift, and transforms it into a set of dimensional tables. This solution empowers the analytics team to find out more about what songs our users are listening to.

## My Approach

I began by understanding the two primary datasets stored in S3 - one consisting of JSON logs on user activity and another with JSON metadata on the songs in the app. Both datasets are in JSON format, with logs partitioned by year and month, and song files partitioned by the first three letters of each song's track ID.

### Schema Design

My next step was to design a star schema optimized for queries on song play analysis. This schema includes one fact table - `songplays`, and four dimension tables - `users`, `songs`, `artists`, and `time`. I chose the star schema because of its simplicity and high performance, which suits the needs of Sparkify's analytics team to run complex queries.

### ETL Pipeline

To execute the ETL process, I created Python scripts that performed the following:

1. `create_tables.py`: Connects to the Redshift cluster, drops any existing tables, and creates new tables.
2. `etl.py`: Loads data from S3 into staging tables on Redshift, and then transforms the data into the dimensional tables.
3. `sql_queries.py`: Contains all the SQL queries executed in the other scripts.

## Final Thoughts

I had to ensure that I was using the right keys, roles, region, etc. for setting up the Redshift cluster, IAM role, and other security considerations. Additionally, I learned the important fact that the `SERIAL` command in Postgres is not supported in Redshift. The equivalent in Redshift is `IDENTITY(0,1)`.

With the completion of this project, I have successfully moved the data onto the cloud, and created a robust and efficient pipeline for the analytics team to utilize. They can now run queries to fetch crucial insights, for example, finding the most popular song, or the peak usage time of the app.

