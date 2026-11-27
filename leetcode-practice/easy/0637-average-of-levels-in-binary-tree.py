# LeetCode 637. Average of Levels in Binary Tree — Easy
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Submission 2197508268 — Accepted, Python3
#
# My thinking: level by level with a queue. I take
# all the nodes of one level, add up their values,
# divide by how many there are, and put their
# children in the queue for the next level.

class Solution:
    def averageOfLevels(self, root) -> list[float]:
        result = []
        queue = [root]
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_count)
        return result
