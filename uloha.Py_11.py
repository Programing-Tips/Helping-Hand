import barcode
from barcode.writer import ImageWriter

#treba stiahnut: pip install pillow, a ešte, pip install python-barcode
number = input()

barcode_format = barcode.get_barcode_class('ean8')
my_barcode = barcode_format(number, writer=ImageWriter())
#treba určiť kam sa obrazok uloží
my_barcode.save(r'E:\Nový priečinok\Barcode_17.png')