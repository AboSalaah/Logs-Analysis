# Logs Analysis
Logs Analysis is a reporting tool that prints out reports (in plain text) based on a newspaper articles database, as well as the web server log for the newspaper site.
## Getting Started

### prerequisites
Logs Analysis uses a virtual machine (VM) to run an SQL database server and a web app that uses it.

Logs Analysis requires the following to run:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) the software that actually runs the virtual machine
* [Vagrant](https://www.vagrantup.com/downloads.html) is the software that configures the VM and lets you share files between your host computer and the VM's filesystem
* [VM configuration](https://github.com/udacity/fullstack-nanodegree-vm)
* [News Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) the data the project operates on.

After the installation, change to a folder called vagrant inside the VM configuration directory

```
$ cd ../VM configuration director/vagrant
```
* Start the virtual machine
```
$ vagrant up
```
This will cause Vagrant to download the Linux operating system and install it.

* run ```vagrant ssh``` to log in to 
your newly installed Linux VM
```
$ vagrant ssh
```
 * Unzip the **News Data** file after downloading it. The file inside is called **newsdata.sql**. Put this file into the **vagrant** directory, which is shared with your virtual machine.

* Load the site's data into your local database
```
$ cd ../vagrant
$ psql -d news -f newsdata.sql
```


### Installing

```
$ git clone https://github.com/AboSalaah/Logs-Analysis.git
```
### Running the code
* Put the downloaded project directory inside vagrant directory.
* Inside the VM, change directory to ```/vagrant``` and run the project.
```
$ cd /vagrant
$ cd /LogsAnalysis
$ python LogsAnalysis.py
```
### Technologies
Project is created with: 
* Python 3.7.4
* PostgreSQL

### Usage
```python
import LogsAnalysis

LogsAnalysis.mostPopularArticles() # returns the most popular three articles of all time
LogsAnalysis.mostPopularAuthors() # returns the most popular authors of all time
LogsAnalysis.highErrorDays() # returns the days that have more than 1% of requests lead to errors
```