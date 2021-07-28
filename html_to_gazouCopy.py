import glob
from distutils.dir_util import copy_tree
import shutil

moto = glob.glob('C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/img/*')
saki_dir = 'C:/xampp/htdocs/niku/niku-site/img'
moto_dir = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/img'

copy_tree(moto_dir, saki_dir)

saki_dir = 'C:/xampp/htdocs/niku/niku-site/css'
moto_dir = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/css'
copy_tree(moto_dir, saki_dir)

saki_dir = 'C:/xampp/htdocs/niku/niku-site/js'
moto_dir = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/js'
copy_tree(moto_dir, saki_dir)

saki_dir = 'C:/xampp/htdocs/niku/niku-site/beef_blog'
moto_dir = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_blog'
copy_tree(moto_dir, saki_dir)


saki_f = 'C:/xampp/htdocs/niku/niku-site/styles.css'
moto_f = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/styles.css'
shutil.copyfile(moto_f, saki_f)
#shutil.copyfile(saki_f, moto_f)

saki_f = 'C:/xampp/htdocs/niku/niku-site/rss.xml'
moto_f = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/rss.xml'
shutil.copyfile(moto_f, saki_f)


saki_f = 'C:/xampp/htdocs/niku/niku-site/style_map.css'
moto_f = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/style_map.css'
shutil.copyfile(moto_f, saki_f)