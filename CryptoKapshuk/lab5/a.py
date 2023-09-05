from PIL import Image
import numpy as np


class Stego():
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_ext = image_path.split(".")[-1]
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.output_image = None

    def hide(self, hide_path):
        array = np.array(list(self.image.getdata()))
        num_of_channels = 3

        total_pixels = array.size // num_of_channels
        with open(hide_path, "rb") as f:
            message = f.read()

        req_pixels = len(message) * 8 // 3 + 17
        header = len(message)
        if req_pixels > total_pixels:
            raise RuntimeError('Cannot hide data. Need a larger container')
        else:
            index = 0
            k = 0
            header_i = 0
            for p in range(total_pixels):
                for q in range(num_of_channels):
                    if index < header:
                        if header_i > 31:
                            m = message[index]
                        else:
                            m = header
                        a = bin(m)
                        old = array[p][q]
                        new = self.setBit(old, 0) if self.testBit(m, k) else self.clearBit(old, 0)
                        array[p][q] = new
                        if header_i > 31:
                            k += 1
                            if k > 7:
                                k = 0
                                index += 1
                        else:
                            k += 1
                            if k > 31:
                                k = 0
                            header_i += 1

            array = array.reshape(self.image.height, self.image.width, num_of_channels)
            self.output_image = Image.fromarray(array.astype('uint8'), self.image.mode)
            print("Data has been hidden")
        return message.decode("utf8")

    def reveal(self, reveal_path):
        array = np.array(list(self.image.getdata()))
        num_of_channels = 3
        total_pixels = array.size // num_of_channels

        hidden_bits = bytearray()
        index = 0
        k = 0
        i = 0
        header = 0
        header_i = 0
        for p in range(total_pixels):
            for q in range(num_of_channels):
                m = array[p][q]
                if header_i > 31:
                    if index < header:
                        old = i
                        new = self.setBit(old, k) if self.testBit(m, 0) else self.clearBit(old, k)
                        i = new
                        k += 1
                        if k > 7:
                            k = 0
                            index += 1
                            hidden_bits.append(i)
                            i = 0
                else:
                    old = header
                    new = self.setBit(old, header_i) if self.testBit(m, 0) else self.clearBit(old, header_i)
                    header = new
                    header_i += 1
        message = hidden_bits.decode("utf8")
        print("Data has been revealed successfully!")

        with open(reveal_path, "w") as f:
            f.write(message)
        return message

    def save(self, save_path=None):
        if not self.output_image:
            raise Exception("Info wasn`t hided")
        if not save_path:
            save_path = self.image_path[:-(len(self.image_ext)+1)]+"_hide."+self.image_ext
        self.output_image.save(save_path)

    # testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
    def testBit(self, int_type, offset):
        mask = 1 << offset
        return (int_type & mask)

    # setBit() returns an integer with the bit at 'offset' set to 1.
    def setBit(self, int_type, offset):
        mask = 1 << offset
        return (int_type | mask)

    # clearBit() returns an integer with the bit at 'offset' cleared.
    def clearBit(self, int_type, offset):
        mask = ~(1 << offset)
        return (int_type & mask)
    
    
im = Stego("4.bmp")
m1 = im.hide("v35.txt")
im.save()
im = Stego("4_hide.bmp")
r1 = im.reveal("reveal.txt")
