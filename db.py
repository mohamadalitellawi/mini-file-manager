import csv
import tempfile
import uuid

FILENAME = "products.csv"

def get_temp_files():
    random_text = str(uuid.uuid4())
    yield random_text
    for i in range (10):
        tf = tempfile.NamedTemporaryFile()
        yield str(tf.name)