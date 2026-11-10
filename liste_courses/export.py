def mettre_en_forme(recette, nb_personnes,ingredients):
    texte="Liste de courses : "+recette.nom + " pour " +str(nb_personnes)+"\n\n"
    for ing in ingredients:
        texte+= "- "+ing.nom+" " + str(round(ing.quantite))+" "+ing.unite + "\n"
    return texte

# renvoie la liste en html : un titre <h1> puis une liste <ul> avec un <li> par ingredient
def mettre_en_forme_html(recette,nb_personnes, ingredients):
    pass

def ecrire_fichier(chemin,texte):
    f=open(chemin, "w")
    f.write(texte)
    f.close()
