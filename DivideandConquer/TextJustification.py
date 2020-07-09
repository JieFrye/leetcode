# Text Justification
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each line
# has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the
# number of spaces on a line do not divide evenly between words, the empty slots
# on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.

class Solution:
    def fullJustify(self, words, maxWidth: int):
        '''
        ideas:
        Greedy algorithm: make local optimal choice with the hope to find global optimum
        Check 1: global optimum can be arrived at by selecting a local optimum
        Check 2: a optimal solution to the problem contains optimal solution to the subproblems

        Evenly distribute the extra spaces and as left as possible:
        w1' ' + gap1 + w2' ' + gap2 + w3
        spaces in each gap: (maxWidth - total_char) // gaps
        rest spaces to the left: (maxWidth - total_char) % gaps = r, add 1 to the first r gaps
        '''
        result = []
        n = len(words)

        # record the index in words
        i = 0
        while i < n:
            # total char in a line including a space between words
            total = len(words[i])
            # the last word index in the same line
            last = i + 1
            while last < n:
                # pack words in a greedy approach
                if total + 1 + len(words[last]) > maxWidth:
                    break
                total += 1 + len(words[last])
                last += 1 # exclusive
            # the number of gaps between i and last
            gaps = last - i - 1
            s = ''
            # final line or no gap
            if last == n or gaps == 0:
                for j in range(i, last):
                    s += words[j] + ' '
                s = s[:-1]
                while len(s) < maxWidth:
                    s += ' '
            # for lines before final, evenly distribute spaces
            else:
                spaces = (maxWidth - total) // gaps
                rest = (maxWidth - total) % gaps
                for j in range(i, last-1): # no gap or space for the last word in line
                    s += words[j] + ' ' + ' '*spaces + ' '*(j - i < rest)
                s += words[last - 1]
            result.append(s)
            i = last
        return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol = Solution()
print(sol.fullJustify(words, maxWidth))
