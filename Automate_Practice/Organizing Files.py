# import os
# import zipfile

# os.chdir('C:\\Users\\Admin\\Documents\\Python practice\\Automate')
# print('Start')
# exampleZip = zipfile.ZipFile('MED.zip')
# a = exampleZip.namelist()
# print(a)
# exampleZip.extractall('C:\\Users\\Admin\\Documents\\Python practice\\ZipFIleOpener')
# exampleZip.close()
# print('Done')

# import shutil a = shutil.copytree('D:\\Temp', 'C:\\Users\\Admin\\Documents\\Python
# practice\\Automate\\CopiedFileNew2') print(a) b = shutil.move('C:\\Users\\Admin\\Desktop\\Documents\\BMI',
# 'C:\\Users\\Admin\\Documents\\Python practice\\Automate\\CopiedFileNew') print(b) print('Done')

# import send2trash   # Sends files and folders to recycle bin instead of permanently deleting them like os and shutil
# print('Start')
# send2trash.send2trash('C:\\Users\\Admin\\Documents\\Python practice\\Automate\\CopiedFileNew2')
# print('Done')

# Create a zip file of a folder and open it
import zipfile
for i in range(35):
    newZip = zipfile.ZipFile('C:\\Users\\Admin\\Documents\\Python practice\\Automate\\NEW.zip', "a")
    newZip.write('C:\\Users\\Admin\\Documents\\Python practice\\Automate\\CapitalsQuiz_Answer%s.txt' % (i+1),
                 compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
print('Done')
