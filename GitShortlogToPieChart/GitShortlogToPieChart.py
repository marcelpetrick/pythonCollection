import matplotlib.pyplot as plt

#-------------------------

def generateExampleChart():
        # modified example taken from: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
        # and: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,
                #explode=explode,
                labels=labels,
                autopct='%1.1f%%',
                shadow=False,
                startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

#-------------------------

def prepareFileContent():
     with open('testdata.csv') as file:
             for line in file.readlines():
                # trim it from whitespace
                strippedLine = line.strip()
                print(strippedLine) # todom remove
                # split at first occasion of " "
             


prepareFileContent()
#-------------------------
#-------------------------
#-------------------------
#-------------------------

