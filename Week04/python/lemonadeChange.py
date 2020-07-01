class Solution(object): #aw
    """
    匹配多种情况
    // 算法1：
    // 如果给5元，不用找
    // 如果给10元，找5元，否则找不开
    // 如果给20元，优先找10+5，再找5+5+5，否则找不开
    """
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
































