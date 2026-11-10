from lecture import lire_recette
from calcul import adapter_quantites
from export import mettre_en_forme,mettre_en_forme_html, ecrire_fichier

nb_personnes=int(input("nombre de personnes : "))
format = input("format (txt ou html) : ")

recette= lire_recette("recette.txt")
ingredients = adapter_quantites(recette,nb_personnes)

if format=="html":
    texte = mettre_en_forme_html(recette, nb_personnes,ingredients)
    ecrire_fichier("liste_courses.html",texte)
else :
    texte=mettre_en_forme(recette,nb_personnes, ingredients)
    ecrire_fichier("liste_courses.txt", texte)

print("ok")
