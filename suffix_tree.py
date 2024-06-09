class SuffixTreeNode:
    def __init__(self, c: str = None) -> None:
        self.c = c
        self.end = False
        self.children = [None] * 26

    def store_node(self, s: str):
        t = self
        for c in s:
            if self.children[ord(c) - ord("a")] != None:
                t = t.children[ord(c) - ord("a")]
            else:
                t.children[ord(c) - ord("a")] = SuffixTree(c)
        t.end = True


class SuffixTree:
    def __init__(self, s: str) -> None:
        self.s = s
        self.length = s.length
        self.suffix_node = SuffixTreeNode()

    def create_suffix_tree(self):
        suffixes = []
        for i in range(self.length):
            suffix = self.s[i:] + "$"
            suffixes.append(suffix)
            self.suffix_node.store_node(suffix)
