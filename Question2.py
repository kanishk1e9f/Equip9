import heapq
from collections import defaultdict

def match_equipment_deals(requests, sellers):
    price_map = defaultdict(list)
    
    for eq, price in sellers:
        heapq.heappush(price_map[eq], price)

    result = []
    for eq, max_price in requests:
        while price_map[eq] and price_map[eq][0] > max_price:
            heapq.heappop(price_map[eq])
        
        result.append(price_map[eq][0] if price_map[eq] else None)

    return result

requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

print(match_equipment_deals(requests, sellers))
