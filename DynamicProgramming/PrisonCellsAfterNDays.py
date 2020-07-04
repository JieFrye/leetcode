# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the rules:
#
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
#
# (Note that because the prison is a row, the first and the last cells in the
# row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way:
# cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison
# after N days (and N such changes described above.)
#
# cells.length == 8


class Solution:
    def prisonAfterNDays(self, cells, N: int):
        '''
        ideas: cells[0] = cells[-1] = 0 from day 1 by definition.
        cells[1:6] have 2^6 = 64 total possiblities but only some are valid.
                                       [0,*,0,x,0,1,0,0] prev
        for example, a state cannot be [0,1,0,0,0,1,0,0]
        for large N, there will be a cycle. Use a set to detect the len(cycle)
        '''
        d = 0
        seen = set()
        cycle = False
        result = cells.copy()
        while d < N:
            result = [0] + [cells[i-1]^cells[i+1]^1 for i in range(1, 7)] + [0]
            if str(result) in seen:
                cycle = True
                break
            seen.add(str(result))
            d += 1
            cells = result.copy()
        if cycle:
            # print(cycle, d)
            return self.prisonAfterNDays(cells, N%d)
        return result


# cells = [0,1,0,1,1,0,0,1]
# cells = [0,0,0,0,0,0,0,0]
# N = 16
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
sol = Solution()
print(sol.prisonAfterNDays(cells, N))
