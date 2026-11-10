from donnees import Ingredient

def adapter_quantites(recette,nb_personnes):
    res=[]
    for ing in recette.ingredients:
        q= ing.quantite *nb_personnes / recette.personnes
        res.append(Ingredient(ing.nom,q, ing.unite))
    return res
