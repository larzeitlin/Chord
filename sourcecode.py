add_library('themidibus')
position = "C"

a = 0.0
w = 1000
m = "major"
lc = ""
rn = ""
sustain = 50
mode = 0
note = 0
notelist = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
CorS = "C"
sevenths = "off"



def setup():
    
    size(700, 700)
    frameRate(30)
    pixelDensity(displayDensity())
    background(0)
    global myBus
    myBus = MidiBus(this, -1, "Bus 1")
    
    mainConstruct()
        
    pushStyle()
    textAlign(LEFT)
    text("[M] Major/Minor", w/20, w/12)
    text("[UP/DOWN] Sustain: " + str(sustain), w/20, w/15)
    text("[X] Sevenths: " + str(sevenths), w/20, w/20)
    text("[Z] Chords/Scales: " + str(CorS), w/20, w/30)
    popStyle()
    
     
def draw():
    sectors() 
    
def mainConstruct():
    
    for l in range(12):
        rad = l*30
        lineBig(rad)
    for l in range(12):
        rad = l*30
        lineSmall(rad)                          # N.B. These can't all go in one loop becase they are drawn to the screen in layers
    for l in range(12):
        rad = l*30
        circlesbig(rad)
    for l in range(12):
        rad = l*30
        circlessmall(rad)
    for l in range(12):
       rad = l*30
       keystext(rad)
    for l in range(12):
        rad = l*30
        chprog(rad)
    pushStyle()
    textAlign(CENTER, CENTER)
    textSize(12)
    text("Use numbers 1 to 7 on the computer keyboard to trigger chords and notes", width/2, height/1.03)
    popStyle()
    

def circlesbig(r):
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(r))
    stroke(225)
    noFill()
    ellipseMode(CENTER)
    ellipse(w/5, 0, w/5, w/5)
    popMatrix()

def circlessmall(r):
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(r))
    stroke(225)
    fill(0)
    ellipseMode(CENTER)
    ellipse((w/10)*3, 0, w/50, w/50)
    ellipse((w/10), 0, w/50, w/50)
    ellipse(w/5, w/10, w/50, w/50)
    ellipse(w/5, w/-10, w/50, w/50)
    sr = w/10
    adj = (sr/2)*sqrt(3)
    p = sr + (sr - adj)
    ellipse(p, sr/2, w/50, w/50)
    ellipse(p, sr/-2, w/50, w/50)
    popMatrix()

def lineBig(r):
    pushMatrix()
    translate(width/2, height/2)

    rotate(radians(r))
    ang = 120
    rbig = (w/10)*3
    stroke(225)
    line(rbig, 0, cos(radians(ang))*rbig, sin(radians(ang))*rbig)
    popMatrix()
    
def lineSmall(r):
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(r))
    stroke(225)
    line(0, w/10, w/-10, 0)
    popMatrix()
    
def keystext(r):
   keyname = dict()
   keyname['0'] = 'C'
   keyname['30'] = 'G'
   keyname['60'] = 'D'
   keyname['90'] = 'A'
   keyname['120'] = 'E'
   keyname['150'] = 'B'
   keyname['180'] = 'F#'
   keyname['210'] = 'Db'
   keyname['240'] = 'Ab'
   keyname['270'] = 'Eb'
   keyname['300'] = 'Bb'
   keyname['330'] = 'F'
   textforkey = keyname[str(r)]

   #major fifths
   pushMatrix()
   translate(width/2, height/2)
   rotate(radians(r))
   fill(225)
   textAlign(CENTER)
   textSize(w/50)
   text(textforkey, 0, w/-4)
   popMatrix()
    
   #Minor fifths
   pushMatrix()
   translate(width/2, height/2)
   rotate(radians(r - 90))
   fill(225)
   textAlign(CENTER)
   textSize(w/100)
   text(textforkey, 0, w/-12.5)
   popMatrix() 

def chprog(r):
    alignbump = width/-300
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(r))
    textAlign(CENTER, CENTER)
    textSize(w/100)
    text("I", 0, ((w/10)*-3) + alignbump)
    text("VI", 0,  (w/-10) + alignbump)
    text("IV", w/-10, (w/-5) + alignbump)
    text("V", w/10, (w/-5) + alignbump)
    sr = w/10
    adj = (sr/2)*sqrt(3)
    p = sr + (sr - adj)
    text("III", sr/2, (0 - p) + alignbump)
    text("II", sr/-2, (0 - p) + alignbump)
    popMatrix()
    

