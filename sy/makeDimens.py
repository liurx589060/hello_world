#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil

class valueParam:
    def __init__(self,name,dpi,resolution):
        self.name = name
        self.dpi = dpi
        self.resolution = resolution
        try:
            resolutions = str(resolution).split('x')
            self.height = float(resolutions[0])
            self.width = float(resolutions[1])
        except:
            print 'valueParam exception'
            self.width = 1080
            self.height = 1920

        print 'valueParam:','name=',name,'---dpi=',dpi,'---resolution=',resolution

topTag = r'<?xml version="1.0" encoding="utf-8"?>' + '\n' + r'<resources>' + '\n'
endTag = r'</resources>'
plusDimenTag = 'sy_p'
minusDimenTag = 'sy_m'
plusCount = 2000
minusCount = 200

standardDpi = 160.0
baseDpi = 480.0
baseScale = 0
baseValueParam = valueParam('0',0,'0x0')
isInit = False
otherResolutionArray = []

baseValues = {valueParam('ldpi',120,'320x240'),valueParam('mdpi',160,'480x320'),valueParam('hdpi',240,'800x480')
    ,valueParam('xhdpi',320,'1280x720'),valueParam('xxhdpi',480,'1920x1080')}

dimenParentDirPrefix = 'values'
dimenFileName = 'sy_dimens.xml'

def createDimens(resolusion,pdScale,pxScale,type,isNodip=False):
    flagStr = '-nodpi-' if isNodip else '-'
    dimenParentDirPrefixPath = dimenParentDirPrefix + '/'+ type + '/' + ('' if type=='dp' else dimenParentDirPrefix + flagStr + resolusion)
    filePath = dimenParentDirPrefixPath + "/" + dimenFileName

    if not os.path.exists(dimenParentDirPrefixPath):
        # 创建文件夹
        os.makedirs(dimenParentDirPrefixPath)
    demenFile = open(filePath,'w+')
    demenFile.truncate()
    # 添加头部
    demenFile.write(topTag)
    for index in range(1,plusCount+1):
        value = (index / pdScale) if type=='dp' else (index*pxScale)
        valueStr = '\t'+ r'<dimen name="' + plusDimenTag + '_' + str(index) + r'">' + str(value) + type + r'</dimen>' + '\n'
        demenFile.write(valueStr)

    for index in range(1,minusCount+1):
        value = (index / pdScale) if type == 'dp' else (index*pxScale)
        valueStr = '\t'+ r'<dimen name="' + minusDimenTag + '_' + str(index) + r'">' + str(-value) + type + r'</dimen>' + '\n'
        demenFile.write(valueStr)

    demenFile.write(endTag)
    demenFile.close()
    return

def createBaseDimens(resolution):
    global baseScale
    global baseDpi
    global isInit
    global baseValueParam
    for value in baseValues:
        if value.resolution == resolution.strip():
            baseDpi = value.dpi
            baseScale = baseDpi / standardDpi
            isInit = True
            baseValueParam = value
            break
    if not isInit:
        print "cannot found the base relosution,not init"
        return False
    createDimens(resolution,baseScale,1,'dp')
    createDimens(resolution, baseScale,1,'px',True)
    return True


def createOtherValueDimens():
    if not isInit:
        return

    for param in baseValues:
        pxScale = param.dpi/float(baseDpi)
        createDimens(param.name,(baseDpi/param.dpi),pxScale,'px')
    return

def createResolutionDimens(resolutionArra):
    if not isInit:
        return

    for resolution in resolutionArra:
        try:
            resolutions = str(resolution).split('x')
            height = float(resolutions[0])
            width = float(resolutions[1])
            scale = baseScale * min(width / baseValueParam.width, height / baseValueParam.height)
            pxScale = min(width / baseValueParam.width, height / baseValueParam.height)
            createDimens(resolution, scale,pxScale,'px',True)
        except:
            print 'valueParam exception'
            return


# 开始基准分辨率创建
if os.path.exists(dimenParentDirPrefix):
    shutil.rmtree(dimenParentDirPrefix)
baseResolution = raw_input('please input the base resolution:')
result = createBaseDimens(baseResolution)

# 开始进行其他分辨率的创建
while(1 and result):
    inputResolution = raw_input('please input the other resolution or input Y to continue:')
    if inputResolution == 'Y':
        print 'start to create the dimen file'
        break
    else:
        otherResolutionArray.append(inputResolution)

print 'otherResolution:',otherResolutionArray

# 开始创建value ldi,mdpi....
createOtherValueDimens()

# 开始创建其他确定分辨率
createResolutionDimens(otherResolutionArray)

print 'dimens complete'

while(1):
    if len(raw_input('please input any to exit:')) > 0:
        break