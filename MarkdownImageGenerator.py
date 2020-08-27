# smoil script te generate the markdown-tags for a list of 38 images.
# lol, never do something manually what you can automate in 2 hrs ..

# author: mail@marcelpetrick.it
# license: GPL v3.0

#-----------------------------------------------------------------
def makeTwoDigitsString(number):
    numStr = str(number)
    if len(numStr) == 1:
        numStr = "0" + numStr

    return numStr

#-----------------------------------------------------------------

for number in range(1, 38):
    result = "![](Day3_question" + makeTwoDigitsString(number) + ".png)"
    print(result)
    print("-----") # added to have a separator, because white-bordered screenshots on white background are not distinguishable

#-----------------------------------------------------------------

# result:
# ![](Day3_question01.png)
# ![](Day3_question02.png)
# ![](Day3_question03.png)
# ![](Day3_question04.png)
# ![](Day3_question05.png)
# ![](Day3_question06.png)
# ![](Day3_question07.png)
# ![](Day3_question08.png)
# ![](Day3_question09.png)
# ![](Day3_question10.png)
# ![](Day3_question11.png)
# ![](Day3_question12.png)
# ![](Day3_question13.png)
# ![](Day3_question14.png)
# ![](Day3_question15.png)
# ![](Day3_question16.png)
# ![](Day3_question17.png)
# ![](Day3_question18.png)
# ![](Day3_question19.png)
# ![](Day3_question20.png)
# ![](Day3_question21.png)
# ![](Day3_question22.png)
# ![](Day3_question23.png)
# ![](Day3_question24.png)
# ![](Day3_question25.png)
# ![](Day3_question26.png)
# ![](Day3_question27.png)
# ![](Day3_question28.png)
# ![](Day3_question29.png)
# ![](Day3_question30.png)
# ![](Day3_question31.png)
# ![](Day3_question32.png)
# ![](Day3_question33.png)
# ![](Day3_question34.png)
# ![](Day3_question35.png)
# ![](Day3_question36.png)
# ![](Day3_question37.png)