def colourcircles(rot1, g, h, j): 
    global a
    pushMatrix()
    translate(width/2, height/2)
    ellipseMode(CENTER)
    rotate(radians(rot1))
    stroke(g, h, j)
    a = a + 0.08
    strokeWeight(3)
    noFill()
    ellipse(0, w/-5, w/5, w/5)
    
    popMatrix()
    strokeWeight(1)
    noTint()
    
def highlights(key1, position):    
    notelist = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    chordroot_dict = {1:0, 2:2, 3:4, 4:5, 5:7, 6:9, 7:11}
    rot = (((int(notelist.index(position)) + int(chordroot_dict[key1]))* 7 )%12)*30
    if m == "major":
        if key1 == 1 or key1 == 4 or key1 == 5:
            colourcircles(rot + 120, 0, 225, 0)
            colourcircles(rot + 30, 0, 225, 160)
            colourcircles(rot, 0, 185, 225)
        elif key1 == 2 or key1 == 3 or key1 == 6:
            colourcircles(rot - 90, 0, 44, 225)
            colourcircles(rot + 30, 0, 225, 160)
            colourcircles(rot, 0, 185, 225)
        elif key1 == 7:
            colourcircles(rot - 90, 0, 44, 225)
            colourcircles(rot + 180, 0, 225, 160)
            colourcircles(rot, 0, 185, 225)
    elif m == "minor":
        if key1 == 1 or key1 == 4 or key1 == 5:
            colourcircles(rot - 90, 0, 44, 225)
            colourcircles(rot + 30, 0, 225, 160)
            colourcircles(rot, 0, 185, 225)
            
        elif key1 == 7 or key1 == 3 or key1 == 6:
            colourcircles(rot - 90, 0, 225, 0)
            colourcircles(rot + 180, 0, 225, 160)
            colourcircles(rot + 150, 0, 185, 225)
            
            
        elif key1 == 2:
            colourcircles(rot - 90, 0, 44, 225)
            colourcircles(rot + 180, 0, 225, 160)
            colourcircles(rot, 0, 185, 225)           
    
    
    small_C_highlights((((notelist.index(position)*7)-3)%12)*30, key1)
    
def scaleHighlights(key1, position):    
    notelist = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    chordroot_dict = {1:0, 2:2, 3:4, 4:5, 5:7, 6:9, 7:11}
    rot = (((int(notelist.index((position)) + mode) + int(chordroot_dict[key1]))* 7 )%12)*30
    if m == "major":
        colourcircles(rot, 0, 185, 225)
    elif m == "minor":
        colourcircles(rot + 30, 0, 185, 225) 
     
def small_C_highlights(r, chord):
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(r))
    stroke(0, 225, 225)
    strokeWeight(4)
    ellipseMode(CENTER)
    sr = w/10
    adj = (sr/2)*sqrt(3)
    p = sr + (sr - adj)
    def c7():
        pushMatrix()
        translate(w/3, 0)
        rotate(radians(90))
        textSize(10)
        text("VII",0, 0)
        strokeWeight(2)
        ellipse(0, 0, w/50, w/50)
        popMatrix()
    def c6():
        ellipse((w/10), 0, w/50, w/50)
    def c5():
        ellipse(w/5, w/10, w/50, w/50)
    def c4():
        ellipse(w/5, w/-10, w/50, w/50)
    def c3():
        ellipse(p, sr/2, w/50, w/50)
    def c2():
        ellipse(p, sr/-2, w/50, w/50)
    def c1():
        ellipse((w/10)*3, 0, w/50, w/50)
        
        
    chordarray = []
    chordarray.append([2, 1, 1, 1, 1, 1, 1])
    chordarray.append([0, 2, 0, 0, 1, 0, 1])
    chordarray.append([0, 0, 2, 1, 0, 1, 0])
    chordarray.append([1, 1, 0, 2, 1, 0, 1])
    chordarray.append([1, 0, 0, 0, 2, 1, 0])
    chordarray.append([0, 1, 0, 1, 1, 2, 0])
    chordarray.append([1, 0, 0, 0, 1, 0, 2])
    

    sugchords = (chordarray[chord - 1])
    for num in range(7):
        if sugchords[num] == 1:
            stroke(0, 225, 0)
            cons = "c" + str(int(num+1)) + "()"
            eval(cons)
        elif sugchords[num] == 2:
            stroke(225)
            cons = "c" + str(int(num+1)) + "()"
            eval(cons)
        
    popMatrix()
    strokeWeight(1)
    
