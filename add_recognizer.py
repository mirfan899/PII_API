import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, Pattern, PatternRecognizer
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.predefined_recognizers import SpacyRecognizer

spacy_recognizer = SpacyRecognizer(supported_language="en")

yaml_file = "my_recognizers/medical_id.yaml"
registry = RecognizerRegistry()
registry.add_recognizers_from_yaml(yaml_file)
analyzer = AnalyzerEngine(registry=registry)
analyzer.registry.add_recognizer(spacy_recognizer)

result = analyzer.analyze(text="This is New York and my medical id is 315-77-8771A 002-51-3788B2", language="en")
print(result)
print(analyzer.get_supported_entities())
