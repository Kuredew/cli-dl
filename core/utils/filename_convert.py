def convert(str):
    return "".join(i for i in str if i not in "\/:*?<>|")