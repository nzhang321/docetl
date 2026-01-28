This project was run on my local machine with Windows 10 and Python 3.10 and the newest version of pip installed. I created a fork of the docetl repo which I cloned to my local machine. Then I checked out to the repository and ran the project in a virtual environment with the following commands:
```

```


Results
    Reproduce: 
    Break:
    Break 1: 
        score of 46 extracted, only beaten by pipelines 5 and 8.
        the only one of the pipelines that used a code directive was pipeline 13, which processes the document with a pointless truncation of the first 200 and last 50 words if the document is longer than 250 words, which could potentially miss a place name (ie if the moderator of the speech introduces the place that they are speaking from and it is not brought up again).
        A smarter approach to filter much more quickly is to realize that because place names are proper nouns, a simple filter for capitalized words could already greatly reduce the number of tokens needed to be processed with LLM calls  