# import drqa.tokenizers
# drqa.tokenizers.set_default(
#     'corenlp_classpath', '/Users/sxs2561/Documents/AcademicAssignments/CSE597_NLP/Project/NLP2020_Project/DrQA/data/corenlp/*')

from drqa.tokenizers import CoreNLPTokenizer
tok = CoreNLPTokenizer()
tok.tokenize('hello world').words()
