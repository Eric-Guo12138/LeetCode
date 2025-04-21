class Solution:
    def isValid(self, s: str) -> bool:
        # 利用栈的特性，将s中的左括号依次放入栈中，若检测到右括号，则弹出
        # 栈顶的左括号，看是否匹配
        # 如果s的长度是奇数，肯定无效
        if len(s) % 2 != 0:
            return False
        # 初始化一个栈
        st = []
        # 依次遍历栈中元素
        for i in range(len(s)):
            # 左括号直接放进栈中
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            # 右括号，弹出栈顶元素看是否匹配
            elif s[i] == ')':
                if len(st) != 0 and st.pop() == '(':
                    return True
                else:
                    return False
            elif s[i] == ']':
                if len(st) != 0 and st.pop() == '[':
                    return True
                else:
                    return False
            elif s[i] == '}':
                if len(st) != 0 and st.pop() == '{':
                    return True
                else:
                    return False
        if len(st) != 0:
            return False