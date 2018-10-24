import os
from framework import getcwd

class delete:      #用户删除所有的日志，截图，报告,日常调试清理时使用
    def delete_all(self):
        dir_list = ['logs', 'screenshots', 'test_report']  # 要删除文件的目录名
        for dir in dir_list:
            dirPath = getcwd.get_cwd() + '\\' + dir  # 拼接删除目录完整路径
            file_list = os.listdir(dirPath)  # 返回目录下的文件list
            for i in file_list:
                file_path = os.path.join(dirPath, i)  # 拼接文件的完整路径
                os.remove(file_path)

if __name__ == '__main__':
    delete = delete()
    delete.delete_all()
