class BWT:
    def __init__(self, s) -> None:
        self.length = len(s)
        self.cycle_s = s + "$" + s

    def find_BWT(self):
        cyclic_sub_rotation = []
        for i in range(self.length + 1):
            cyclic_sub_rotation.append(self.cycle_s[i : i + self.length + 1])
        cyclic_sub_rotation.sort()
        res = ""
        for sub in cyclic_sub_rotation:
            res += sub[-1]
        return res


def main():
    s = "banana"
    bwt = BWT(s)
    print(f"bwt of banana is {bwt.find_BWT()}")


if __name__ == "__main__":
    main()
