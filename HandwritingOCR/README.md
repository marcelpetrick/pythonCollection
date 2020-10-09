# Handwriting to Text via OCR (and maybe DeepLEarning)

That ReseNet-example from ML reminded me that I could do something similar for the texts of one of my grandmas.
I love receiving letters and postcards from her, but I have problems with deciphering :')

So why not take that challenge and create a tool, which could convert the photo of a textblock into readable text?

## Steps so far:
* grayscale and preprocess the image (maybe reduce resolution)
* find and extract all image parts which contain handwritten letters (as block or one after another?)
* pre-train a model (ML) to recognize all samples (prepare dataset for this)

## research is necessary - helpful material
* good, but has strong issues: <https://www.pyimagesearch.com/2020/08/24/ocr-handwriting-recognition-with-opencv-keras-and-tensorflow/>
* extract handwriting: <https://stackoverflow.com/questions/58141153/how-do-i-isolate-handwritten-text-from-an-image-using-opencv-and-python>
* <http://cs231n.stanford.edu/reports/2017/pdfs/810.pdf>
+ promising approach with ResNet101: <https://medium.com/@akshaychougule/handwritten-devanagari-character-identification-using-resnet-b90894b42c4d>
* almost forgotten about this: <https://modelzoo.co/>
