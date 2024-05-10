# BLUE Evaluation for Transformer DE-EN Translation using Multi30K Dataset
BLUE (BiLingual Evaluation Understudy) evaluation of German to English translation by "Attention is All You Need" Transformer using Multi30K Dataset
The evaluation applied on 100 results for each of Encoder Attention, Decoder Attention, and Encoder-Decoder Attention.


# Results files
enco.ref: encoder reference translation
enco.con: trasndformer encoder translation
enco.de: the input German sentences

deco.ref: decoder reference translation
deco.con: trasndformer decoder translation
deco.de: the input German sentences


enco-deco.ref: encoder-decoder reference translation
enco-deco.con: trasndformer encoder-decoder translation
enco-deco.de: the input German sentences


# Execution
!pip install nltk
blue.py
