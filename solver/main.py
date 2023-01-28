import itertools
import re


class Solver(object):
    def __init__(self):
        self.__strength_card_info = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
                                     'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.__strength_combination_info = {'Straight Flush': 9, 'Four of a kind': 8, 'Full House': 7, 'Flush': 6,
                                            'Straight': 5, 'Three of a kind': 4, 'Two pairs': 3, 'Pair': 2, 'High card': 1}
        self.__combinations = [self.__straight_flush_check, self.__four_of_a_kind_check, self.__full_house_check,
                               self.__flush_check, self.__straight_check, self.__three_of_a_kind_check,
                               self.__pairs_check, self.__high_card_check]

    def process(self, line: str) -> str:
        poker_type, all_cards = line.split(' ', 1)
        if poker_type == 'texas-holdem':
            return self.__texas_holdem_sort(all_cards)
        elif poker_type == 'five-card-draw':
            return self.__five_card_draw_sort(all_cards)
        elif poker_type == 'omaha-holdem':
            return self.__omaha_holdem_sort(all_cards)

    def __texas_holdem_sort(self, all_cards: str) -> str:
        blocks_of_cards = self.__get_all_combinations(all_cards)
        res_blocks = []
        for block in blocks_of_cards:
            for combination in self.__combinations:
                res = combination(block)
                if res:
                    # replace name of the combination with the strength of combination
                    res[0] = self.__strength_combination_info[res[0]]
                    res_blocks.append([res, block[10:]])
                    break
        res_blocks.sort()
        return self.__get_res_sort(res_blocks)

    def __omaha_holdem_sort(self, all_cards: str) -> str:
        blocks_of_cards = self.__get_all_combinations(all_cards)
        possible_variations_for_omaha_rules = []
        from_table = [all_cards[:2], all_cards[2:4], all_cards[4:6], all_cards[6:8], all_cards[8:10]]
        table_cards_variation = list(itertools.combinations(from_table, 3))
        for block in blocks_of_cards:
            from_hand = [block[10:12], block[12:14], block[14:16], block[16:18]]
            hand_cards_variation = list(itertools.combinations(from_hand, 2))
            possible_variations = list(itertools.product(table_cards_variation, hand_cards_variation))
            arr_of_variation = []
            for variation in possible_variations:
                arr_of_variation.append(''.join(list(variation[0] + variation[1])))
            result_of_variations = []
            for variation in arr_of_variation:
                result_of_variations.append(variation)
            possible_variations_for_omaha_rules.append(result_of_variations)
        res_blocks = []
        temp_res = []
        for arr_variations in possible_variations_for_omaha_rules:
            for variation in arr_variations:
                for combination in self.__combinations:
                    res = combination(variation)
                    if res:
                        res[0] = self.__strength_combination_info[res[0]]
                        temp_res.append([res, variation])
                        break
            # choose the best possible combination
            temp_res.sort()
            # add the best combination
            res_blocks.append(temp_res[-1])
            temp_res = []
        cards = re.findall('..', all_cards.replace(' ', ''))
        hands = [cards[i:i + 4] for i in range(5, len(cards), 4)]
        for res_block in res_blocks:
            for hand in hands:
                for pair in hand:
                    if pair in res_block[1]:
                        temp_hand = ''.join(hand)
                        res_block[1] = temp_hand
        res_blocks.sort()
        return self.__get_res_sort(res_blocks)

    def __five_card_draw_sort(self, all_cards: str) -> str:
        blocks_of_cards = all_cards.split(' ')
        res_blocks = []
        for block in blocks_of_cards:
            for combination in self.__combinations:
                res = combination(block)
                if res:
                    res[0] = self.__strength_combination_info[res[0]]
                    res_blocks.append([res, block])
                    break
        res_blocks.sort()
        return self.__get_res_sort(res_blocks)

    def __straight_flush_check(self, block_of_card: str) -> list:
        suits_count = self.__get_suits_count(block_of_card)
        main_suit = ''
        for key in suits_count.keys():
            if suits_count[key] >= 5:
                main_suit = key
                break
        if main_suit:
            cards = []
            for i in range(1, len(block_of_card), 2):
                if block_of_card[i] == main_suit:
                    cards.append(self.__strength_card_info[block_of_card[i - 1]])
            cards.sort()
            straight_flush = False
            temp = 0
            diff = 1
            if cards[0] == 2 and cards[-1] == 14:
                cards.insert(0, 1)
            cards_of_combination = []
            left_side = 0
            cards = list(set(cards))
            for i in range(1, len(cards)):
                if cards[i] - cards[left_side] == diff:
                    temp += 1
                    diff += 1
                else:
                    temp = 0
                    left_side = i
                    diff = 1
                if temp >= 4:
                    straight_flush = True
                    right_side = i
                    cards_of_combination = cards[right_side - 4: right_side + 1]
            if straight_flush:
                cards_of_combination.sort(reverse=True)
                return ['Straight Flush', cards_of_combination]
        return None

    def __four_of_a_kind_check(self, block_of_card: str) -> list:
        values_count = self.__get_values_count(block_of_card)
        cards = []
        for i in range(0, len(block_of_card), 2):
            cards.append(self.__strength_card_info[block_of_card[i]])
        cards.sort(reverse=True)
        for key in values_count.keys():
            if values_count[key] >= 4:
                for i in range(4):
                    cards.remove(self.__strength_card_info[key])
                cards_of_combination = [self.__strength_card_info[key]] * 4
                cards_of_combination.append(cards[0])
                return ['Four of a kind', cards_of_combination]
        return None

    def __full_house_check(self, block_of_card: str) -> list:
        straight = False
        pair = False
        max_straight_val = 0
        max_pair_val = 0
        values_count = self.__get_values_count(block_of_card)
        cards = []
        for i in range(0, len(block_of_card), 2):
            cards.append(self.__strength_card_info[block_of_card[i]])
        cards.sort(reverse=True)
        for key in values_count.keys():
            if values_count[key] >= 3 and max_straight_val < self.__strength_card_info[key]:
                straight = True
                if max_straight_val > max_pair_val:
                    max_pair_val = max_straight_val
                    pair = True
                max_straight_val = self.__strength_card_info[key]
                continue
            if values_count[key] >= 2 and self.__strength_card_info[key] > max_pair_val:
                pair = True
                max_pair_val = self.__strength_card_info[key]
        if straight and pair:
            cards_of_combination = [max_straight_val] * 3
            cards_of_combination.append(max_pair_val)
            cards_of_combination.append(max_pair_val)
            return ['Full House', cards_of_combination]
        return None

    def __flush_check(self, block_of_card: str) -> list:
        suits_count = self.__get_suits_count(block_of_card)
        main_suit = ''
        for key in suits_count.keys():
            if suits_count[key] >= 5:
                main_suit = key
                break
        if main_suit:
            cards_values = []
            for i in range(1, len(block_of_card), 2):
                if block_of_card[i] == main_suit:
                    cards_values.append(self.__strength_card_info[block_of_card[i - 1]])
            cards_values.sort(reverse=True)
            return ['Flush', cards_values[:5]]
        return None

    def __straight_check(self, block_of_card: str) -> list:
        value_combination = block_of_card[::2]
        card_values = []
        for value in value_combination:
            card_values.append(self.__strength_card_info[value])
        card_values.sort()
        temp = 0
        diff = 1
        straight = False
        if card_values[0] == 2 and card_values[-1] == 14:
            card_values.insert(0, 1)
        values_of_combination = []
        left_side = 0
        card_values = list(set(card_values))
        for i in range(1, len(card_values)):
            if card_values[i] - card_values[left_side] == diff:
                temp += 1
                diff += 1
            else:
                temp = 0
                left_side = i
                diff = 1
            if temp >= 4:
                straight = True
                right_side = i
                values_of_combination = card_values[right_side - 4: right_side + 1]
        if straight:
            values_of_combination.sort(reverse=True)
            return ['Straight', values_of_combination]
        return None

    def __three_of_a_kind_check(self, block_of_card: str) -> list:
        values_count = self.__get_values_count(block_of_card)
        cards = []
        for i in range(0, len(block_of_card), 2):
            cards.append(self.__strength_card_info[block_of_card[i]])
        cards.sort(reverse=True)
        max_value = 0
        three_of_a_kind = False
        for key in values_count.keys():
            if values_count[key] == 3 and self.__strength_card_info[key] > max_value:
                max_value = self.__strength_card_info[key]
                three_of_a_kind = True
        cards_of_combination = [max_value] * 3
        if three_of_a_kind:
            for i in range(3):
                cards.remove(max_value)
            for i in range(2):
                cards_of_combination.append(cards[i])
            return ['Three of a kind', cards_of_combination]
        return None

    def __pairs_check(self, block_of_card: str) -> list:
        pairs = 0
        values_count = self.__get_values_count(block_of_card)
        cards_values = []
        cards = []
        for i in range(0, len(block_of_card), 2):
            cards.append(self.__strength_card_info[block_of_card[i]])
        cards.sort(reverse=True)
        for key in values_count.keys():
            if values_count[key] == 2:
                pairs += 1
                cards_values.append(self.__strength_card_info[key])
        cards_values.sort()
        if pairs == 1:
            cards_of_combination = [cards_values[0]] * 2
            for i in range(2):
                cards.remove(cards_values[0])
            for i in range(3):
                cards_of_combination.append(cards[i])
            return ['Pair', cards_of_combination]
        if pairs >= 2:
            cards_of_combination = [cards_values[-1]] * 2
            for i in range(2):
                cards_of_combination.append(cards_values[-2])
            for i in range(2):
                cards.remove(cards_values[-1])
                cards.remove(cards_values[-2])
            cards_of_combination.append(cards[0])
            return ['Two pairs', cards_of_combination]
        return None

    def __high_card_check(self, block_of_card: str) -> list:
        cards_values = []
        for i in range(0, len(block_of_card), 2):
            cards_values.append(self.__strength_card_info[block_of_card[i]])
        cards_values.sort(reverse=True)
        return ['High card', cards_values[:5]]

    def __get_values_count(self, block_of_card: str) -> dict:
        suits_combination = block_of_card[::2]
        return {
            '2': suits_combination.count('2'), '3': suits_combination.count('3'),
            '4': suits_combination.count('4'), '5': suits_combination.count('5'),
            '6': suits_combination.count('6'), '7': suits_combination.count('7'),
            '8': suits_combination.count('8'), '9': suits_combination.count('9'),
            'T': suits_combination.count('T'), 'J': suits_combination.count('J'),
            'Q': suits_combination.count('Q'), 'K': suits_combination.count('K'),
            'A': suits_combination.count('A')
        }

    def __get_suits_count(self, block_of_card) -> dict:
        suits_combination = block_of_card[1::2]
        return {
            's': suits_combination.count('s'), 'c': suits_combination.count('c'),
            'd': suits_combination.count('d'), 'h': suits_combination.count('h')
        }

    def __get_res_sort(self, res_blocks) -> str:
        res_sort = ''
        first = True
        last_block = ''
        last_combination_strength = 0
        for block in res_blocks:
            if first:
                res_sort = (block[1])
                first = False
                last_block = block[0][1]
                last_combination_strength = block[0][0]
            else:
                if block[0][1] == last_block and block[0][0] == last_combination_strength:
                    res_sort = res_sort + '=' + block[1]
                else:
                    res_sort = res_sort + ' ' + block[1]
                last_block = block[0][1]
                last_combination_strength = block[0][0]
        return res_sort

    def __get_all_combinations(self, all_cards: str) -> list:
        blocks_of_cards = all_cards.split(' ')
        card_from_table = blocks_of_cards[0]
        # create combination from table and hands cards
        for i in range(len(blocks_of_cards) - 1):
            blocks_of_cards[i] = card_from_table + blocks_of_cards[i + 1]
        blocks_of_cards.pop()
        return blocks_of_cards
