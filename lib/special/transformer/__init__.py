from PIL import Image, ImageDraw, ImageFont

class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open("lib/special/transformer/former.jpg"), ImageFont.truetype("lib/special/transformer/Transformers.ttf",280),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 1866:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=610
        for i in spliter[:86]:
            draw.text((210, int(line)), i, font=font, fill=("white")) #selisih = Line
            line+=450 + 4.0
        self.output.append(img)
        if len(spliter) > 86:
            self.output+=tulis(spliter[86:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
