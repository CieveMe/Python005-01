import time
import logging
import os
import sys
from pathlib import *

#用字符串拼接目录的话没有方法可以判断路径是否存在，所以只能用pathlib的路径拼接方法。进而用is_dir()进行判断
# logdir = 'var/log/python-'+time.strftime("%Y%m%d")

# systemlogdir = Path('/var/log')
systemlogdir = Path('var/log')
today = time.strftime('%Y%m%d')
logdir = systemlogdir.joinpath('python-{}'.format(today))
logfile = logdir.joinpath('opened.log')

# 目标目录是否存在，没有则创建
if not logdir.is_dir():
    try:
        # 创建目录
        os.makedirs(logdir)
    except OSError as err:
        print('Create log directory failed: {}'.format(err))
        sys.exit(1)

# 配置日志参数
logging.basicConfig(filename=logfile,
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %X',
                    format='%(asctime)s %(name)-8s %(levelname)-8s  %(message)s')
logging.info("function is executed at: {}".format(time.ctime()))