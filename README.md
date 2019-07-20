# Logs Analysis
Logs Analysis is a reporting tool that prints out reports (in plain text) based on a newspaper articles database, as well as the web server log for the newspaper site.
# Getting Started
## Prerequisites

## Installing
```
$ git clone https://github.com/AboSalaah/LogsAnalysis.git
$ cd ../logs_analysis_project
$ python LogsAnalysis.py
```
## Technologies
Project is created with: 
* Python 3.7.4
* PostgreSQL

## Usage
```python
import LogsAnalysis

LogsAnalysis.mostPopularArticles() # returns the most popular three articles of all time
LogsAnalysis.mostPopularAuthors() # returns the most popular authors of all time
LogsAnalysis.highErrorDays() # returns the days that have more than 1% of requests lead to errors
```