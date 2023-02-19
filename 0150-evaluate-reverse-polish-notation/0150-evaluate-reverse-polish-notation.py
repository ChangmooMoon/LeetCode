class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for el in tokens:
            if el.isnumeric() or el.lstrip('-').isnumeric():
                st.append(int(el))
            else:
                num2, num1 = st.pop(), st.pop()
                if el == '+':
                    st.append(num1 + num2)
                elif el == '-':
                    st.append(num1 - num2)
                elif el == '*':
                    st.append(num1 * num2)
                else:
                    st.append(int(num1 / num2))
        return st[-1]
'''
1. string token이 주어짐. 후위표기식

2. 10 6 -132 / 
'''
