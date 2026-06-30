"""
USACO 2018 US Open Contest, Bronze - Problem 3. Family Tree
============================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=833

Tags: Graph, Tree, Ad Hoc

Difficulty: very_hard

Problem Description:
-------------------
Given N mother-child relationships (1 ≤ N ≤ 100), determine the familial
relationship between two specified cows. Cow names are strings of up to
10 uppercase letters.

Output the relationship, which is one of:
- "SIBLINGS": the two cows share the same mother.
- "X is the (relation) of Y": X is a direct ancestor (mother, grand-mother,
  great-grand-mother, ...) or aunt (aunt, great-aunt, ...) of Y.
  An aunt is a child of an ancestor of Y who is not herself an ancestor
  or sister of Y.
- "COUSINS": the two cows share a common ancestor but none of the above apply.
- "NOT RELATED": no common ancestor and neither is an ancestor of the other.

Note: Unlike in Chinese kinship terminology, "COUSINS" in this problem
includes ANY relationship where two cows share a common ancestor but are
not siblings, direct ancestor/descendant, or aunt/niece. This includes
cross-generation relationships (e.g., what Chinese would call "cousin once
removed" or "表姑/表侄").

Sample Input:              Sample Output:
7 AA BB                    BB is the great-aunt of AA
MOTHER AA
GGMOTHER BB
MOTHER SISTER
GMOTHER MOTHER
GMOTHER AUNT
AUNT COUSIN
GGMOTHER GMOTHER

Explanation:
AA's ancestors: MOTHER → GMOTHER → GGMOTHER
BB is a child of GGMOTHER (AA's great-grand-mother), making BB AA's
great-aunt.

====================================================================
Solution 1: DFS Tree Builder + Explicit Relationship Checking
====================================================================
Build the family tree as a graph using DFS to compute each cow's:
- generation depth (1 = root)
- mother
- children list
- root (oldest ancestor in this tree)

Then classify the relationship:
1. Different roots → "NOT RELATED"
2. Same mother → "SIBLINGS"
3. Otherwise, determine which cow is older (higher generation).
   - `is_mother()`: check if `old` is a direct ancestor of `young` at the
     computed distance. If yes → "mother/grand-mother/..."
   - `is_aunt()`: check if `old` shares the same mother as `young`'s
     ancestor at the computed distance. If yes → "aunt/great-aunt/..."
   - If neither → "COUSINS"

This approach explicitly checks each relationship type (mother vs. aunt)
using case analysis, which is intuitive but requires careful handling of
each kinship pattern.

Time Complexity: O(N) to build tree + O(depth) to check relationships
"""

import sys

sys.stdin = open('family.in', 'r')
sys.stdout = open('family.out', 'w')

n, a, b = input().split()
n = int(n)

# d[name] = [depth, mother, [children], root]
d = {}

# Build the family tree from mother-child edges
for i in range(n):
    m, c = input().split()
    if c not in d and m not in d:
        node_c = [0, m, []]          # child node: depth=0, mother=m, no children yet
        node_m = [0, '', [c]]        # mother node: depth=0, root, child=c
        d[c] = node_c
        d[m] = node_m
    elif c not in d and m in d:
        node_c = [0, m, []]
        d[m][2].append(c)            # add child to existing mother
        d[c] = node_c
    elif c in d and m not in d:
        node_m = [0, '', [c]]
        d[c][1] = m                  # set mother for existing child
        d[m] = node_m
    else:
        d[c][1] = m                  # both exist: connect them
        d[m][2].append(c)


def dfs(node, g, r):
    """DFS to assign generation depth and root to all nodes in a tree."""
    node[0] = g        # set generation (depth)
    node.append(r)     # set root

    if not node[2]:    # no children → leaf
        return

    for children in node[2]:
        dfs(d[children], g + 1, r)


# Find all root nodes (cows with no mother) and run DFS from each
roots = []
for k, v in d.items():
    if v[1] == '':
        roots.append(k)
        dfs(v, 1, k)


def is_mother(x, y, diff):
    """
    Check if x is a direct ancestor of y at exactly `diff` generations.
    Walks up from y's mother `diff - 1` times and compares to x.
    """
    mom = d[y][1]
    for _ in range(diff - 1):
        mom = d[mom][1]

    return True if mom == x else False


def is_aunt(x, y, diff):
    """
    Check if x is an aunt of y.
    An aunt means x shares the same mother as one of y's ancestors.
    Walk up from y's mother `diff` times to reach that ancestor,
    then check if that ancestor's mother equals x's mother.
    """
    mom = d[y][1]
    for _ in range(diff):
        mom = d[mom][1]

    return True if mom == d[x][1] else False


