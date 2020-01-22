import tools.db as db , os, random
try:
    import V7xStyle
    from V7xStyle import Style,Text,Animation
    from V7xStyle import (R,G,W,P,C,B,Y,Bl,BL)
except ModuleNotFoundError:
    print ("\033[1;31m[!] Import error...\n[+] To fix error '\033[1;32mpip install V7xStyle\033[1;31m'")
    exit()

class app:
    def run(self):
        self.Introduction()
        user = int(input(Text('G#[W#*G#] Enter numder : W#')))
        self.StartApp(user)

    def Introduction(self):
        os.system('clear')
        Intro = str( Text(db.Intro) )
        Intro = Text(Intro).DeleteSpace
        title = Style('### Style {1.0} ###')
        title = title.Square(padding_x=12)
        tools = ['[G#1W#]C# Python','[G#2W#]C# Bash ']
        tools = Style(*tools)
        tools = tools.Square(Space=2,padding_x=5,Equal=False)
        end = Style('[G#99W#]C# Exit')
        end = end.Square(padding_x=17)
        text = Style(Intro,title,tools,end).Center
        Animation.SlowLine(text)

    def StyleText(self):
        color = self.RandColor()
        cols = int(input(Text('G#[W#*G#] cols : W#')))
        padding = int(input(Text('G#[W#*G#] padding : W#')))
        title = input(Text('G#[W#*G#] title : W#'))
        tools = input(Text('G#[W#*G#] tools : W#'))
        end = input(Text('G#[W#*G#] end : W#'))

        Intro = random.choice([color[3]+db.dragon.replace('8',color[3]+'8'+color[2]),W+db.skull])
        title = Style( str(Text(title)) )
        title = title.Square(Color=color[0])
        tools = [f'{color[3]}[{color[2]}{N+1}{color[3]}] {T}' for N,T in enumerate(str(Text(tools)).split(' '))]
        tools = Style(*tools).Square(Color=color[1],padding_x=padding,cols=cols)
        end = Style(end).Square(Color=color[0])
        text = Style(Intro,title,tools,end).Center
        return text

    def RandColor(self):
        color = []
        temp = 0
        while True:
            title = random.choice([R,G,W,P,C,B,Y,Bl])
            color += [title]
            tools = random.choice([R,G,W,P,C,B,Y,Bl])
            if tools in color:
                temp += 1
            color += [tools]
            toolsnum = random.choice([R,G,W,P,C,B,Y,Bl])
            if toolsnum in color:
                temp += 1
            color += [toolsnum]
            toolslist = random.choice([R,G,W,P,C,B,Y,Bl])
            if toolslist in color:
                temp += 1
            color += [toolslist]
            if temp == 0:
                break
            temp = 0
            color = []
        return color

    def StartApp(self,user):
        pyORba = {
        1:self.python,
        2:self.bash,
        99:exit,
        }
        pyORba[user]()

    def python(self):
        os.system('clear')
        Intro = str( Text(db.Intro) )
        Intro = Text(Intro).DeleteSpace
        title = Style('### Style {1.0} ###')
        title = title.Square(padding_x=12)
        end = Style('python ')
        end = end.Square(padding_x=18)
        text = Style(Intro,title,end).Center
        Animation.SlowLine(text)
        Style_Text = self.StyleText()
        file = input(Text('G#[W#*G#] file :W# '))
        print ('')
        Animation.Loading(text='G#[W#*G#]W# Loading ')
        print (Text(f'G#[W#*G#] Saved [C#SERVICES/{file}G#]'))
        Style_Text = Style_Text.replace('\\','\\\\')
        Style_Text = Style_Text.replace('\033[1;30m','\\033[1;30m')
        Style_Text = Style_Text.replace('\033[0;31m','\\033[0;31m')
        Style_Text = Style_Text.replace('\033[0;32m','\\033[0;32m')
        Style_Text = Style_Text.replace('\033[0;33m','\\033[0;33m')
        Style_Text = Style_Text.replace('\033[0;34m','\\033[0;34m')
        Style_Text = Style_Text.replace('\033[0;35m','\\033[0;35m')
        Style_Text = Style_Text.replace('\033[0;36m','\\033[0;36m')
        Style_Text = Style_Text.replace('\033[0;37m','\\033[0;37m')
        Style_Text = Style_Text.replace('\n','\\n')
        with open('SERVICES/'+file,'w') as f:
            f.write(f"#!/usr/bin/python\n# - * - coding: utf-8 - * -\ndef Style():\n\tfrom V7xStyle import Animation\n\ttext = '''{Style_Text}'''\n\tAnimation.SlowLine(text)\nStyle()")

    def bash(self):
        os.system('clear')
        Intro = str( Text(db.Intro) )
        Intro = Text(Intro).DeleteSpace
        title = Style('### Style {1.0} ###')
        title = title.Square(padding_x=12)
        end = Style(' bash  ')
        end = end.Square(padding_x=18)
        text = Style(Intro,title,end).Center
        Animation.SlowLine(text)
        Style_Text = self.StyleText()
        file = input(Text('G#[W#*G#] file :W# '))
        print ('')
        Animation.Loading(text='G#[W#*G#]W# Loading ')
        print (Text(f'G#[W#*G#] Saved [C#SERVICES/{file}G#]'))
        Style_Text = Style_Text.replace('\\','\\\\')
        Style_Text = Style_Text.replace('\033[1;30m','\\033[1;30m')
        Style_Text = Style_Text.replace('\033[0;31m','\\033[0;31m')
        Style_Text = Style_Text.replace('\033[0;32m','\\033[0;32m')
        Style_Text = Style_Text.replace('\033[0;33m','\\033[0;33m')
        Style_Text = Style_Text.replace('\033[0;34m','\\033[0;34m')
        Style_Text = Style_Text.replace('\033[0;35m','\\033[0;35m')
        Style_Text = Style_Text.replace('\033[0;36m','\\033[0;36m')
        Style_Text = Style_Text.replace('\033[0;37m','\\033[0;37m')
        Style_Text = Style_Text.replace('`','\\`')
        Style_Text = Style_Text.replace('"','\\"')
        with open('SERVICES/'+file,'w') as f:
            for i in Style_Text.split('\n'):
                f.write(f'echo -e "{i} "\nsleep 0.1\n')


if __name__ == '__main__':
    app = app()
    app.run()
