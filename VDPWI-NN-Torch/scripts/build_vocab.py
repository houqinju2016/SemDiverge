import os
import glob
import sys


def build_vocab(filepaths, dst_path, lowercase=True):
    vocab = set()
    for filepath in filepaths:
        with open(filepath) as f:
            for line in f:
                if lowercase:
                    line = line.lower()
                vocab |= set(line.split())
    with open(dst_path, 'w') as f:
        for w in sorted(vocab):
            f.write(w + '\n')

data_dir = sys.argv[1]
build_vocab(
        glob.glob(os.path.join(data_dir, '*/*.toks')),
        os.path.join(data_dir, 'vocab-cased.txt'), False)