def my_print():
    """
    Determine and print the specific relationship between the two cows.
    Assumes they share a common root, same generation, and different mothers.
    """
    # Determine which cow is older (higher in the tree = smaller depth)
    if d[a][0] < d[b][0]:
        old = a
        young = b
    else:
        old = b
        young = a

    diff = d[young][0] - d[old][0]
    if is_mother(old, young, d[young][0] - d[old][0]):
        # old is a direct ancestor of young → mother/grand-mother/...
        title = 'mother'
        if diff == 1:
            pre = ''
        elif diff == 2:
            pre = 'grand-'
        else:
            pre = 'great-' * (diff - 2) + 'grand-'

        print(f'{old} is the {pre+title} of {young}')
    elif is_aunt(old, young, d[young][0] - d[old][0]):
        # old is a child of young's ancestor → aunt/great-aunt/...
        title = 'aunt'
        if diff == 1:
            pre = ''
        else:
            pre = 'great-' * (diff - 1)
        print(f'{old} is the {pre+title} of {young}')
    else:
        # Share common ancestor but not mother/aunt → COUSINS
        print('COUSINS')


# Main classification logic
if d[a][3] != d[b][3]:
    # Different roots → no common ancestor at all
    print('NOT RELATED')
else:
    # Same root → they share a common ancestor
    if d[a][1] == d[b][1]:
        # Same mother → SIBLINGS
        print('SIBLINGS')
    else:
        my_print()


# =====================================================================
# Solution 2: Official USACO Solution (by Dhruv Rohatgi) — Python Translation
# =====================================================================
# Approach: Find the closest common ancestor (CCA) of the two cows, then
# use the distances a (CCA → Elsie) and b (CCA → Bessie) to classify.
#
# Algorithm:
# 1. `find_mother(cow)`: scan all N edges to find a cow's mother.
# 2. `is_ancestor(cow1, cow2)`: walk up from cow2's mother repeatedly;
#    return the number of generations if cow1 is an ancestor, else -1.
# 3. Starting from Bessie, walk up the tree. For each ancestor, check if
#    it is an ancestor of Elsie — the first one that is = the CCA.
#    Let b = distance from CCA to Bessie, a = distance from CCA to Elsie.
# 4. Casework on (a, b):
#    - a=1, b=1 → SIBLINGS
#    - a>1, b>1 → COUSINS
#    - Otherwise: ensure b > a (swap if needed), then:
#      a=0 → mother/grand-mother/...   a=1 → aunt/great-aunt/...
#
# Time Complexity: O(N³) — N ancestor checks × N² per is_ancestor call.
# For N=100 this is fine (~1M operations).
#
# Key differences from Solution 1:
# - Official: distance-based casework on (a, b) after finding a single CCA.
#   Simple but O(N³).
# - User's: explicit mother/aunt/cousins checks with DFS-built tree.
#   O(N) tree build, but requires careful `is_mother`/`is_aunt` logic.
#   Also, Solution 1 checks same-generation by depth equality first
#   (`d[a][0] == d[b][0]`), adding a COUSINS shortcut that the official
#   solution handles via the a>1 && b>1 check regardless of generation.
#
# import sys
# sys.stdin = open('family.in', 'r')
# sys.stdout = open('family.out', 'w')
#
# n, bessie, elsie = input().split()
# n = int(n)
#
# mother = [''] * n
# daughter = [''] * n
# for i in range(n):
#     mother[i], daughter[i] = input().split()
#
#
# def find_mother(cow):
#     """Return the mother of cow, or '' if none exists."""
#     for i in range(n):
#         if cow == daughter[i]:
#             return mother[i]
#     return ''
#
#
# def is_ancestor(cow1, cow2):
#     """
#     Return the number of generations cow1 is removed from cow2
#     if cow1 is a direct ancestor of cow2. Otherwise return -1.
#     """
#     counter = 0
#     while cow2 != '':
#         if cow1 == cow2:
#             return counter
#         cow2 = find_mother(cow2)
#         counter += 1
#     return -1
#
#
# # Walk up from Bessie to find the closest common ancestor (CCA)
# cow = bessie
# b = 0  # distance from CCA to Bessie
# while cow != '':
#     if is_ancestor(cow, elsie) != -1:
#         break        # found the CCA
#     cow = find_mother(cow)
#     b += 1
#
# if cow == '':
#     print('NOT RELATED')
# else:
#     a = is_ancestor(cow, elsie)  # distance from CCA to Elsie
#     if a == 1 and b == 1:
#         print('SIBLINGS')
#     elif a > 1 and b > 1:
#         print('COUSINS')
#     else:
#         # Ensure the younger cow (farther from CCA) is Bessie
#         if a > b:
#             elsie, bessie = bessie, elsie
#             a, b = b, a
#         # Now b > a, and a is either 0 or 1
#         result = elsie + ' is the '
#         result += 'great-' * (b - 2)
#         if b > 1 and a == 0:
#             result += 'grand-'
#         if a == 0:
#             result += 'mother'
#         else:
#             result += 'aunt'
#         result += ' of ' + bessie
#         print(result)
