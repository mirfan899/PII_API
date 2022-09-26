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
loaded_nlp_engine = LoadedSpacyNlpEngine(loaded_spacy_model = nlp)
yaml_file = "my_recognizers/medical_id.yaml"
registry = RecognizerRegistry()
registry.add_recognizers_from_yaml(yaml_file)
analyzer = AnalyzerEngine(registry=registry)
result = analyzer.analyze(text="this is a medical id 315-77-8771, A 002-51-3788B2", language="en")
print(result)


# Define the regex pattern
regex = r"\b\d{3}(-)\d{2}(-)\d{4}(A|B[1-7]?|M|T|C[1-4]|D)\b"
medical_pattern = Pattern(name="Medical ID pattern", regex=regex, score=0.5)
medical_recognizer = PatternRecognizer(supported_entity="MEDICAL_ID", patterns=[medical_pattern], context=["id", "medical"])
registry = RecognizerRegistry()
registry.add_recognizer(medical_recognizer)
analyzer = AnalyzerEngine(nlp_engine=loaded_nlp_engine)

results = analyzer.analyze(text="This is Micheal and my medical id is 315-77-8771A 002-51-3788B2", language="en")
print(f"Result:\n {results}")

# def add_medical_id_recognizer():
