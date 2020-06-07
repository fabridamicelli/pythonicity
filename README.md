Eclectic collection of Python resources, solutions, etc. <br/> Happy Pythoning!
----
1. Compute 1.3 billion cosine distances on a laptop in ~35 seconds. <br/>
I needed to compute pairwise cosine distances for a large list of high-dimensional vectors. After a couple of (very bad) possible solutions I found a reasonable one, of course, standing on the shoulders of giants.
It is pretty much a one-liner and you don't need to care about manually splitting/parallelizing things. [This is a quick write-up](https://fabridamicelli.github.io/blog/python/scikit-learn/scientific-computing/2019/11/30/divide-and-conquer.html) for other people to save that time.

2. Interactive visualization of a 2D embedding.<br/>
Take a quick look at your 2D projected your data in 2D see if it makes any (human) sense.
   - [blogpost](https://fabridamicelli.github.io/blog/python/dataviz/dimensionality-reduction/2019/12/12/interactive-embedding.html)
   - [Example in browser](https://nbviewer.jupyter.org/github/fabridamicelli/pythonicity/blob/master/figs/interactiveEmbedding.html)
   - [Code](https://github.com/fabridamicelli/pythonicity/blob/master/code/interactive_embedding.py)

	![Alt Text](https://github.com/fabridamicelli/pythonicity/blob/master/figs/interactiveEmbedding_demo.gif)

3. Python Gotchas <br/>
The awesomeness of Python and its third party libraries comes with behaviours that sometimes make us chase silly bugs for hours. 
This is an ad eternum growing collection of those headaches.
  - [Explicit is better that implicit: a numpy example](https://fabridamicelli.github.io/blog/python/numpy/2020/05/10/numpy-array-in-place.html)
  - [Achtung: Watch out, German csv readers!](https://fabridamicelli.github.io/blog/python/pandas/text/2020/05/20/achtung-german-csv-reader.html)

----
#### Any bugs, questions, comments, suggestions? Ping me on [twitter](https://www.twitter.com/fabridamicelli) or [drop me an e-mail](https://www.uke.de/allgemein/arztprofile-und-wissenschaftlerprofile/wissenschaftlerprofilseite_fabrizio_damicelli.html).
