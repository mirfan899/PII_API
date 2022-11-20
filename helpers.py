from copy import deepcopy
from presidio_analyzer import RecognizerRegistry
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.predefined_recognizers import SpacyRecognizer

spacy_recognizer = SpacyRecognizer(supported_language="en")

yaml_file = "my_recognizers/medical_id.yaml"
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizers_from_yaml(yaml_file)
analyzer = AnalyzerEngine(registry=registry)
analyzer.registry.add_recognizer(spacy_recognizer)


def get_pii(text=None):
    results = analyzer.analyze(text=text, language="en")
    output = []
    urls_emails = []

    for r in results:
        # check score first
        if r.score >= 0.5:
            if r.entity_type in ["URL", "EMAIL_ADDRESS", "LINK"]:
                urls_emails.append((r.start, r.end, r.entity_type))
            else:
                output.append((r.start, r.end, r.entity_type))

    # remove overlapping mixed entities i.e. URL, EMAIL_ADDRESS
    doutput = deepcopy(urls_emails)
    for o in doutput:
        for i in doutput:
            if o[0] == i[0] and o[1] < i[1]:
                urls_emails.remove(o)
            elif o[0] > i[0] and o[1] == i[1]:
                urls_emails.remove(o)
    output.extend(urls_emails)

    final_r = []
    for o in output:
        final_r.append({text[o[0]:o[1]]: o[2]})

    return final_r
