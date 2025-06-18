if __name__ == "__main__":
    import os
    import glob

    datapath = []
    if "textbook" in glob.glob("*"):
        datapath.append("textbook")
        datapath.append("data")
    elif len(glob.glob("*.py")) > 0:
        datapath.extend(["..", "..", "data"])
    datapath = os.path.join(*datapath)

    path = os.path.join(datapath, "rosalind_ba3l.txt")
    if os.path.exists(path):
        with open(path) as f:
            lines = [line.strip() for line in f.readlines()]
            k, d = map(int, lines[0].split())
            pairs = [tuple(line.split("|")) for line in lines[1:]]


def reconstruct_from_gapped_pairs(pairs, k, d):
    prefix_string = pairs[0][0]
    suffix_string = pairs[0][1]

    for a, b in pairs[1:]:
        prefix_string += a[-1]
        suffix_string += b[-1]

    # Now validate: the suffix of prefix_string should match the prefix of suffix_string
    for i in range(k + d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            raise ValueError("No valid string can be reconstructed from the given gapped pairs.")

    return prefix_string + suffix_string[-(k + d):]


if __name__ == "__main__":
    result = reconstruct_from_gapped_pairs(pairs, k, d)
    print(result)
