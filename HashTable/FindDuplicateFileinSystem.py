# Find Duplicate File in System
#
# Given a list of directory info including directory path, and all the files with
# contents in this directory, you need to find out all the groups of duplicate
# files in the file system in terms of their paths.
#
# A group of duplicate files consists of at least two files that have exactly
# the same content.
#
# A single directory info string in the input list has the following format:
#
# "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
#
# It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content,
# f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm.
# Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the
# root directory.
#
# The output is a list of group of duplicate file paths. For each group,
# it contains all the file paths of the files that have the same content.
# A file path is a string that has the following format:
#
# "directory_path/file_name.txt"
import collections

class Solution:
    def findDuplicate(self, paths):
        '''
        Use dict with content as key and the list of files as value
        '''
        d = collections.defaultdict(list)
        for s in paths:
            data = s.split()
            for p in data[1:]:
                file, _, content = p.partition('(')
                d[content[:-1]].append(data[0] + '/' + file)
        result = [ v for v in d.values() if len(v) > 1]
        return result

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", \
"root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
sol = Solution()
print(sol.findDuplicate(paths))
