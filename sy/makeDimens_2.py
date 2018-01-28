#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class valueParam:
    def __init__(self,name,dpi,resolution):
        self.name = name
        self.dpi = dpi
        self.resolution = resolution
        try:
            resolutions = str(resolution).split('x')
            self.width = int(resolutions[0])
            self.height = int(resolutions[1])
        except:
            print 'valueParam exception'
        else:
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

def createDimens(resolusion,scale):
    dimenParentDirPrefixPath = dimenParentDirPrefix + '/'+ dimenParentDirPrefix + '-' + resolusion
    filePath = dimenParentDirPrefixPath + "/" + dimenFileName
    if not os.path.exists(dimenParentDirPrefixPath):
        # 创建文件夹
        os.makedirs(dimenParentDirPrefixPath)
    demenFile = open(filePath,'w+')
    demenFile.truncate()
    # 添加头部
    demenFile.write(topTag)
    for index in range(1,plusCount+1):
        value = index / scale
        valueStr = '\t'+ r'<dimen name="' + plusDimenTag + '_' + str(index) + r'">' + str(value) + r'dp</dimen>' + '\n'
        demenFile.write(valueStr)

    for index in range(1,minusCount+1):
        value = index / scale
        valueStr = '\t'+ r'<dimen name="' + minusDimenTag + '_' + str(index) + r'">' + str(-value) + r'dp</dimen>' + '\n'
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
    createDimens(resolution,baseScale)
    return True


def createOtherValueDimens():
    if not isInit:
        return

    for param in baseValues:
        createDimens(param.name,baseScale*(baseDpi/param.dpi))
    return

def createResolutionDimens(resolutionArra):
    if not isInit:
        return

    for resolution in resolutionArra:
        try:
            resolutions = str(resolution).split('x')
            width = float(resolutions[0])
            height = float(resolutions[1])
            scale = baseScale * min(baseValueParam.width / width, baseValueParam.height / height)
            createDimens(resolution, scale)
        except:
            print 'valueParam exception'
            return


# 开始基准分辨率创建
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
# createOtherValueDimens()

# 开始创建其他确定分辨率
createResolutionDimens(otherResolutionArray)