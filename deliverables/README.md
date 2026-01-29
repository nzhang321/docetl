
### CUHK AI Sys PhD Application Project - *Nicholas Zhang* 
##### January 29 2026

This project was run on my local machine with Windows 10 and Python 3.10 and the newest version of pip installed. I created a fork of the docetl repo which I cloned to my local machine. Then I checked out to the repository and ran the project in a virtual environment with the following commands:

```
cd docetl
python -m venv .venv
.venv\Scripts\activate
pip install docetl
```

While debugging various bugs, I also had to run

```
pip install pyrate_limiter==3.9.0
```

and modified line 321 of docetl/moar/ParetoFrontier.py from

```graph_dir = str(new_node.yaml_file_path).rsplit("/", 1)[0] + "/graph/"```

to

```graph_dir = str(Path(new_node.yaml_file_path).with_suffix('')) + "/graph/"```

Of course, it is also necessary to edit the .env file and include your personal OPENAI_API_KEY, which I filled with 10$ (which was more or less my budget for this project, although I definitely could've done it with less if I were more efficient).

  

All 3 pipelines and the sample dataset used were placed in the root directory, which was also where the commands to run the pipelines were run. The results were output into directories uncreatively named "results/moar_optimization/results" "results/moar_optimization/results1" and "results/moar_optimization/results2". I renamed and reorganized these output files so that they correspond more clearly with their associated pipelines for the sake of the deliverables. These were generated like so:

```
docetl build pipeline_reproduce1.yaml --optimizer moar
```

```
docetl build pipeline_reproduce2.yaml --optimizer moar
```

```
docetl build pipeline_break.yaml --optimizer moar
```

  

For the baseline results (originally just output to the root directory, but organized into the respective deliverable folder) without optimization, I created a duplicate pipeline without the optimizer config and ran the following:

```
docetl run pipeline_reproduce_no_opt.yaml
```

```
docetl run pipeline_break_no_opt.yaml
```

```
docetl run pipeline_break1_no_opt.yaml
```

The dataset used for all three pipelines were the same `data_sample.json` file which just uses the first transcript (to save on inference cost and avoid API rate limits) of the [Presidential Debates Dataset](https://raw.githubusercontent.com/ucbepic/docetl/refs/heads/main/example_data/debates/data.json) given as an example in the [DocETL documentation tutorial](https://ucbepic.github.io/docetl/playground/tutorial/).

While I did also set up the docker container following the instructions to interact with the playground, I found that using the instance hosted on docetl.org/playground was faster, and only used it to familiarize myself with the application and its functionality anyways. It was otherwise not used for the deliverables of the project.