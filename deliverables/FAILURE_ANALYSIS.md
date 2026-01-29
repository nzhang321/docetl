Results
    Reproduce: 
        To reproduce MOAR, I decided to create a relatively straightforward task of 
    Break:
        6, 7, 11 and 12 were on the Pareto frontier, and 11 and 12 used a code directive. 11 was a truncation of the first 200 and last 100 words
    Break 1: 
        Score of 46 place names extracted, only beaten by pipelines 5 and 8.
        the only one of the pipelines that used a code directive was pipeline 13, which processes the document with a pointless truncation of the first 200 and last 50 words if the document is longer than 250 words, which could potentially miss a place name (ie if the moderator of the speech introduces the place that they are speaking from and it is not brought up again).
        A smarter approach to filter much more quickly is to realize that because place names are proper nouns, a simple filter for capitalized words could already greatly reduce the number of tokens needed to be processed with LLM calls  

RENAME THE PIPELINE_REPRODUCE TO PIPELINE_REPRODUCE1, BREAK TO REPRODUCE2 AND BREAK1 TO BREAK