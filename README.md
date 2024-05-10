# BLUE Evaluation for Transformer DE-EN Translation using Multi30K Dataset
BLUE (BiLingual Evaluation Understudy) evaluation of German to English translation by "Attention is All You Need" Transformer using Multi30K Dataset
The evaluation applied on 100 results for each of Encoder Attention, Decoder Attention, and Encoder-Decoder Attention.
<br> 
<br> 
# Results files
**enco.ref**: encoder reference translation<br> 
**enco.con**: trasndformer encoder translation<br> 
**enco.de**: the input German sentences<br> 
<br> 
**deco.ref**: decoder reference translation<br> 
**deco.con**: trasndformer decoder translation<br> 
**deco.de**: the input German sentences<br> 
<br> 
**enco-deco.ref**: encoder-decoder reference translation<br> 
**enco-deco.con**: trasndformer encoder-decoder translation<br> 
**enco-deco.de**: the input German sentences<br> 
<br> 
<br> 
# Execution
!pip install nltk<br> 
run **blue.py**
