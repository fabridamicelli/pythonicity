Eclectic collection of Python resources, solutions, etc. <br/> Happy Pythoning!
----
1. [Compute 1.3 billion cosine distances on a laptop in ~35 seconds](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/notebooks/cosineDistances.ipynb).
I needed to compute pairwise cosine distances for a large list of high-dimensional vectors. After a couple of (very bad) possible solutions I found a reasonable one, of course, standing on the shoulders of giants: [sklearn.metrics.pairwise_distances_chunked](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html).
It is pretty much a one-liner and you don't need to care about manually splitting/parallelizing things. [This is a quick write-up](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/notebooks/cosineDistances.ipynb) for other people to save that time.


----
#### Any bugs, questions, comments, suggestions? Ping me on [twitter](https://www.twitter.com/fabridamicelli) or [drop me an e-mail](https://www.uke.de/allgemein/arztprofile-und-wissenschaftlerprofile/wissenschaftlerprofilseite_fabrizio_damicelli.html).
