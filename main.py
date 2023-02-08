import importlib
import sys
import os
try:
    import json
except ImportError:
    import subprocess
    subprocess.call([sys.executable, "-m", "pip", "install", "json"])
    importlib.reload(json)
    
#-----------------SYSTEME DE GESTION DE SUPERMARKET--------------------
# Author: @Anna-el
# Licence: MIT
# Language: Python
# email: aerabenadrasana@gmail.com

articles = []
filname = "articles.json"

if os.path.exists(filname):
    with open(filname, "r") as file:
        articles = json.load(file)
print("------------------Bienvenue dans Anna-el Market------------------")
while True:
    pause = input("Appuyez sur entrer pour continuer.")
    print("1. voir les articles\n2. ajouter un article\n3. acheter un article\n4. chercher un article\n5. modifier un article\n6. effacer un articles\n7. quittez")
    choix = input("Que voulez-vous faire? : ")
    
    if choix == "1":
        print("------------------Voici la liste des articles------------------")
        print("Le nombre d'articles dans l'inventaire est de : ", len(articles))
        while len(articles) != 0:
            print("Voici tous les articles disponibles en supermarcher.")
            for article in articles:
                for key, value in article.items():
                    print(key, ":", value)
            break
    elif choix == "2":
        print("------------------Ajouter un article------------------")
        print("Veuillez entrer les informations de l'article.")
        # while True:
        #     try:
        #         nbr_article = int(input("Entrer le nombre d'article que vous voulez ajouter : "))
        #         break
        #     except ValueError:
        #         print("Veuillez entrer un nombre.")
        # for i in range(nbr_article):
        article = {}
        article["nom"] = input("Entrer le nom de l'article : ")
        while True:
            try:
                article["quantite"] = int(input("Entrer la quantite de l'article : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre.")
        while True:
            try:
                article["prix"] = int(input("Entrer le prix de l'article (Ar): "))
                break
            except ValueError:
                print("Veuillez entrer un nombre.")
        print("L'article a ete ajoute avec succes.")
        articles.append(article)
    elif choix == "3":
        print("------------------Acheter un article------------------")
        print(articles)
        achat_article = input("Entrer le nom de l'article que vous voulez acheter : ")
        for articles in articles:
            if achat_article.lower() == articles["nom"].lower():
                if articles["quantite"] != 0:
                    print("payer", articles["prix"], "Ar","a la caisse.")
                    articles["quantite"] -= 1
                else:
                    print("L'article est epuise.")
    elif choix == "4":
        print("------------------Chercher un article------------------")
        cherche_article = input("Entrer le nom de l'article que vous voulez chercher : ")
        for article in articles:
            if article["nom"].lower() == cherche_article.lower():
                print("L'element que vous cherchez " + cherche_article + "est affiche dessous avec ses details.")
                print(article)
            else:
                print("L'article n'existe pas.")
    elif choix == "5":
        print("------------------Modifier un article------------------")
        article_modifie = input("Entrer le nom de l'article que vous voulez modifier : ")
        for article in articles:
            if article["nom"].lower() == article_modifie.lower():
                print("L'article que vous voulez modifier est affiche dessous.")
                print(article)
                article["nom"] = input("Entrer le nouveau nom de l'article : ")
                while True:
                    try:
                        article["quantite"] = int(input("Entrer la nouvelle quantite de l'article : "))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre.")
                while True:
                    try:
                        article["prix"] = int(input("Entrer le nouveau prix de l'article : "))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre.")
                print("L'article a ete modifie avec succes.")
            else:
                print("L'article n'existe pas.")
    elif choix == "6":
        print("------------------Effacer un article------------------")
        article_efface = input("Entrer le nom de l'article que vous voulez effacer : ")
        for article in articles:
            if article["nom"].lower() == article_efface.lower():
                print("L'article que vous voulez effacer est affiche dessous.")
                print(article)
                confirmation = input("Voulez-vous vraiment effacer cet article? (o/n) -> oui = o, nom = n : ")
                if confirmation.lower() == "o":
                    try :
                        articles.remove(article)
                        print("L'article a ete efface avec succes.")
                    except IndexError:
                        print("Le dictionnaire d'articles est vide.")
                else:
                    print("L'article n'a pas ete efface.")
    elif choix == "7":
        print("------------------Merci d'avoir utilise notre service------------------")
        break
    else:
        print("veuillez entrer un choix valide.")
    with open(filname, "w") as file:
        json.dump(articles, file, indent=4)