import os
import image    #pip3 uninstall pillow, PIL, then easy_install image
import PIL      #easy_install pillow
import numpy as np  #pip3 install numpy



#Please forgive the sloppynes - I did this quick and havent cleaned up yet...

currentDir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.realpath("{0}/../../../resources/htsProgrammingChallenge2.png".format(currentDir))

# This code is related to the HackThisSite.org challenge
# hackthissite challenge here -> https://www.hackthissite.org/missions/prog/2/
# image used for testing in the resources folder - relative path used above should prevent the need to modify that path


if __name__ == '__main__':

    img = PIL.Image.open(str(filename))
    image_sequence = img.getdata()
    image_array = np.array(image_sequence)

    print("img pixel array size is: " + str(image_array.size))

    tcounter = 0
    for a in image_array:
        tcounter = tcounter + 1
        print("a: " + str(a))

    print("tcounter finshed at count: " + str(tcounter));

    print(image_array)
    # print( "inmg: " + (str(img)))
    #---------------------------------
    # col, row = img.size
    # data = np.zeros((row * col, 5))
    # pixels = img.load()
    #---------------------------------
    # for i in range (row):
    #     for j in range (col):
    #         print(str(row(i.as_integer_ratio())) + str(col(j.as_integer_ratio())))
    #         if j == 99:
    #             print("\r\n")
    # img = imread("C:\\Users\\mason\\Downloads\\download.png")
    # print(str(img))
    #--------------------------------------
    row,col = img.size
    data=[] #r,g,b,i,j
    pixels=img.load()

    #gather all the pixels from the PNG file
    for i in range(row):
        for j in range(col):
            data.append(pixels[i, j])

    tempStr = ""
    counter = 0
    #for the star coding challenge, we need to track the row index for each star.
    # Then, aside from the first star, each next stars value is ( valueOf(i) - valueOf(i-1))
    # such that the difference between the previous number is the actual ASCII number intended for that star

    starRowIndexVals = []
    for d in data:

        counter = counter + 1
        tempStr += (str(d))

        if(counter % 100 == 0):
            print(tempStr);
            tempStr = ""


        if d == 1:
            print("row counter /ASCII value for white star is: " + str(counter))
            starRowIndexVals.append(counter)
        #if counter == 100:
         #   counter = 0;

    print("starRowIndexVals are" + str(starRowIndexVals));

    #normally somewhere around 45 - original image is 46
    print("total star count in image is: " + str(len(starRowIndexVals)))


    dynamicOriginalToMidStarList = starRowIndexVals.copy()

#easier way here

    shiftedAsciiStarValsEasy = []
    counter2 = 0
    for star in starRowIndexVals:
        if(counter2 == 0):
            counter2 = counter2 + 1
            shiftedAsciiStarValsEasy.append(star);
            continue
        elif(counter2 == 1):
            counter2 = counter2 + 1
            tempStar = star - starRowIndexVals[int(counter2)-2]
            if tempStar < 0:
                tempStar = int(tempStar) * -1
            shiftedAsciiStarValsEasy.append(tempStar)
        else:
            counter2 = counter2 + 1
            #star 2 was originally at value 100, after difffing from star 1, star 2 becomes now 54 because 100-46=54.
            #Start 3, which is currntly at say 24, needs to compare against star 2 AFTER star 2 has made its adjustment
            # from star 1. Thus, we start to pull from the "final" array so that when we compare current star against previous
            #star, we are comparing against the previous start WITH the changed value from the diff rather than the orignal index value
            tempStar = star - starRowIndexVals[int(counter2)-2]
            if tempStar < 0:
                tempStar = int(tempStar) * -1
            shiftedAsciiStarValsEasy.append(tempStar)



#hard way below
    shiftedAsciiStarVals = []
    counter3 = 0
    for star in starRowIndexVals:
        if(counter3 == 0):
            counter3 = counter3 + 1
            shiftedAsciiStarVals.append(star);
            continue
        elif(counter3 == 1):
            counter3 = counter3 + 1
            tempStar = star - starRowIndexVals[int(counter3)-2]
            if tempStar < 0:
                tempStar = int(tempStar) * -1
            shiftedAsciiStarVals.append(tempStar)
        else:
            counter3 = counter3 + 1
            #star 2 was originally at value 100, after difffing from star 1, star 2 becomes now 54 because 100-46=54.
            #Start 3, which is currntly at say 24, needs to compare against star 2 AFTER star 2 has made its adjustment
            # from star 1. Thus, we start to pull from the "final" array so that when we compare current star against previous
            #star, we are comparing against the previous start WITH the changed value from the diff rather than the orignal index value
            tempStar = star - shiftedAsciiStarVals[int(counter3)-2]
            if tempStar < 0:
                tempStar = int(tempStar) * -1
            shiftedAsciiStarVals.append(tempStar)


    print("shiftedAsciiStarVals are: " + str(shiftedAsciiStarVals))

    print("the final result...")

    print("hard arry is: " + str(shiftedAsciiStarVals));

    hardString=""
    for decyptedLetter in shiftedAsciiStarVals:
        print("decryptedLetter number is: " + str(decyptedLetter))
        hardString +=chr(decyptedLetter)

    print("hard string is: " + hardString );

    print("easy arry is: " + str(shiftedAsciiStarValsEasy));
    easyString = ""
    for easyDecryptedLetter in shiftedAsciiStarValsEasy:
        print("decrypted easy letter list is: " + str(easyDecryptedLetter))
        easyString += chr(easyDecryptedLetter)


    print("easy string is: " + easyString );
