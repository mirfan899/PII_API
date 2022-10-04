import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, Pattern, PatternRecognizer
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine
import spacy


# Create a class inheriting from SpacyNlpEngine
class LoadedSpacyNlpEngine(SpacyNlpEngine):
    def __init__(self, loaded_spacy_model):
        self.nlp = {"en": loaded_spacy_model}


# Load a model a-priori
nlp = spacy.load("en_core_web_md")

# Pass the loaded model to the new LoadedSpacyNlpEngine
loaded_nlp_engine = LoadedSpacyNlpEngine(loaded_spacy_model=nlp)
yaml_file = "my_recognizers/medical_id.yaml"
registry = RecognizerRegistry()
registry.add_recognizers_from_yaml(yaml_file)
analyzer = AnalyzerEngine(registry=registry, nlp_engine=loaded_nlp_engine)
result = analyzer.analyze(text="This is New York and my medical id is 315-77-8771A 002-51-3788B2", language="en")
print(result)
print(r for r in analyzer.get_recognizers())
print(analyzer.get_supported_entities())

# Define the regex pattern
# regex = r"\b\d{3}(-)\d{2}(-)\d{4}(A|B[1-7]?|M|T|C[1-4]|D)\b"
# medical_pattern = Pattern(name="Medical ID pattern", regex=regex, score=0.5)
# medical_recognizer = PatternRecognizer(supported_entity="MEDICAL_ID", patterns=[medical_pattern], context=["id", "medical"])
# analyzer = AnalyzerEngine()
# analyzer.registry.add_recognizer(medical_recognizer)
#
# results = analyzer.analyze(text="This is New York and my medical id is 315-77-8771A 002-51-3788B2", language="en")
# print(f"Result:\n {results}")
