# Example prompt:
"""
I have some texts along with their corresponding F1 scores. The texts are arranged in ascending order
based on their F1 scores, where higher scores indicate better quality.
text:
Let’s solve the problem.
F1 score:
31
text:
Let’s extract triples containing (subject, relation, object) from the input!
F1 score:
39.7
(. . . more instructions and scores . . . )
In an Information Extraction task, given a sentence s, you generate triples of the form (subject; relation; object),
where subject, relation and object are the constituents of a triple. The following exemplars show how
to apply your text: You replace <INS> in each input with your text, then read the input and give output
which is every triples from the sentence s. We say your output is bad if the triple extract from your output is
different from the given output, and we say your output is correct if they are the same.
input:
S: Applications use this service to record activity for a system while other OSIDs use the service to
record data during development, debugging, or analysis.
A: <INS>
output:
(Applications; use; this service to record activity for a system)
(other OSIDs; use; service to record data during development)
(other OSIDs; use; the service)
(the service; record;  data during debugging)
(the service; record;  data during analysis)
(. . . more exemplars . . . )
Write your new text that is different from the old ones and has a score as high as possible. Write the
text in square brackets.
"""

meta_prompt = """
I have some texts along with their corresponding F1 scores. The texts are arranged in ascending order
based on their F1 scores, where higher scores indicate better quality.
{texts_and_scores}
In an Information Extraction task, given a sentence "S", you generate triples of the form (subject; relation; object),
where subject, relation and object are the constituents of a triple. The following exemplars show how
to apply your text: You replace <INS> in each input with your text, then read the input and give output
which is every triples from the sentence "S". We say your output is bad if the triple extract from your 
output is different from the given output, and we say your output is correct if they are the same.
{exemplars}
Write your new text that is different from the old ones and has a score as high as possible. Write the
text in square brackets.
"""

scorer_prompt = """
S: {question}
{instruction}
Answer with each triple in the form (subject; relation; object) and nothing else.
A:"""