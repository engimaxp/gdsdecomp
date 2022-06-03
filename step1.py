import shutil,os


def get_files(path,path2, n=1):
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
            get_files(file_path, path2,n + 1)
        else:
            # 直接输出文件名
            if os.path.splitext(file)[-1][1:] == 'gdc':
                shutil.copy(os.path.abspath(file_path), path2 + '\\' + os.path.basename(file))
                print('\t' * n, os.path.abspath(file_path))


get_files(r'F:\qqq',r'F:\target')
exit()
