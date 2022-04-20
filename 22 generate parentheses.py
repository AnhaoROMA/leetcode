class Solution:
    def all_possible_results(self, string, left, right):
        if left == 0 and right == 0:
            res = []
            res.append(string)
            return res
        elif left == right:
            return self.all_possible_results(string + "(", left - 1, right)
        elif left == 0 and right > 0:
            return self.all_possible_results(string + ")", left, right - 1)
        elif right == 0 and left > 0:
            return self.all_possible_results(string + "(", left - 1, right)
        else:
            return self.all_possible_results(string + "(", left - 1, right) + self.all_possible_results(string + ")",
                                                                                                        left, right - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        # 计数
        num_of_left = n
        num_of_right = n
        # 求解过程
        results = self.all_possible_results(
            string="",
            left=num_of_left,
            right=num_of_right
        )
        return results
