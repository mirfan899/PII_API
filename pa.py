from copy import deepcopy

from presidio_analyzer import AnalyzerEngine
import validators
# Set up the engine, loads the NLP module (spaCy model by default) and other PII recognizers
analyzer = AnalyzerEngine()

text = """
John, please get that article on www.linkedin.com to me by 5:00PM 
on Jan 9th 2012. 4:00 would be ideal, actually. If you have any 
questions, You can reach me at (519)-236-2723x341 or get in touch with
my associate at harold.smith@gmail.com
"""

# Call analyzer to get results
results = analyzer.analyze(text=text, language='en')
# print(results)
output = []
urls_emails = []
for r in results:
    print(r.start, r.end, text[r.start: r.end], r.entity_type)
    if r.entity_type in ["URL", "EMAIL_ADDRESS", "LINK"]:
        urls_emails.append((r.start, r.end, r.entity_type))
    else:
        output.append((r.start, r.end, r.entity_type))

doutput = deepcopy(urls_emails)
for o in doutput:
    for i in doutput:
        if o[0] == i[0] and o[1] < i[1]:
            urls_emails.remove(o)
        elif o[0] > i[0] and o[1] == i[1]:
            urls_emails.remove(o)

print(output)
print(urls_emails)
output.extend(urls_emails)
print(output)