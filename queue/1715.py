import sys
import heapq

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]

heapq.heapify(cards)
result = 0
while len(cards) != 1:
    card_1, card_2 = heapq.heappop(cards), heapq.heappop(cards)
    result += card_1 + card_2
    heapq.heappush(cards, card_1 + card_2)
print(result)
