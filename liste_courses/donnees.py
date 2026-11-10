class Ingredient:
    def __init__(self,nom, quantite, unite):
        self.nom=nom
        self.quantite = quantite
        self.unite =unite

class Recette:
    def __init__(self, nom,personnes, ingredients):
        self.nom = nom
        self.personnes=personnes
        self.ingredients = ingredients
