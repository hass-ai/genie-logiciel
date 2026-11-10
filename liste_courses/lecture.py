from donnees import Ingredient,Recette

# ligne du type "pates 200 g"
def lire_ingredient(ligne):
    l=ligne.split()
    if len(l)==3:
        return Ingredient(l[0], float(l[1]),l[2])
    else :
        return Ingredient(l[0],float(l[1]), "")  # pas d'unite (ex: oeufs)

def lire_recette(chemin):
    f = open(chemin,"r")
    lignes=f.read().split("\n")
    f.close()

    nom= lignes[0]
    personnes = int(lignes[1].split()[0])
    ingredients=[]
    for i in range(2,len(lignes)):
        if lignes[i]!="":
            ingredients.append(lire_ingredient(lignes[i]))
    return Recette(nom, personnes,ingredients)
