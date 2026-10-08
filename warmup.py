import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



def visualiser_types_de_bruit(longueur=1000, sauvegarder=True):
    """
    Visualise les différents types de bruit disponibles.
    """
    print("\n" + "="*60)
    print("COMPARAISON DES TYPES DE BRUIT")
    print("="*60)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    # 1. Gaussien
    print("  [1/4] Bruit gaussien...")
    bruit = generer_bruit_gaussien(longueur, moyenne=0.0, ecart_type=1.0)
    axes[0].plot(bruit, alpha=0.7, color='blue')
    axes[0].set_title('Bruit Gaussien (Normal)')
    axes[0].set_xlabel('Temps')
    axes[0].set_ylabel('Valeur')
    axes[0].grid(True, alpha=0.3)
    
    # 2. Student-t
    print("  [2/4] Bruit Student-t...")
    bruit = generer_bruit_student(longueur, degres_liberte=5, echelle=1.0)
    axes[1].plot(bruit, alpha=0.7, color='orange')
    axes[1].set_title('Bruit Student-t (Queues lourdes)')
    axes[1].set_xlabel('Temps')
    axes[1].set_ylabel('Valeur')
    axes[1].grid(True, alpha=0.3)
    
    # 3. GARCH
    print("  [3/4] Bruit GARCH...")
    bruit = generer_bruit_garch(longueur, omega=0.1, alpha=0.15, beta=0.8)
    axes[2].plot(bruit, alpha=0.7, color='green')
    axes[2].set_title('Bruit GARCH (Volatilité variable)')
    axes[2].set_xlabel('Temps')
    axes[2].set_ylabel('Valeur')
    axes[2].grid(True, alpha=0.3)
    
    # 4. AR(1)
    print("  [4/4] Bruit AR(1)...")
    bruit = generer_bruit_ar(longueur, phi=0.7, ecart_type=1.0)
    axes[3].plot(bruit, alpha=0.7, color='purple')
    axes[3].set_title('Bruit AR(1) (Autocorrélé)')
    axes[3].set_xlabel('Temps')
    axes[3].set_ylabel('Valeur')
    axes[3].grid(True, alpha=0.3)
    
    plt.suptitle('Comparaison des différents types de bruit', fontsize=16)
    plt.tight_layout()
    
    if sauvegarder:
        nom_fichier = 'types_de_bruit.png'
        plt.savefig(nom_fichier, dpi=150, bbox_inches='tight')
        print(f"\n✓ Figure sauvegardée : {nom_fichier}")
    
    print("="*60)
    return fig