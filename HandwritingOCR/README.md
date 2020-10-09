# Handwriting to Text via OCR (and maybe DeepLEarning)

That ReseNet-example from ML reminded me that I could do something similar for the texts of one of my grandmas.
I love receiving letters and postcards from her, but I have problems with deciphering :')

So why not take that challenge and create a tool, which could convert the photo of a textblock into readable text?

## Steps so far:
* grayscale and preprocess the image (maybe reduce resolution)
* find and extract all image parts which contain handwritten letters (as block or one after another?)
* pre-train a model (ML) to recognize all samples (prepare dataset for this)
