import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, Pattern, PatternRecognizer
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.predefined_recognizers import SpacyRecognizer

spacy_recognizer = SpacyRecognizer(supported_language="en")

yaml_file = "my_recognizers/medical_id.yaml"
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizers_from_yaml(yaml_file)
analyzer = AnalyzerEngine(registry=registry)
analyzer.registry.add_recognizer(spacy_recognizer)

text = "This is New York and my medical id is 315-77-8771A 002-51-3788B2, 03468871351"
result = analyzer.analyze(text=text, language="en")

for r in result:
    if r.score >= 0.4:
        print(text[r.start:r.end], r.entity_type)
print(analyzer.get_supported_entities())
