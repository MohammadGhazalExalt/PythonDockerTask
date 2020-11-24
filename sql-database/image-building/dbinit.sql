CREATE DATABASE system_data;
USE system_data;
CREATE TABLE disk_stats (used INT, free INT, timestamp DATETIME);
CREATE TABLE mem_stats (used INT, free INT, timestamp DATETIME);
CREATE TABLE cpu_stats (idle INT, timestamp DATETIME);