def modeGen(a, b):
    modeArray = []
    modeArray.append([3, 5, 7, 8, 10, 12, 14, 15])
    modeArray.append([5, 7, 8, 10, 12, 14, 15, 17])
    modeArray.append([7, 8, 10, 12, 14, 15, 17, 19])
    modeArray.append([8, 10, 12, 14, 15, 17, 19, 20])
    modeArray.append([10, 12, 14, 15, 17, 19, 20, 222 ])
    modeArray.append([0, 2, 3, 5, 7, 8, 10, 12])
    modeArray.append([2, 3, 5, 7, 8, 10, 12, 14])
    return modeArray[a][b]

def modeName(modeNum):
    modeSelector = ["Ionian", " Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locryan"]
    return modeSelector[modeNum]
def keyPressed():
    background(0)
    
    global m
    global sustain
    global mode
    global note
    global position
    global notelist
    global CorS
    global sevenths
    channel = 0
    velocity = 127
    if CorS == "C":
        try:
            key1 = int(key)
            if type(key1) == int and key1 <= 7:
                
                chord_const(key1, position)
                highlights(key1, position)
            
                    
        except:
            pass
        
        try:
            if key == "m":
                if m == "major":
                    m = "minor"
                    mode = 5
                else:
                    m = "major"
                    mode = 0
                    
        except:
            pass
        
        try:
            if key == "x":
                if sevenths == "on":
                    sevenths = "off"
                else:
                    sevenths = "on"

                    
        except:
            pass
        
        try:
            if key == CODED:
                if keyCode == UP:
                    sustain = sustain + 50
                elif keyCode == DOWN:
                    if sustain > 0:
                        sustain = sustain - 50
                        
            
        except:
            pass
        
        try:
            if key == "z":
                    CorS = "S"
        except:
            pass
    
                    
        
        mainConstruct()
    
        pushStyle()
        textAlign(LEFT)
        text("[M] Major/Minor", w/20, w/12)
        text("[UP/DOWN] Sustain: " + str(sustain), w/20, w/15)
        text("[X] Sevenths: " + str(sevenths), w/20, w/20)
        text("[Z] Chords/Scales: " + str(CorS), w/20, w/30)
        popStyle()
    
        
        
    elif CorS == "S":
        
        try:
            key1 = int(key)
            if type(key1) == int and key1 <= 8:
                if m == "major":
                    note = modeGen(mode, key1 - 1) + notelist.index(position) + 45
                    myBus.sendNoteOn(channel, note, velocity)
                    delay(sustain)
                    myBus.sendNoteOff(channel, note, velocity)
                    scaleHighlights(key1, position)
                elif m == "minor":
                    note = modeGen(mode, key1 - 1) + notelist.index(position) + 48
                    myBus.sendNoteOn(channel, note, velocity)
                    delay(sustain)
                    myBus.sendNoteOff(channel, note, velocity)
                    scaleHighlights(key1, position)
                    
        
            
        except:
            pass
            
        
        try:
            if key == CODED:
                if keyCode == UP:
                    sustain = sustain + 50
                elif keyCode == DOWN:
                    if sustain > 0:
                        sustain = sustain - 50
                elif keyCode == RIGHT:
                    mode = (mode + 1)%7
                elif keyCode == LEFT:
                    mode = (mode - 1)%7
        except:
            pass
            
        try:
            if key == "z":
                    CorS = "C"
        except:
            pass
        
        try:
            if key == "m":
                if m == "major":
                    m = "minor"
                    mode = 5
                else:
                    m = "major"
                    mode = 0
                    
        except:
            pass
                    
        
        mainConstruct()
    
        pushStyle()
        textAlign(LEFT)
        text("[M] Major/Minor", w/20, w/12)
        text("[UP/DOWN] Sustain: " + str(sustain), w/20, w/15)
        text("[LEFT/RIGHT] Mode Switch", w/20, w/20)
        text("[Z] Chords/Scales: " + str(CorS), w/20, w/30)
        pushStyle()
    

        

