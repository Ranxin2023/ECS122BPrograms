from typing import List


class SuffixNode:
    def __init__(self, c: str = None) -> None:
        self.c = c
        self.end = False
        self.children = dict()

    def store_node(self, s: str):
        t = self
        for c in s:

            if c in t.children:
                t = t.children[c]
            else:
                t.children[c] = SuffixNode(c)
        t.end = True

    def find_suffix(self, suffix):
        t = self
        for c in suffix:
            if c in t.children:
                t = t.children[c]
            else:
                return False
        return t.end


class SuffixTree:
    def __init__(self, s: str) -> None:
        self.s = s
        self.length = len(s)
        self.suffix_node = SuffixNode()
        self.idx_suffix = []

    def create_suffix_tree(self):
        suffixes = []
        for i in range(self.length):
            suffix = self.s[i:] + "$"
            suffixes.append(suffix)
            self.suffix_node.store_node(suffix)
            self.idx_suffix.append((i, suffix))

    def generate_suffix_array(self) -> List[int]:
        suffix_array = []
        self.idx_suffix = sorted(self.idx_suffix, key=lambda x: x[1])
        for idx, _ in self.idx_suffix:
            suffix_array.append(idx)
        return suffix_array

    def in_tree(self, suffix):
        suffix += "$"
        return self.suffix_node.find_suffix(suffix=suffix)


def main():
    s = "dabcde"
    st = SuffixTree(s)
    st.create_suffix_tree()
    sa = st.generate_suffix_array()
    for idx in sa:
        print(idx, end="\t")
    print()
    print(f"Whether dab is in tree or not: {st.in_tree('dab')}")


if __name__ == "__main__":
    main()
