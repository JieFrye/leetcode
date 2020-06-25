# Reorder Data in Log Files
#
# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.
# Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier,
# with the identifier used in case of ties.
# The digit-logs should be put in their original order.
# Return the final order of the logs.

class Solution:
    def reorderLogFiles(self, logs):
        '''
        Ideas: divide into the two categories specified
        '''
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                # digit-logs in their original order
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # letter-logs are ordered lexicographically ignoring identifier
        # with the identifier used in case of ties
        letter_logs.sort(key = lambda x: x.split()[0])
        letter_logs.sort(key = lambda x: x.split()[1:])
        return letter_logs + digit_logs


# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig",\
# "let4 art zero", "let3 art z", "let3 art nzero", "let3 art zero a"]
logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
sol = Solution()
print(sol.reorderLogFiles(logs))
