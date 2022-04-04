from fileinput import filename
from tempfile import TemporaryDirectory, mkdtemp, TemporaryFile
import pdf2image
def split(fileName):
    with TemporaryDirectory() as path: 
        convert = pdf2image.convert_from_path(fileName, dpi = 500, output_folder=path)
        for i in range(len(convert)):
            convert[i].save('Output_Images/'+'page'+str(i+1)+'.jpg', 'JPEG')