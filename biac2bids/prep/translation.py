def trans_dict(filepath, delimiter="\t", header=0):
    """Given a path to a file, translate code to task name.

    Expect the file to be in format (| is the delimiter)
    Code | Task
    -----------
      4  |  train
      ........
    
    params:
        - filepath: path to file which contains the translation mapping
        - delimiter: delimiter for the file (default to tab)
        - header: the number of lines to skip for header
    returns: a translation dict
    """
    with open(filepath, "r") as f:
        for _ in range(header):
            f.readline()
        d = dict()
        for line in f:
            line = line.rstrip()
            info = line.split(delimiter)
            d[info[0]] = info[1]
    return d


def trans_dict_by_folders():
    """Given a folder of 
    """
     

if __name__ == "__main__":
    d = trans_dict("/Users/lpjiang/Research/CBT/Data/func/19492/series_order_note.txt")
    for key, value in d.items():
        print(key, value)