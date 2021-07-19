import glob
from distutils.dir_util import copy_tree

moto = glob.glob('C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/img/*')
saki_dir = 'C:/xampp/htdocs/niku/niku-site/img'
moto_dir = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/img'

copy_tree(moto_dir, saki_dir)