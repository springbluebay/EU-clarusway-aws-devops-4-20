# 05-06-2020
# AWS Lab Session - Callahan
# Relational Database Service (RDS) 
# Session starts at 6pm

# launched 2 instances of Amazon Linux 2 and name them as MySQL DB Server, and MariaDB Server
# configure security group to allow SSH connection (Port 22) and sql connection (Port 3306)

# Part 1 - Creating EC2 Instance and Installing MariaDB Server

# Launch EC2 Instance.

# AMI: Amazon Linux 2
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere
#   - MYSQL/Aurora  -----> 3306  -----> Anywhere

# Connect to EC2 instance with SSH.

# Update yum package management and install MariaDB server.
sudo yum update -y
sudo yum install mariadb-server -y

# start mariadb service
sudo systemctl start mariadb
# show status of mariadb service
sudo systemctl status mariadb
# enable mariadb service, so that mariadb service will be activated on restarts
sudo systemctl enable mariadb
-----------------------------
# Part 2 - Connecting and Configuring MariaDB Database

# connect to the mariadb-server and open mysql cli with root user, no password set as default
mysql -u root

# show default databases in the Mariadb server
SHOW databases;

# Choose a database (mysql db) to work with. ⚠️ Caution: We have chosen mysql db as demo purposes, normally database mysql is used by server itself, it shouldn't be changed or altered by the user.
USE mysql;

# show tables within the mysql db
SHOW tables;

# show users defined in the db server currently.
SELECT Host, User, Password FROM user;

# close the mysql terminal
EXIT;

# setup secure installation of MariaDB
# No root password for root so 'Enter' for first question,
# Then set root password: 'root1234' and yes 'y' to all remaining ones.
sudo mysql_secure_installation

Enter current password for root (enter for none): "enter"
Set root password? [Y/n] "y"
Remove anonymous users? [Y/n] "y"
Disallow root login remotely? [Y/n] "y"
Remove test database and access to it? [Y/n] "y"
Reload privilege tables now? [Y/n] "y"

# show that you can not log into mysql terminal without password anymore
mysql -u root

#Connect to the MariaDB Server and open MySQL CLI with root user and password (pw:root1234).
mysql -u root -p

# show that test db is gone.
SHOW databases;

# list the users defined in the server and show that it has now password and its encrypted
USE mysql;
SELECT Host, User, Password FROM user;

# create new database named "clarusway";
CREATE DATABASE clarusway;

# show newly created database
SHOW DATABASES;

# create a user named "clarus_user"; 
CREATE USER clarus_user IDENTIFIED BY 'user1234';

# grant permissions to the user "clarus_user" for database "clarusway"
GRANT ALL ON clarusway.* TO clarus_user IDENTIFIED BY 'user1234' WITH GRANT OPTION;

# update privileges
FLUSH PRIVILEGES;
# close the mysql terminal
EXIT;
--------------------------------------------
# Part 3 - Manipulating MariaDB Database

# login back as "clarus_user" using the password defined
mysql -u clarus_user -p
# show databases for clarus_user
SHOW DATABASES;
# select the database clarusway
USE clarusway;

