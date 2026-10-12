# Buzz in Social Media

Project based on the UCI [Buzz in Social Media](https://archive.ics.uci.edu/dataset/248/buzz+in+social+media) dataset.

## Getting the dataset

The `.data` files (≈ 300 MB in total) are not versioned: they exceed GitHub's 100 MB per-file limit.
To download them and put them in the right place:

```bash
python download_dataset.py
```

Resulting files:

- `buzz+in+social+media/regression/regression/Twitter/Twitter.data`
- `buzz+in+social+media/regression/regression/TomsHardware/TomsHardware.data`

The column descriptions (`*.names`) are included in the repository.

You can also download the dataset manually from the UCI page above.
