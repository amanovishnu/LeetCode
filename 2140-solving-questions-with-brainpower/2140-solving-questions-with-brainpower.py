class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
      
        max_points = [0] * (n + 1)
     
        for i in range(n - 1, -1, -1):
            points, jump = questions[i]
           
            next_question = min(jump + i + 1, n)
            points_from_this_question = points + max_points[next_question]
            max_points[i] = max(points_from_this_question, max_points[i + 1])
        
        return max_points[0]