"""Télécharge le dataset UCI "Buzz in Social Media" et place les fichiers .data
aux emplacements attendus par le projet.

Source : https://archive.ics.uci.edu/dataset/248/buzz+in+social+media

Usage : python download_dataset.py
"""

import shutil
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/248/buzz+in+social+media.zip"
ROOT = Path(__file__).resolve().parent
TARGETS = {
    "Twitter.data": ROOT / "buzz+in+social+media/regression/regression/Twitter/Twitter.data",
    "TomsHardware.data": ROOT / "buzz+in+social+media/regression/regression/TomsHardware/TomsHardware.data",
}


def extract_all(directory: Path) -> None:
    """Extrait récursivement les archives (zip / tar*) contenues dans directory."""
    done = set()
    while True:
        archives = [
            p for p in directory.rglob("*")
            if p.is_file() and p not in done
            and (zipfile.is_zipfile(p) or tarfile.is_tarfile(p))
        ]
        if not archives:
            return
        for archive in archives:
            done.add(archive)
            dest = archive.with_name(archive.name + "_extracted")
            if zipfile.is_zipfile(archive):
                with zipfile.ZipFile(archive) as z:
                    z.extractall(dest)
            else:
                with tarfile.open(archive) as t:
                    t.extractall(dest, filter="data")


def main() -> None:
    missing = {name: path for name, path in TARGETS.items() if not path.exists()}
    if not missing:
        print("Dataset déjà présent.")
        return

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        archive = tmp / "buzz.zip"
        print(f"Téléchargement de {URL} ...")
        urllib.request.urlretrieve(URL, archive)
        extract_all(tmp)

        for name, path in missing.items():
            found = next(tmp.rglob(name), None)
            if found is None:
                raise SystemExit(f"{name} introuvable dans l'archive téléchargée.")
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(found), path)
            print(f"-> {path.relative_to(ROOT)}")

    print("Dataset prêt.")


if __name__ == "__main__":
    main()
