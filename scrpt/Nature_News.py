#!/usr/bin/env python3

import pdfkit, sys, fitz
import os, time
import datetime


os.system("echo "+time.strftime("%H:%M %D")+" NATURE SCRIPT START")
PATH = sys.path[0]
def UPdate():
    pdfkit.from_url('https://www.nature.com/subjects/biological-sciences', PATH+'/N_BC.pdf')
    os.system("echo Page1"+time.strftime("%H:%M %D")+" NATURE SCRIPT START")
    pdfkit.from_url('https://www.nature.com/subjects/cell-biology', PATH+'/N_CB.pdf')
    os.system("echo Page2"+time.strftime("%H:%M %D")+" NATURE SCRIPT START")
    pdfkit.from_url('https://www.nature.com/subjects/computational-biology-and-bioinformatics', PATH+'/N_BioInfor.pdf')
    os.system("echo Page3"+time.strftime("%H:%M %D")+" NATURE SCRIPT START")
    pdfkit.from_url('https://www.nature.com/subjects/developmental-biology', PATH+'/N_Dev.pdf')
    os.system("echo Page4"+time.strftime("%H:%M %D")+" NATURE SCRIPT START")
    pdfkit.from_url('https://www.nature.com/subjects/biotechnology', PATH+'/N_BioTech.pdf')
    os.system("echo Page5"+time.strftime("%H:%M %D")+" NATURE SCRIPT START")

def pyMuPDF2_fitz(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath) # open document
    for pg in range(pdfDoc.pageCount-1): # iterate through the pages
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate) # 缩放系数1.3在每个维度  .preRotate(rotate)是执行一个旋转
        rect = page.rect                         # 页面大小
        mp = rect.tl + (rect.bl - (0,1224/zoom_x)) # 矩形区域    56=75/1.3333
        clip = fitz.Rect(mp, rect.br)            # 想要截取的区域
        pix = page.getPixmap(matrix=mat, alpha=False, clip=clip) # 将页面转换为图像
        #if not os.path.exists(imagePath):
            #os.makedirs(imagePath)
        pix.writePNG(imagePath+''+'psReport_%s.png' % pg)# store image as a PNG

def main():
    UPdate()
    for i in os.listdir(PATH):
        if "pdf" in i:
            pdfPath = PATH+'/'+i
            imagePath = PATH+'/../Nature/'+i
            pyMuPDF2_fitz(pdfPath, imagePath)#指定想要的区域转换成图片

while True:
    main()
    time.sleep(360000)
