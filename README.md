# Buzz in Social Media

Analysis of the UCI [Buzz in Social Media](https://archive.ics.uci.edu/dataset/248/buzz+in+social+media) dataset, by Côme Rossary and Batiste Fancellu.

Each row is a topic (a tech keyword) followed over a few weeks on one of two networks, Twitter or the Tom's Hardware forum, with a dozen activity indicators per time step. The target is the topic's popularity over the following weeks: active discussions on Twitter, page views on the forum. The whole analysis is in [notebook.ipynb](notebook.ipynb), in French.

## What we found

**Tomorrow looks like today.** Predicting the last observed value already explains 89 % of the variance (in log) on Twitter and 98 % on the forum. Fitting a trend over the window and extrapolating it, linearly or exponentially, does worse: the series are short and noisy, and extrapolation amplifies the noise.

**The other indicators help, mostly on Twitter.** A gradient boosting on all columns cuts the error by 29 % on Twitter and 19 % on the forum. A linear regression on log-transformed attributes gets almost the same score, so the relationship is roughly additive in log scale and the remaining error sits in the data, not in the model.

**Twitter buzz is one thing: volume.** Discussions, authors, contributions and attention share are all the same signal, because a discussion there is usually a single tweet. Popularity is volatile: it typically moves by about 40 % from one step to the next.

**Forum buzz is two things: writing and reading.** Threads, posts and authors form one block, mostly zero. Page views are another, almost never zero and extremely persistent (0.99 from one step to the next). The target is reading, and writing tells you little about it. Popularity moves by about 18 % a step.

**The two networks can be told apart from the shape of a topic's popularity curve alone**, once scale, activity density and discussion structure are removed (AUC 0.82). What separates them is not the trend, which rises on both by construction of the dataset, but the volatility.

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
