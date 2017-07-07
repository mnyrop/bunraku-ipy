# bunraku-ipy

Jupyter notebooks &etc. for processing data from the __[Barbara Curtis Adachi Bunraku](https://cul.github.io/bunraku-demo/)__ (Japanese Puppet Theater) Collection.

## pipeline(s):
#### online collection data / [bunraku-online.ipynb](https://github.com/mnyrop/bunraku-ipy/blob/master/bunraku-online.ipynb)

|               |             |
|-------------:|:-------------| 
| __Start__     | __Cake PHP site powered by Relational MYSQL database__ | 
| 1             | MySQL dump to CSVs     | 
| 2             | Import CSVs into __[IPython](https://ipython.org/)__ as __[Pandas](http://pandas.pydata.org/)__ Dataframes    | 
| 3             | Merge relational data (from CSV jointables) onto Dataframes by type    | 
| 4             | Export Dataframes as JSON records (and CSVs, for archival purposes only).   | 
| 5             | Drop null key:value pairs from JSON (bash __[JQ](https://stedolan.github.io/jq/)__)   | 
| 6             | Convert (no nulls) JSON to YAML (bash __[Pyyaml](http://pyyaml.org/)__)   | 
| 7             | Generate __[Jekyll collections](https://jekyllrb.com/docs/collections/)__ (and pages) from YAML using __[Yaml-Splitter plugin](https://github.com/mnyrop/yaml-splitter)__ |
| __End__       | __Static Jekyll site powered by YAML data, with JSON index for static search__ | 

#### total collection data / [bunraku-full.ipynb](https://github.com/mnyrop/bunraku-ipy/blob/master/bunraku-full.ipynb)

The data accessible on the original PHP site (as well as the new Jekyll site) represents only about 60% or so of the information stored in the MySQL database. To preserve that information for future use, I used a separate Ipy notebook/pipeline to output CSVs and JSON where images/media marked 'offline' were not dropped.


## stats:
There is also a Jupyter notebook for generating matplotlib graphs and D3-specific/refactored JSON for data visualization. (__[bunraku-stats.ipynb](https://github.com/mnyrop/bunraku-ipy/blob/master/stats/bunraku-stats.ipynb)__)
