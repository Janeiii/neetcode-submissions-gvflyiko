class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range(len(operations)):
            if operations[i] in ['+', 'D']:
                if operations[i] == '+':
                    prev = score[-1] + score[-2]
                    score.append(prev)
                else:
                    cscore = 2 * score[-1]
                    score.append(cscore)
            elif operations[i] == 'C':
                score.pop()
            else:
                score.append(int(operations[i]))
        return sum(score)