from typing import List


class SuffixNode:
    def __init__(self, c=None) -> None:
        self.c = c
        self.end = -1
        self.children = [None] * 128

    def store_node(self, s: str, idx: int):
        t = self
        for c in s:

            if t.children[ord(c)] != None:
                t = t.children[ord(c)]
            else:
                t.children[ord(c)] = SuffixNode(c)
                t = t.children[ord(c)]
        t.end = idx

    def find_suffix(self, suffix):
        t = self
        for c in suffix:
            if t.children[ord(c)] != None:
                t = t.children[ord(c)]
            else:
                return False
        return t.end != -1

    def generate_sa(self, sa):
        if self.end != -1:
            sa.append(self.end)
        for child in self.children:
            if child != None:
                child.generate_sa(sa)


class SuffixTree:
    def __init__(self, s: str) -> None:
        self.s = s
        self.length = len(s)
        self.suffix_node = SuffixNode()
        self.idx_suffix = []
        self.suffixes = []

    def create_suffix_tree(self):
        # suffixes = []
        for i in range(self.length):
            suffix = self.s[i:]
            self.suffixes.append(suffix)
            self.suffix_node.store_node(suffix, i)
            self.idx_suffix.append((i, suffix))

    def generate_suffix_array_brute_force(self) -> List[int]:
        suffix_array = []
        self.idx_suffix = sorted(self.idx_suffix, key=lambda x: x[1])
        for idx, _ in self.idx_suffix:
            suffix_array.append(idx)
        return suffix_array

    def in_tree(self, suffix):
        return self.suffix_node.find_suffix(suffix=suffix)

    def generate_suffix_array_by_suffix_tree(self) -> List[int]:
        sa = []
        self.suffix_node.generate_sa(sa)
        return sa

    def search_pattern(self, p: str):
        sa = self.generate_suffix_array_by_suffix_tree()
        left = 0
        right = self.length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if p > self.suffixes[sa[mid]]:
                left = mid + 1
            elif p < self.suffixes[sa[mid]]:
                right = mid - 1
            else:
                return True
        return False

    def generate_suffix_array_linearly(self):
        new_s = self.s + "$$"
        all_mode_one_two_substr = []
        for i in range(self.length):
            if i % 3 == 0 or i % 3 == 1:
                all_mode_one_two_substr.append(new_s[i : i + 3])
        self.radix_sort(all_mode_one_two_substr)

    def radix_sort(self, idx, arr):
        if idx == 3:
            return arr
        radix = [[] for i in range(27)]


def main():
    s = "dabcde"
    st = SuffixTree(s)
    st.create_suffix_tree()
    print(f"sa via brute force:{st.generate_suffix_array_brute_force()}")
    print(f"sa via suffix tree:{st.generate_suffix_array_by_suffix_tree()}")
    print(f"Whether dab is in tree or not: {st.in_tree('dab')}")
    print(f"Whether cde is in sa or not:{st.search_pattern('cde')}")


if __name__ == "__main__":
    main()
