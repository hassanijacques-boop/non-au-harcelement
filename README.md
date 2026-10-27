# Non au harcèlement — enquête école

Application de passation de la **grille d’auto-évaluation officielle** sur le harcèlement scolaire
(école élémentaire, CE2-CM2), avec calcul automatique des indices et rapport pour la circonscription.

## Ce que fait l’application

1. **Saisie par l’enseignant (méthode retenue)** : les élèves remplissent la grille papier en classe,
   puis chaque enseignant recopie les résultats de sa classe dans une grille de saisie (24 questions +
   9 oui/non sur un seul écran), au clavier — touches 1 à 4, Entrée pour enregistrer, une minute par
   questionnaire. La classe est choisie une fois pour toute la série.
   **Passation directe sur tablette** également disponible : une question par écran, lecture à voix
   haute, reformulation en français simple, pour un élève isolé ou un petit groupe.
2. **Calcul conforme à la grille** : total A = réponses 3 et 4 aux questions 2 à 8 ; total B =
   réponses 3 et 4 aux questions 11 à 20 ; total C = réponses 2, 3 et 4 aux questions 21 à 24.
   Croisement A × (B+C) dans la table officielle → *harcèlement* / *à surveiller* / *pas de difficulté*.
3. **Espace adulte protégé par code** : vue d’ensemble, résultats par classe, par question, liste des
   élèves à recevoir, interprétation rédigée automatiquement, actions prioritaires.
4. **Rapport imprimable** (A4, PDF) prêt pour le conseil d’école et la circonscription, avec la
   contribution au dossier de labellisation niveau 1.
5. **Exports** : sauvegarde complète `.json` (fusion de plusieurs tablettes), tableau anonyme `.csv`.

Aucune donnée ne quitte l’appareil : tout est stocké dans le navigateur (`localStorage`), aucun serveur.

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | structure + tout le CSS |
| `app.js` | questions officielles, calcul des scores, écrans, rapport |
| `manifest.json`, `sw.js`, `icon-*.png` | installation sur l’écran d’accueil + fonctionnement hors connexion |
| `version.txt` | version publiée (déclenche la mise à jour automatique) |
| `test_nah.py` | 53 contrôles Playwright (parcours complet, table de croisement, exports, mobile) |

## Modifier et publier

```bash
node --check app.js                 # syntaxe
./run_test.sh test_nah.py           # 53 contrôles sur http://127.0.0.1:8823
```

Incrémenter `VERSION` dans `app.js`, `version.txt` et `CACHE` dans `sw.js`, puis pousser sur `main`.

## Source

Grille d’auto-évaluation 2025 (ministère de l’Éducation nationale) et guide de passation
2026-2027. Les questions sont reproduites à l’identique ; la reformulation « en clair » est un
ajout, affiché sous le texte officiel, destiné aux élèves en difficulté de lecture.
