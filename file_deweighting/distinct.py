# 去除leakCanary/blockCanary产生的重复日志文件
from file_deweighting import utils


def leak_distinct():
    filenamepathmap = utils.visitdir(utils.LEAKCANARY_LOG_PATH)
    filenamecontentmap = utils.getfilecontentmap(filenamepathmap, utils.LEAKPATTERN)
    filenamecontentmap_noduplicate = utils.tuple_r_dict(utils.tuple_r_dict(filenamecontentmap))
    utils.copyfiles(filenamepathmap, filenamecontentmap_noduplicate, utils.LEAKCANARY_LOG_PATH)
    print("leakCanary去重成功")


# blockCanary去重,重新生成去重文件
def block_distinct():
    filenamepathmap = utils.visitdir(utils.BLOCKCANARY_LOG_PATH)
    filenamecontentmap = utils.getfilecontentmapex(filenamepathmap)
    filenamecontentmap_noduplicate = utils.tuple_r_dict(utils.tuple_r_dict(filenamecontentmap))
    utils.copyfiles(filenamepathmap, filenamecontentmap_noduplicate, utils.BLOCKCANARY_LOG_PATH)
    print("blockCanary去重成功")


if __name__ == '__main__':

    leak_distinct()
    # block_distinct()
