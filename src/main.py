from PIL import Image
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer import Pattern, PatternRecognizer
from presidio_image_redactor import ImageRedactorEngine
import matplotlib.pyplot as plt
from pathlib import Path

# -- TEXT ---
# # Set up the engine, loads the NLP module (spaCy model by default) and other PII recognizers
# analyzer = AnalyzerEngine()

# # Call analyzer to get results
# results = analyzer.analyze(text="My phone number is 212-555-5555",
#                            entities=["PHONE_NUMBER"],
#                            language='en')
# print(results)



# --- Standard images ----
engine = ImageRedactorEngine()

image = Image.open(Path("sample_data/test_image.png"))

redacted_image = engine.redact(image, (155, 11, 103))
redacted_image.show()