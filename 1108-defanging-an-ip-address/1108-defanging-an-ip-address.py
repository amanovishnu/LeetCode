class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = ''
        for ch in address:
            string+= ch if ch != '.' else '[.]'
        return string    