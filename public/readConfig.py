import configparser
cp = configparser.ConfigParser(allow_no_value=True)
def read(file,item):
    cp.read(file)
    itemList = cp.items(item)
    return itemList