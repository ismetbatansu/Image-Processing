
Skip to content

    Pull requests
    Issues
    Marketplace
    Explore

    @ismetbatansu

You don’t have any verified emails. We recommend verifying at least one email.
Email verification helps our support team verify ownership if you lose account access and allows you to receive all the notifications you ask for.

1
1

    1

haticeerdagi/Image_Processing
Code
Issues 0
Pull requests 0
Projects 0
Wiki
Insights
Image_Processing/HAFTA2.py
de10498 on 18 Oct
@haticeerdagi haticeerdagi Add files via upload
39 lines (27 sloc) 1.07 KB
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img_mpimg.imread('test1.jpg')
#%matplotlib inline
import numpy as np

im_1=plt.imread("1.jpg")

plt.imshow(im_1)
plt.show()

def fonk1(image_1):
    print("Resmin boyutu = ",image_1.ndim,"\n") 
    print("Resmin Shape deðeri = ",image_1.shape,"\n")
    print("Red için min deðer = ",image_1[:,:,0].min(),"\n") 
    print("Red için max deðer = ",image_1[:,:,0].max(),"\n")
    
fonk1(im_1)

im_1[:,:,0]=im_1[:,:,0]+50

plt.imshow(im_1)
plt.show()

def my_function_1(my_img):
    
    print("eksen sayisi : ",my_img.ndim)
    print("eksen degerleri :",my_img.shape)
    
    print("en kucuk kirmizi renk degeri : ",np.min(my_img[:,:,0]))
    print("en kucuk kirmizi renk degeri : ",np.max(my_img[:,:,0]))
    
    print("en kucuk yesil renk degeri : ",np.min(my_img[:,:,1]))
    print("en kucuk yesil renk degeri : ",np.max(my_img[:,:,1]))
    
    print("en kucuk mavi renk degeri : ",np.min(my_img[:,:,2]))
    print("en kucuk mavi renk degeri : ",np.max(my_img[:,:,2]))
    
my_function_1(im_1)

    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Press h to open a hovercard with more details.
