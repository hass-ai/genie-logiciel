import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

types_de_bruits = [
    ('Bruit gaussien', 'Bruit Gaussien (Normal)', 'blue',
     lambda n: generer_bruit_gaussien(n, moyenne=0.0, ecart_type=1.0)),
    ('Bruit Student-t', 'Bruit Student-t (Queues lourdes)', 'orange',
     lambda n: generer_bruit_student(n, degres_liberte=5, echelle=1.0)),
    ('Bruit GARCH', 'Bruit GARCH (Volatilité variable)', 'green',
     lambda n: generer_bruit_garch(n, omega=0.1, alpha=0.15, beta=0.8)),
    ('Bruit AR(1)', 'Bruit AR(1) (Autocorrélé)', 'purple',
     lambda n: generer_bruit_ar(n, phi=0.7, ecart_type=1.0)),
]

def remplir_axes(axes,longueur):
    for i in range (0,4):
        nom, titre, couleur, generer = types_de_bruits[i]
        print(f"  [{i+1}/4] {nom}...")
        axes[i].plot(generer(longueur), alpha=0.7, color=couleur)
        axes[i].set_title(titre)
        axes[i].set_xlabel('Temps')
        axes[i].set_ylabel('Valeur')
        axes[i].grid(True, alpha=0.3)

def visualiser_types_de_bruit(longueur=1000, sauvegarder=True):
    """
    Visualise les différents types de bruit disponibles.
    """
    print("\n" + "="*60)
    print("COMPARAISON DES TYPES DE BRUIT")
    print("="*60)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    remplir_axes(axes,longueur)

    plt.suptitle('Comparaison des différents types de bruit', fontsize=16)
    plt.tight_layout()
    
    if sauvegarder:
        nom_fichier = 'types_de_bruit.png'
        plt.savefig(nom_fichier, dpi=150, bbox_inches='tight')
        print(f"\n✓ Figure sauvegardée : {nom_fichier}")
    
    print("="*60)
    return fig
