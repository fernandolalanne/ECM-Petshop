
# Guide d'utilisation du code du site web ECM Petshop

Le fichier suivant a pour but d'expliquer comment le code a été créé afin qu'il soit plus facile à modifier à l'avenir :smile:





## Index :card_index_dividers:
---

- [Bibliothèques nécessaires](#bibliothèques-nécessaires) :blue_book:
- [Comment lancer ou gérer le programme](#comment-lancer-ou-gérer-le-programme) :raised_eyebrow:
- [Dossiers existants](#dossiers-existants) :file_folder:
- [Explication du dossier Templates](#explication-du-dossier-templates) :framed_picture:
- [Explication du dossier Formateur dans Templates](#explication-du-dossier-formateur-dans-templates) :nerd_face:
- [Fichier views.py](#fichier-views.py) :globe_with_meridians:



## Bibliothèques nécessaires :blue_book:
---
Afin de faire fonctionner le programme, 3 bibliothèques ont été installées:
- Django
- Openpyxl
- Datetime

De plus, si vous utilisez VS Code, je vous recommande d'installer les extensions suivantes :wink: :

- Bootstrap 5 Quick Snippets
- Github Copilot
- Palenight Theme
- Markdown Emoji

## Comment lancer ou gérer le programme :raised_eyebrow:
Pour pouvoir exécuter le programme, il est nécessaire de taper dans le terminal de l'ordinateur

    python3 manage.py runserver

Dans mon cas, j'utilise python 3 et je dois donc taper *python 3*.

Par ailleurs, si vous souhaitez modifier un modèle, c'est-à-dire un tableau de la base de données, vous devez écrire les modifications puis écrire

    python3 manage.py makemigrations

Et ensuite

    python3 manage.py migrate

De plus, le programme comporte une logique de *login* et *logout* ainsi que l'enregistrement d'utilisateurs normaux et d'un *superuser*. Ce dernier est celui qui a le pouvoir de modifier l'ensemble du site web à partir de l'onglet d'Admin, qui est un onglet créé par défaut par Django. 

Pour créer un nouveau *superuser*, il suffit d'exécuter la ligne de code suivante et de suivre les instructions dans le terminal:

    python3 manage.py createsuperuser

Actuellement, les superutilisateurs créés avec leurs mots de passe respectifs sont:

    superuser1: admin
    mot de passe: 123123

Ces données peuvent être modifiées à tout moment à partir de l'onglet "Admin", accessible via le bouton de l'onglet accueil ou via l'URL suivante:

    http://127.0.0.1:8000/admin/


## Dossiers existants :file_folder:
---

Dans le dossier PetshopInfo2, vous trouverez tous les fichiers pratiques, à savoir les fichiers HTML, les images utilisées, les fichiers *urls.py* et *views.py* etc.


Plus précisément dans le dossier PetshopInfo2, vous trouverez les fichiers suivants dont la fonction est détaillée ci-dessous :
- *static*: Dossier contenant les fichiers statiques de l'application. Vous y trouverez le dossier *js*, qui contient le code javascript, le dossier *css*, qui contient le design de la page et enfin le dossier *images*, qui contient les images utilisées.
- *models.py*: Contient les modèles créés dans la base de données. Toute modification des tableaux présentes doit être effectuée ici.
- *forms.py*: Sa fonction est de gérer la manière dont les informations contenues dans les tableaux sont affichées.
- *templates*: Vous trouverez ici les codes qui vous permettent d'afficher les vues du site web. Les détails de ce dossier sont expliqués ci-dessous
- *views.py*: Dossier le plus important. Il contient les fonctions qui gèrent la logique de l'application.
- *urls.py* : Permet de connecter chaque fichier HTML avec les fonctions présentes dans views.py

Tous les autres fichiers sont sans importance

## Explication du dossier Templates :framed_picture:
---
Le dossier contient des dossiers dont le nom correspond à celui des onglets du site, à l'exception du dossier *general_tabs*, du dossier *registration* et *baste.html*.

Dans *general_tabs*, vous trouverez des fichiers html qui affichent des messages d'erreur ou de réussite dans le déroulement du programme, par exemple lors du téléchargement d'un fichier, d'un enregistrement réussi, etc.

Dans *registration* se trouvent les fichiers html qui affichent les onglets de connexion et d'enregistrement.

Enfin, *base.html* est un fichier utilisé pour concevoir les pages du site web avec Bootstrap 5.

## Explication du dossier shops dans Templates :nerd_face:
---

Le dossier contient 4 fichiers:
- *cart.html*
- *confirmation_of_purchase.html*
- *statusAnimal.html*
- *index2.html*

Tous ces fichiers sont des vues montrant différentes parties du programme. 

Bien entendu, le fichier *index2.html* est le fichier qui affiche le menu principal de la page. 

*statusAnimal.html* est un fichier qui affiche l'état des animaux dans l'animalerie et est une fonction exclusive aux utilisateurs administrateurs. Cet onglet n'est pas activé pour les utilisateurs normaux. 

Enfin, *cart.html* affiche une page résumant les articles à acheter.


## Fichier views.py :globe_with_meridians:
Il contient toutes les fonctions qui vous permettent d'exécuter différentes actions dans les vues du programme.
