def solution(coin, cards):
    def check() -> bool:
        for i in card_set:
            if n + 1 - i in card_set:
                card_set.remove(i)
                card_set.remove(n + 1 - i)
                return True
        return False

    def one_coin() -> bool:
        for i in candidates:
            if n + 1 - i in card_set:
                candidates.remove(i)
                card_set.remove(n + 1 - i)
                return True
        return False

    def two_coin() -> bool:
        for i in candidates:
            if n + 1 - i in candidates:
                candidates.remove(i)
                candidates.remove(n + 1 - i)
                return True
        return False

    result = 1

    n = len(cards)
    idx = n // 3
    card_set = set(cards[:idx])
    candidates = set()
    while idx < n:
        candidates |= {cards[idx], cards[idx + 1]}
        if check():
            result += 1
        elif coin >= 1 and one_coin():
            coin -= 1
            result += 1
        elif coin >= 2 and two_coin():
            coin -= 2
            result += 1
        else:
            break
        idx += 2
    return result
