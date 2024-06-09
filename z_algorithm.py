class ZAlgorithm:
    def __init__(self, s) -> None:
        self.s = s
        self.length = len(s)

    def find_box(self):
        z_box = [0] * (self.length - 1)
        right = 0
        for i in range(1, self.length):
            if i >= right:
                idx = 0
                right = i
                while i + idx < self.length and self.s[i + idx] == self.s[idx]:
                    right += 1
                    idx += 1
                left = i
                z_box[i - 1] = right - left

            else:
                if self.s[i] == self.s[0]:
                    z_box[i - 1] = right - i
            # print(f"left:{left};right:{right}")

        return z_box

    def change_s(self, s):
        self.s = s
        self.length = len(s)

    def find_pattern(self, p: str):
        idxs = []
        p_len = len(p)
        original_s = self.s
        self.change_s(p + "$" + self.s)
        box = self.find_box()
        print(box)
        for i in range(self.length - 1):
            if box[i] == p_len:
                idxs.append(i - p_len)
        self.change_s(original_s)
        return idxs


def main():
    s = "daadaadaadaaxdaadaa"
    za = ZAlgorithm(s)
    print(za.find_box())
    za.change_s("aaaaaaaaxaaa")
    print(za.find_box())
    za.change_s("daadaadaadaaxdaadaa")
    print(za.find_pattern("daa"))


if __name__ == "__main__":
    main()
