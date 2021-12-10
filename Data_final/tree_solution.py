    def _traverse_forward(self, node):
        """
        This is the answer to the challenge is this.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)