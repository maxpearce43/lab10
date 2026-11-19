# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline:
    #   Push numbers on a stack. On an operator, pop b then a, push a<op>b.
    #   Division truncates toward zero. Answer is the last item on the stack.
    #   ["2","1","+","3","*"]: [2] -> [2,1] -> [3] -> [3,3] -> [9]
    stack = []
    for t in tokens:
        if t in "+-*/" and len(t) == 1:
            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]


def decode_string(s):
    # Outline:
    #   Stack of (text_so_far, repeat_count). On "[" save current text and count, reset.
    #   On "]" pop and set text = saved_text + text * count. Digits build the count
    #   (can be multi-digit); letters append to the current text.
    #   "3[a2[c]]": inner c*2 = "cc", then "a"+"cc" = "acc", *3 = "accaccacc"
    stack = []
    text, num = "", 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((text, num))
            text, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            text = prev + text * k
        else:
            text += ch
    return text


def daily_temperatures(temps):
    # Outline:
    #   Monotonic stack of indices with falling temps. When today is warmer than the
    #   index on top, that day's answer is today - index. Leftovers stay 0.
    #   [73,74,75,71,...]: day0 waits 1 (74), day1 waits 1 (75), day2 waits until 76...
    res = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   Scan cells; on an unseen "1", count an island and flood-fill its neighbours
    #   (up/down/left/right) with an explicit stack so they are not counted again.
    #   ["11000","11000","00100","00011"] -> 3
    seen = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                stack = [(r, c)]
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if (0 <= ny < len(grid) and 0 <= nx < len(grid[0])
                                and grid[ny][nx] == "1" and (ny, nx) not in seen):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
    return count


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
