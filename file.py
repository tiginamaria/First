import sys
import hashlib
import os


def fhash(path, mod=8192):
    with open(path, 'rb') as x:
        hasher = hashlib.md5()
        tmp = x.read(mod)
        while tmp:
            hasher.update(tmp)
            tmp = x.read(mod)
    return hasher.hexdigest()


def dfind(parent):
    fdups = {}
    for folders, _, files in os.walk(parent):
        for fname in files:
            if fname[0] != '.' and fname[0] != '~':
                if not(os.path.islink(fname)):
                    path = os.path.join(os.path.realpath(folders), fname)
                    hashf = fhash(path)
                    if hashf in fdups:
                        fdups[hashf].append(path)
                    else:
                        fdups[hashf] = [path]
    return fdups


def fprint(dicts):
    for files in filter(lambda x: len(x) > 1, dicts.values()):
        print(':'.join(files))


def main():
    folders = sys.argv[1]
    fprint(dfind(folders))


if __name__ == '__main__':
    main()
