class ZAlgorithm:
    def __init__(self, s) -> None:
        self.s = s
        self.length = len(s)

    def find_max_suffix(self):
        z_box = [0] * (self.length - 1)
        right = 0
        for i in range(1, self.length):
            if i > right:
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
            print(f"left:{left};right:{right}")

        return z_box

    def change_s(self, s):
        self.s = s
        self.length = len(s)


def main():
    s = "daadaadaadaa$daadaa"
    za = ZAlgorithm(s)
    print(za.find_max_suffix())
    za.change_s("aaaaaaaa$aaa")
    print(za.find_max_suffix())


if __name__ == "__main__":
    main()
