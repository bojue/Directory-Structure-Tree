import os
path = "/Users/bojue/Desktop/workspace/mes-base/projects/editrform/src/components/editor-form"
files = os.listdir(path)
spacingCount = 1

print('start...\n初始化路径:', path)
def getFileByFiles(params, nextPath, spacingCount):
  for file in params:
    file_path = nextPath + "/" + file
    isDir = os.path.isdir(file_path)
    if isDir :
      isDirBool = os.path.isdir(file_path)
      if isDirBool: 
        sub_file = os.listdir(file_path)
        print('|'+ '  ' * (spacingCount -1) + '|__' * 1, file)
        getFileByFiles(sub_file, file_path, spacingCount + 1)
    else:
      if file.endswith('.ts') and not file.endswith('.spec.ts') and not file.endswith('component.ts') and file.startswith('xt-setting'):
        print('|'+ '  ' * (spacingCount -1) + '|__' * 1, file)

getFileByFiles(files,path, spacingCount)
print('\ndone!')


