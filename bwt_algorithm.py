class BWT:
    def __init__(self, s) -> None:
        self.length = len(s)
        self.s = s + "$"
        self.cycle_s = s + "$" + s
        self.cyclic_sub_rotation = []

    def find_BWT(self):
        for i in range(self.length + 1):
            self.cyclic_sub_rotation.append(self.cycle_s[i : i + self.length + 1])
        self.cyclic_sub_rotation.sort()
        print(self.cyclic_sub_rotation)
        res = ""
        for sub in self.cyclic_sub_rotation:
            res += sub[-1]
        return res

    def find_suffix_array(self):
        sa = []
        for sub in self.cyclic_sub_rotation:
            end_idx = 0
            for i, c in enumerate(sub):
                if c == "$":
                    end_idx = i
                    break
            sa.append(self.length - end_idx)
        return sa


def main():
    s = "banana"
    bwt = BWT(s)
    print(f"bwt of banana is {bwt.find_BWT()}")
    print(f"suffix array is:{bwt.find_suffix_array()}")


if __name__ == "__main__":
    main()
