# Чувство что я ненавижу питон
# Как будто пытаюсь говорить на китайском
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}

        for i in range(0, len(s)):
            char = s[i]
            mappedChar = map.get(char, False) # Как сложно тут добывать значения
            mapped = mappedChar if mappedChar else {"count": 0, "index": i} # А эти жуткие кавычки без которых никак
            mapped["count"] = mapped.get("count", 0) + 1
            map[char] = mapped

        filtered = [v for v in map.values() if v["count"] == 1]
        # а над отсутствием нормальных цепочек .map .filter .reduce я буду рыдать всю оставшуюся жизнь

        if (len(filtered) == 0):
            return -1

        return filtered[0]["index"]