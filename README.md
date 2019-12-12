Eclectic collection of Python resources, solutions, etc. <br/> Happy Pythoning!
----
1. [Compute 1.3 billion cosine distances on a laptop in ~35 seconds](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/notebooks/cosineDistances.ipynb).<br/>
I needed to compute pairwise cosine distances for a large list of high-dimensional vectors. After a couple of (very bad) possible solutions I found a reasonable one, of course, standing on the shoulders of giants: [sklearn.metrics.pairwise_distances_chunked](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html).
It is pretty much a one-liner and you don't need to care about manually splitting/parallelizing things. [This is a quick write-up](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/notebooks/cosineDistances.ipynb) for other people to save that time.

2. Interactive visualization of a 2D embedding
Say you have a projection of your data in 2D and you want to give _a quick look_ at it to see if it makes any (human) sense.
Then you might find it useful to plot it and interact with it by looking at the labels.
You can also take a look at the results of your embedding compared to a clustering method.

- [Code](https://github.com/fabridamicelli/pythonicity/blob/master/code/interactive_embedding.py)
- [Notebook](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/notebooks/interactiveEmbedding.ipynb)
- [Example (browser)](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/figs/interactiveEmbedding.html)

Demo:

![Alt Text](https://github.com/fabridamicelli/pythonicity/blob/master/figs/interactiveEmbedding_demo.gif)


----
#### Any bugs, questions, comments, suggestions? Ping me on [twitter](https://www.twitter.com/fabridamicelli) or [drop me an e-mail](https://www.uke.de/allgemein/arztprofile-und-wissenschaftlerprofile/wissenschaftlerprofilseite_fabrizio_damicelli.html).
