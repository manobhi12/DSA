class Solution:
    def sortedListToBST(self, head):
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        size = getLength(head)
        self.curr = head

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            left = build(l, mid - 1)

            root = TreeNode(self.curr.val)
            root.left = left

            self.curr = self.curr.next

            root.right = build(mid + 1, r)
            return root

        return build(0, size - 1)