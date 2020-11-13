# -*- coding: utf-8 -*-
import pymysql
import csv

#se connecter à la base de donnée
connection = pymysql.connect(user='dave', host='localhost', password='dave')
cur = connection.cursor()

#definissons une fonction pour ajouter une table à la base de donnée
def ajout():
	cur = connection.cursor()
	#cur.execute("set global local_infile = 1 ")
	#Se connecter à la base de donnée dave
	cur.execute("use dave")
	#Créer une table 
	cur.execute ("create table personne (id int PRIMARY KEY, nom VARCHAR(10),prenom VARCHAR(15),numero varchar(15),email varchar(30), Localite VARCHAR(15))")
	cur.execute ("create table persup (id int PRIMARY KEY, nom VARCHAR(10),prenom VARCHAR(15),numero varchar(15),email varchar(30))")
	# enregistrer les valeur dans la base de de bonnées 
	connection.commit()

	#importont un fichier csv dans une table 
	#repertorier le ficher à importer dans le repertoire par défaut. trouver le répertoir à partir de cette commande show variables like 'secure_file_priv' 

	cur.execute("load data  infile '/var/lib/mysql-files/Classeur1.csv' into table personne fields terminated by ';' lines terminated by '\r\n' ignore 1 lines ")
	cur.execute("load data  infile '/var/lib/mysql-files/Classeur2.csv' into table persup fields terminated by ';' lines terminated by '\r\n' ignore 1 lines ")
	connection.commit()
	cur.execute("select * from personne")
	rows1 = cur.fetchall()
	print(rows1)

#pour modifier la valeur de la colone d'une table 
def modif():
	cur = connection.cursor()
	cur.execute("use dave")
	#vidons le contenue des differentes colonnes
	cur.execute("update personne set nom = null, prenom = null, numero = null, email = null ")
	connection.commit()
	#remplaçons le contenue des differentes colonnes 
	cur.execute("update personne set nom = (select nom from persup where personne.id = persup.id), prenom = (select prenom from persup where personne.id = persup.id), numero = (select numero from persup where personne.id = persup.id), email = (select email from persup where personne.id = persup.id)")
	cur.execute("select * from personne")
	cur.execute("drop table persup")
	rows2 = cur.fetchall()
	print(rows2)

#ajout()
modif()
