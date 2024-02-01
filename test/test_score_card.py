import pytest
from src.score_card import ScoreCard
@pytest.mark.hitting_pins_regular
def test_hitting_pins_regular():
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card == total
