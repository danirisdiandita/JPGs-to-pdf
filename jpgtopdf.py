from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames

imagelist = ["{:03}.jpg".format(i) for i in range(1,53)]


x = 0
y = 0
w = 210
h = 297


for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")

