import shutil,os


def get_files_for_gdc(path,path2, n=1):
    '''
    递归遍历文件夹
    :param path:  初始路径
    :param n:  文件夹层数
    :return:
    '''
    # 查看当前文件夹
    files = os.listdir(path)
    if n == 1:
        print(path + ':')
    # 获取每个文件名
    for file in files:
        # 路径 + 文件名
        file_path = os.path.join(path, file)
        # 判断 file_path 是否为文件夹
        if os.path.isdir(file_path):
            # print('\t' * n, file + ':')
            # 将拼接后的路径传递进去，继续遍历
            get_files_for_gdc(file_path, path2,n + 1)
        else:
            # 直接输出文件名
            if os.path.splitext(file)[-1][1:] == 'gdc':
                file_path1 = path2 + '\\' + os.path.splitext(file)[0] + '.gd'
                file_path2 = os.path.join(path, os.path.splitext(file)[0] + '.gd')
                file_path3 = os.path.join(path, os.path.splitext(file)[0] + '.gdc')
                file_path4 = os.path.join(path, os.path.splitext(file)[0] + '.gd.remap')
                shutil.copy(file_path1, file_path2)
                os.remove(file_path3)
                os.remove(file_path4)
                print('\t' * n, os.path.abspath(file_path))

target_dir = r'F:\qqq'

get_files_for_gdc(target_dir,r'F:\target')


def get_files(path,list,n=1):
    '''
    递归遍历文件夹
    :param path:  初始路径
    :param n:  文件夹层数
    :return:
    '''
    # 查看当前文件夹
    files = os.listdir(path)
    if n == 1:
        print(path + ':')
    # 获取每个文件名
    for file in files:
        # 路径 + 文件名
        file_path = os.path.join(path, file)
        # 判断 file_path 是否为文件夹
        if os.path.isdir(file_path):
            # print('\t' * n, file + ':')
            # 将拼接后的路径传递进去，继续遍历
            get_files(file_path, list,n + 1)
        else:
            # 直接输出文件名
            if os.path.splitext(file)[-1][1:] == 'import':
                filename = os.path.splitext(file)[0]
                it = iter(list)    # 创建迭代器对象
                for x in it:
                    if filename in x:
                        shutil.copy(x, path + '\\' + filename)
                        break

def get_import_list(path):
    files = os.listdir(path)
    list = []
    for file in files:
        suffix = os.path.splitext(file)[-1][1:]
        if suffix == 'png' or suffix == 'wav' or suffix == 'ogg' or suffix == 'svg':
            list.append(path + '\\' + os.path.basename(file))
    return list

list = get_import_list(target_dir + r'\.import')
get_files(target_dir ,list)

