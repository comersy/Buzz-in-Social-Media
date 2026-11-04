# Buzz in Social Media

Analyse du dataset UCI [Buzz in Social Media](https://archive.ics.uci.edu/dataset/248/buzz+in+social+media), par Côme Rossary et Batiste Fancellu.

Chaque ligne est un sujet (un mot-clé tech) suivi pendant quelques semaines sur l'un de deux réseaux, Twitter ou le forum Tom's Hardware, avec une douzaine d'indicateurs d'activité par pas de temps. La cible est la popularité du sujet sur les semaines suivantes : discussions actives sur Twitter, pages vues sur le forum. Toute l'analyse est dans [notebook.ipynb](notebook.ipynb).

## Ce qu'on a trouvé

**Demain ressemble à aujourd'hui.** Prédire la dernière valeur observée explique déjà 89 % de la variance (en log) sur Twitter et 98 % sur le forum. Ajuster une tendance sur la fenêtre et l'extrapoler, linéairement ou exponentiellement, fait moins bien : les séries sont courtes et bruitées, et l'extrapolation amplifie le bruit.

**Les autres indicateurs aident, surtout sur Twitter.** Un gradient boosting sur toutes les colonnes réduit l'erreur de 29 % sur Twitter et de 19 % sur le forum. Une régression linéaire sur les attributs passés en log obtient presque le même score : la relation est à peu près additive en échelle log, et l'erreur restante vient des données, pas du modèle.

**Le buzz Twitter, c'est une seule chose : le volume.** Discussions, auteurs, contributions et part d'attention sont le même signal, parce qu'une discussion y est le plus souvent un tweet unique. La popularité est volatile : elle bouge typiquement de 40 % d'un pas au suivant.

**Le buzz du forum, c'est deux choses : l'écriture et la lecture.** Fils, messages et auteurs forment un bloc, le plus souvent à zéro. Les pages vues en forment un autre, presque jamais nul et extrêmement persistant (0,99 d'un pas au suivant). La cible est la lecture, et l'écriture en dit peu. La popularité bouge d'environ 18 % par pas.

**Les deux réseaux se reconnaissent à la seule forme de la courbe de popularité d'un sujet**, une fois retirées l'échelle, la densité d'activité et la structure des discussions (AUC 0,82). Ce qui les sépare n'est pas la tendance, qui monte sur les deux par construction du dataset, mais la volatilité.

## Récupérer le dataset

Les fichiers `.data` (≈ 300 Mo au total) ne sont pas versionnés : ils dépassent la limite de 100 Mo par fichier de GitHub.
Pour les télécharger et les placer au bon endroit :

```bash
python download_dataset.py
```

Fichiers obtenus :

- `buzz+in+social+media/regression/regression/Twitter/Twitter.data`
- `buzz+in+social+media/regression/regression/TomsHardware/TomsHardware.data`

Les descriptions des colonnes (`*.names`) sont incluses dans le dépôt.

Le dataset peut aussi être téléchargé à la main depuis la page UCI ci-dessus.
