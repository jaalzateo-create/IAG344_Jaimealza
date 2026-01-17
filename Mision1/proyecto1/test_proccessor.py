from proccessor import clean_id
def test_clean_id():
    assert clean_id("cc.75.055.60") == "7505560"
from proccessor import merge_name
def test_merge_name():
    assert merge_name("jaime", "Alberto") == "jaime Alberto"