# create a table named "offices" 
CREATE TABLE `offices` (
  `office_id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  PRIMARY KEY (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# insert some data into the table named "offices"
INSERT INTO `offices` VALUES (1,'03 Reinke Trail','Cincinnati','OH');
INSERT INTO `offices` VALUES (2,'5507 Becker Terrace','New York City','NY');
INSERT INTO `offices` VALUES (3,'54 Northland Court','Richmond','VA');
INSERT INTO `offices` VALUES (4,'08 South Crossing','Cincinnati','OH');
INSERT INTO `offices` VALUES (5,'553 Maple Drive','Minneapolis','MN');
INSERT INTO `offices` VALUES (6,'23 North Plaza','Aurora','CO');
INSERT INTO `offices` VALUES (7,'9658 Wayridge Court','Boise','ID');
INSERT INTO `offices` VALUES (8,'9 Grayhawk Trail','New York City','NY');
INSERT INTO `offices` VALUES (9,'16862 Westend Hill','Knoxville','TN');
INSERT INTO `offices` VALUES (10,'4 Bluestem Parkway','Savannah','GA');

# create a table named "employees"
CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `job_title` varchar(50) NOT NULL,
  `salary` int(11) NOT NULL,
  `reports_to` int(11) DEFAULT NULL,
  `office_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `fk_employees_offices_idx` (`office_id`),
  CONSTRAINT `fk_employees_offices` FOREIGN KEY (`office_id`) REFERENCES `offices` (`office_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# insert some data into the table named "employees"
INSERT INTO `employees` VALUES (37270,'Yovonnda','Magrannell','Executive Secretary',63996,NULL,10);
INSERT INTO `employees` VALUES (33391,'Darcy','Nortunen','Account Executive',62871,37270,1);
INSERT INTO `employees` VALUES (37851,'Sayer','Matterson','Statistician III',98926,37270,1);
INSERT INTO `employees` VALUES (40448,'Mindy','Crissil','Staff Scientist',94860,37270,1);
INSERT INTO `employees` VALUES (56274,'Keriann','Alloisi','VP Marketing',110150,37270,1);
INSERT INTO `employees` VALUES (63196,'Alaster','Scutchin','Assistant Professor',32179,37270,2);
INSERT INTO `employees` VALUES (67009,'North','de Clerc','VP Product Management',114257,37270,2);
INSERT INTO `employees` VALUES (67370,'Elladine','Rising','Social Worker',96767,37270,2);
INSERT INTO `employees` VALUES (68249,'Nisse','Voysey','Financial Advisor',52832,37270,2);
INSERT INTO `employees` VALUES (72540,'Guthrey','Iacopetti','Office Assistant I',117690,37270,3);
INSERT INTO `employees` VALUES (72913,'Kass','Hefferan','Computer Systems Analyst IV',96401,37270,3);
INSERT INTO `employees` VALUES (75900,'Virge','Goodrum','Information Systems Manager',54578,37270,3);
INSERT INTO `employees` VALUES (76196,'Mirilla','Janowski','Cost Accountant',119241,37270,3);
INSERT INTO `employees` VALUES (80529,'Lynde','Aronson','Junior Executive',77182,37270,4);
INSERT INTO `employees` VALUES (80679,'Mildrid','Sokale','Geologist II',67987,37270,4);
INSERT INTO `employees` VALUES (84791,'Hazel','Tarbert','General Manager',93760,37270,4);
INSERT INTO `employees` VALUES (95213,'Cole','Kesterton','Pharmacist',86119,37270,4);
INSERT INTO `employees` VALUES (96513,'Theresa','Binney','Food Chemist',47354,37270,5);
INSERT INTO `employees` VALUES (98374,'Estrellita','Daleman','Staff Accountant IV',70187,37270,5);
INSERT INTO `employees` VALUES (115357,'Ivy','Fearey','Structural Engineer',92710,37270,5);

# show newly created tables;
SHOW tables;
# list all records within employees table
SELECT * FROM offices;
# list all records within offices table
SELECT * FROM employees;

# Filter the first_name, last_name, salary, city, state information of employees having salary more than $100000.
SELECT first_name, last_name, salary, city, state FROM employees INNER JOIN offices ON employees.office_id=offices.office_id WHERE employees.salary > 100000;

# close the mysql terminal
EXIT;
--------------------------------
# Part 4 - Creating a Client Instance and Connecting to MariaDB Server Instance Remotely

# connect the clarusway db on MySQL DB Server from the other hosts

# show that clarus_user can do same db operations from the other host

# Launch EC2 Instance (Ubuntu 20.04) and name it as MariaDB-Client on Ubuntu.

# AMI: Ubuntu 20.04
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere
#   - MYSQL/Aurora  -----> 3306  -----> Anywhere

# Connect to EC2 instance with SSH.

# Update instance.
sudo apt update && sudo apt upgrade -y

# Install the mariadb-client.
sudo apt-get install mariadb-client -y

# Connect the clarusway  db on MariaDB Server on the other EC2 instance (pw:user1234).
mysql -h ec2-54-47-173-9.compute-1.amazonaws.com -u clarususer -p (edited) 


# Show that clarususer can do same db operations on MariaDB Server instance.
SELECT first_name, last_name, salary, city, state FROM employees INNER JOIN offices ON employees.office_id=offices.office_id WHERE employees.salary > 100000;



[ec2-user ~]$ sudo hostnamectl set-hostname MariaDB-Client
HOSTNAME=MariaDB-Client
[ec2-user ~]$ sudo reboot

# Close the mysql terminal.

# DO NOT FORGET TO TERMINATE THE INSTANCES YOU CREATED!!!!!!!!!!