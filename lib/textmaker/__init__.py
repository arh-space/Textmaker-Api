from PIL import Image, ImageDraw, ImageFont

class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open("lib/textmaker/image.png"), ImageFont.truetype("lib/textmaker/fontnya.ttf",220),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 535:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=415
        for i in spliter[:40]:
            draw.text((70, int(line)), i, font=font, fill=("pink")) #selisih = Line
            line+=85 + 4.0
        self.output.append(img)
        if len(spliter) > 40:
            self.output+=tulis(spliter[40:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
