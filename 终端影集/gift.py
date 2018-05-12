from PIL import Image
import os
import time

codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
count = len(codeLib)

def transform_image(image_file):
    #转换为黑白图片，参数"L"表示黑白模式
    image_file = image_file.convert("L")
    codePic = ''
    #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            gray = image_file.getpixel((w,h))
            #建立灰度与字符集的映射
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]
        codePic = codePic+'\r\n'
    return codePic

def main():

    # 获取终端的高度
    height = os.get_terminal_size().lines

    # 获取同级目录文件夹下所有图片的列表
    the_names = os.listdir("./images")

    # 开启循环
    while 1 :
        # 遍历每张图片
        for the_name in the_names:
            try:

                # 清屏幕
                print("\n"*height)
                # 拼合当前图片名
                my_img = open("./images/"+the_name,'rb')
                # 打开当前图片
                image_file = Image.open(my_img)
                #调整图片尺寸到原来的四分之一
                # image_file=image_file.resize((int(image_file.size[0]*0.5), int(image_file.size[1]*0.5)))
                image_file=image_file.resize((250, 250))

                #打印图片
                print(transform_image(image_file))
                # 每张图片停顿5秒
                time.sleep(5)
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
