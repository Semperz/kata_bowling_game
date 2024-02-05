class ScoreCard:
    def __init__(self, score_card_pins):
        self.pins = score_card_pins
        self.score = 0
        self.values = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'X': 10,
            '/': 10,
            '-': 0
        }
    def frame_pins(self):
        if self.pins not in ['X', '/', '-']:
            pins_score_list = list(self.pins)
            current_score = [(self.values[num]) for num in pins_score_list]
            self.score += sum(current_score)
        return self.score

    def first_frame(self):
        if self.pins[0] == 'X':
            current_frame = self.pins[0]
            self.score += current_frame
            if self.second_frame == 20:
                self.score += self.second_frame
                return self.score
            return self.score
        else:
            current_frame = list(self.pins[0:1])
            score_list =[]
            current_score = [score_list.append(int(numbers)) for numbers in current_frame]
            self.score += sum(current_score)
            if '/' in current_frame:
                current_frame = self.pins[2]
                self.score += current_frame
                return self.score

    def second_frame(self):
