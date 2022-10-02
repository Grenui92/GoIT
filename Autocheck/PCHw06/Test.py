# import base64
# s = 'Hello World!!!'
# #sb = s.encode('utf-8')
# bas64 = base64.b64encode(s)
# d_bas64 = bas64.decode('utf-8')
# basi64 = base64.b64decode(bas64)
# print(s, bas64, d_bas64, basi64)

import shutil


archive_name = shutil.make_archive('backup', 'zip', 'Test_folder')
print(archive_name)
shutil.unpack_archive(archive_name, 'Test_unpack_folder')