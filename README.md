# Buzz in Social Media

Projet basé sur le dataset UCI [Buzz in Social Media](https://archive.ics.uci.edu/dataset/248/buzz+in+social+media).

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

Téléchargement manuel possible depuis la page UCI ci-dessus.