def sectors():
    global position
    global CorS
    global mode
    # background(0)
    ellipseMode(CENTER)
    fill(0)
    noStroke()
    ellipse(width/2, height/2, w/10, w/10)
    
    x = (mouseX - (width / 2))
    y = 0 - (mouseY - (height / 2))
    
    if (((float(x))**2.0) + ((float(y))**2.0)) > ((float(w) / 3)**2.0):
            position = "C"
    else:
        if y > 0:
            if x > 0:
                if y > x:
                    if y > 4*x:
                        position = "C"
                    else:
                        position = "G"
                else:
                    if y > x/4:
                        position = "D"
                    else:
                        position =  "A"
            else:
                if y > -x:
                    if y/4 > -x:
                        position = "C"
                    else:
                        position = "F"
                else:
                    if y*4 > -x:
                        position = "Bb"
                    else:
                        position =  "Eb"
        else:
            if x > 0:
                if -y > x:
                    if -y > 4*x:
                        position = "F#"
                    else:
                        position = "B"
                else:
                    if -y > x/4:
                        position = "E"
                    else:
                        position =  "A"
            else:
                if -y > -x:
                    if -y > -x*4:
                        position = "F#"
                    else:
                        position = "Db"
                else:
                    if -y < -x/4:
                        position = "Eb"
                    else:
                        position =  "Ab"
   ## indicators
   
    if CorS == "C":
        textAlign(CENTER, CENTER) 
        fill(225)
        textSize(w/20)
        text(position, width/2, height/2 - w/120)
        textSize(w/50)
        text(m, width/2, height/2 + w/30)
        textSize(w/70)
        text(lc, width/2, height/2 - w/25)
        textSize(w/70)
    elif CorS == "S":
        textAlign(CENTER, CENTER)
        fill(225)
        textSize(w/20)
        text(position, width/2, height/2 - w/120)
        textSize(w/50)
        text(m, width/2, height/2 + w/30)
        textSize(w/80)
        text(modeName(mode), width/2, height/2 - w/25)
        textSize(w/70)
        
 

def chord_const(chord, key1):
    global lc
    global rn
    global sustain
    
 
    
    notelist = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    if m == "major":
    
        chordroot_dict = {1:0, 2:2, 3:4, 4:5, 5:7, 6:9, 7:11}
    
    elif m == "minor":
        
        chordroot_dict = {1:0, 2:2, 3:3, 4:5, 5:7, 6:8, 7:10}
        
        
    chordrootnumb = int(notelist.index(key1)) + int(chordroot_dict[chord])
    chordroot = notelist[chordrootnumb % 12]
    channel = 0
    root = chordrootnumb + 48
    velocity = 127
    maj3rd = root + 4
    min3rd = root + 3
    fifth = root + 7
    dimfifth = root + 6
    maj7th = root + 11
    min7th = root + 10
    
    if sevenths == "on":
        if m == "major":
        
            if chord== 1 or chord == 4:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                myBus.sendNoteOn(channel, maj7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                myBus.sendNoteOff(channel, maj7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
            
            
        
            elif chord == 2 or chord == 3 or chord == 6:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " min"
                
            if chord== 5:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
            
                
                
            elif chord == 7:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, dimfifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, dimfifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " dim"
            
                
        elif m == "minor":
            if chord== 1 or chord== 4 or chord== 5:
                
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " min"
            
                
        
            elif chord== 3 or chord== 6:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                myBus.sendNoteOn(channel, maj7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                myBus.sendNoteOff(channel, maj7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
                
            elif chord== 7:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
            
                
                
            elif chord == 2:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, dimfifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                myBus.sendNoteOn(channel, min7th, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, dimfifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                myBus.sendNoteOff(channel, min7th, velocity)
                lc = str(notelist[chordrootnumb%12]) + " dim"
                
    elif sevenths == "off":
          
          
        if m == "major":
        
            if chord== 1 or chord== 4 or chord== 5:
                
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
            elif chord== 2 or chord== 3 or chord== 6:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " min"    
            elif chord == 7:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, dimfifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, dimfifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " dim"
            
                
        elif m == "minor":
            if chord== 1 or chord== 4 or chord== 5:
                
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " min"
            
                
        
            elif chord== 7 or chord== 3 or chord== 6:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, fifth, velocity)
                myBus.sendNoteOn(channel, maj3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, fifth, velocity)
                myBus.sendNoteOff(channel, maj3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " maj"
            
                
                
            elif chord == 2:
                myBus.sendNoteOn(channel, root, velocity)
                myBus.sendNoteOn(channel, dimfifth, velocity)
                myBus.sendNoteOn(channel, min3rd, velocity)
                delay(sustain)
                myBus.sendNoteOff(channel, root, velocity)
                myBus.sendNoteOff(channel, dimfifth, velocity)
                myBus.sendNoteOff(channel, min3rd, velocity)
                lc = str(notelist[chordrootnumb%12]) + " dim"
             
    
