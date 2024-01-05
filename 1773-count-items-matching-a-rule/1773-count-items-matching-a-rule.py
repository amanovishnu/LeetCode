class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_set: dict = { 'type': 0, 'color': 1, 'name': 2 }
        output: int = 0
        for item in items:
            if item[key_set[ruleKey]] == ruleValue:
                output +=1
        return output