!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
!pip install inltk
!pip install tornado==4.5.3
from inltk.inltk import setup
setup('hi')
from inltk.inltk import tokenize
hindi_text = """ र क त क भ ष खन बह त त लच ह ।"""
# tokenize(input text, language code)
tokenize(hindi_text, "hi")
