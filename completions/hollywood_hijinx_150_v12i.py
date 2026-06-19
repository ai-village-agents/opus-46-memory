import subprocess, time, os, fcntl, re
GAME = "/tmp/hollywoodhijinx-r37-s861215.z3"
def make_nb(fd):
    fcntl.fcntl(fd, fcntl.F_SETFL, fcntl.fcntl(fd, fcntl.F_GETFL) | os.O_NONBLOCK)
class G:
    def __init__(self, seed=1):
        self.p = subprocess.Popen(['/usr/games/dfrotz','-p','-m','-s',str(seed),'-w','80','-h','200',GAME],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        make_nb(self.p.stdout.fileno()); time.sleep(0.5); self.rd(); self.turn = 0
    def rd(self, t=0.8):
        r=[]; dl=time.time()+t
        while time.time()<dl:
            try:
                c=os.read(self.p.stdout.fileno(),8192)
                if c: r.append(c)
                if c and b'>'in c: break
            except BlockingIOError: time.sleep(0.02)
            except: break
        return b''.join(r).decode('latin-1','replace')
    def s(self,cmd):
        self.turn+=1; self.p.stdin.write((cmd+'\n').encode()); self.p.stdin.flush()
        time.sleep(0.04); return self.rd()
    def v(self,cmd,quiet=False):
        o=self.s(cmd)
        if not quiet:
            ls=[l.strip() for l in o.split('\n') if l.strip() and l.strip()!='>']
            print(f"[T{self.turn:03d}] {cmd}",flush=True)
            for l in ls:
                if len(l)>2: print(f"  {l}",flush=True)
        return o
    def close(self):
        try: self.p.kill()
        except: pass

g = G(seed=1)

# ===== P1: SETUP =====
print("===== P1: SETUP =====")
for c in ["turn statue west","turn statue east","turn statue north","north",
           "open mailbox","get yellowed piece of paper","get business card",
           "open front door","north","get flashlight","turn on flashlight"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P2: GRATER + EXPLORE =====
print("===== P2: GRATER + EXPLORE =====")
for c in ["east","move painting","get green card",
           "turn dial right 3","turn dial left 7","turn dial right 5",
           "open safe","get cheese grater",
           "east","open piano","get violet card","west","west","west",
           "enter fireplace","remove brick","get indigo card","out",
           "get red statuette","get white statuette","get blue statuette",
           "north","get thin paper","west","get matchbox","east","east",
           "unlock patio door","open patio door","east","east","get yellow card",
           "south","get film strip","get slide","north","west","west","south"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P3: FINCH + UPSTAIRS =====
print("===== P3: FINCH + UPSTAIRS =====")
for c in ["open closet door","enter closet","pull third peg","open closet door",
           "north","turn newel","east","get sack","open window","open sack",
           "get finch","west","west","south","move bath mat","get red card",
           "north","east","south","pull second peg","open closet door","north"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P4: PENGUIN =====
print("===== P4: PENGUIN =====")
for c in ["drop all","get flashlight","west","enter fireplace",
           "up","up","up","east","down","get penguin",
           "up","west","down","down","down","out","east"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P5: MASK =====
print("===== P5: MASK =====")
for c in ["get matchbox","open closet door","enter closet","get bucket",
           "open closet door","north","north","north","get orange card",
           "north","northwest","get shovel","southeast","south","east",
           "north","north","get cannon ball","put ball in cannon",
           "open matchbox","get red match","light red match","light fuse",
           "open compartment","get catcher's mask",
           "east","south","west"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P6: FIRE HYDRANT =====
print("===== P6: FIRE HYDRANT =====")
for c in ["north","northeast","northwest","fill bucket","southeast","southwest",
           "south","south","south","open closet door","enter closet","get skis",
           "hang bucket on third peg","open closet door","north","up",
           "open closet door","south"]:
    g.v(c, quiet=True)
for i in range(15):
    g.v("wait", quiet=True)
for c in ["open closet door","north","open panel","open trunk",
           "get fire hydrant","down","down"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P7: TOUPEE =====
print("===== P7: TOUPEE =====")
for c in ["drop all","get flashlight",
           "get red card","get yellow card","get green card","get indigo card",
           "get violet card","get orange card",
           "west","north","west","down","open closet door","south","get blue card",
           "north","turn on computer",
           "put red card in slot","put orange card in slot","put yellow card in slot",
           "put green card in slot","put blue card in slot","put indigo card in slot",
           "put violet card in slot","up","east","south",
           "call 576-3190","north","west","down","get toupee",
           "up","east","east","south"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P8: RING =====
print("===== P8: RING =====")
for c in ["north",
           "push green","push green","push green",
           "push black","push black","push white","push white",
           "push green","push green","push green",
           "push blue","push black",
           "push green","push green","push green",
           "push red","push red","push red",
           "reach in hole"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P9: PROJECTOR + PARKING METER =====
print("===== P9: PROJECTOR + PARKING METER =====")
for c in ["south",
           "get film strip","get slide","get red statuette",
           "north","east","east","south",
           "put slide in slide projector","turn on slide projector",
           "focus slide projector lens",
           "put film strip in film projector","take lens cap",
           "turn on film projector","look at screen",
           "north","west","west","south",
           "drop cheese grater","drop finch","drop penguin","drop catcher's mask",
           "drop fire hydrant","drop toupee","drop lens cap","drop ring",
           "east","east","play Yesterday",
           "push piano north","down","south","get dirty pillar","north","up",
           "push piano south","push piano south","down","north",
           "get parking meter","south","up","west","west"]:
    g.v(c, quiet=True)
g.v("score")

# ===== P10: RUBBER STAMP (MAZE) =====
print("===== P10: RUBBER STAMP =====")
for c in ["get yellowed piece of paper","get thin paper","get shovel",
           "put yellowed piece of paper on thin paper",
           "north","north","north","northwest","northeast","north","north"]:
    g.v(c, quiet=True)

maze_in = "west,north,west,north,west,south,west,west,north,west,south,east,south,east,north,east,south,west,north,west,south,west,north,west,south,west,north,east,north,east,north,east,east,north,east,south,east,east,south,east,north,east,north,east,south,west,south,west,south,east,north,west,south".split(",")
for c in maze_in:
    g.v(c, quiet=True)
g.v("dig in ground", quiet=True)
g.v("get rubber stamp", quiet=True)

# FIXED: Correct maze exit path (reverse of maze_in with directions swapped)
maze_out = "north,east,south,west,north,east,north,east,north,west,south,west,south,west,north,west,west,north,west,south,west,west,south,west,south,west,south,east,north,east,south,east,north,east,south,east,north,west,south,west,north,west,north,east,south,east,east,north,east,south,east,south,east".split(",")
for c in ["north"]:  # Exit heart of maze
    g.v(c, quiet=True)
for c in maze_out:
    g.v(c, quiet=True)
# Now should be at entrance position - go south to exit
g.v("south", quiet=True)
o = g.v("look")
# Navigate back to foyer
for c in ["south","southeast","southwest","south","south","south"]:
    g.v(c, quiet=True)
o = g.v("look")
g.v("score")

# ===== P11: CORPSE LINE =====
print("===== P11: CORPSE LINE =====")
for c in ["drop all","get flashlight","get red statuette","get matchbox","get skis",
           "north","north","east","north","east","wear skis","down",
           "get green match","remove skis","drop skis",
           "light red statuette","pour wax on green match","blow out red statuette",
           "swim","south","down","down","west","up","up","north","north",
           "up","light green match","light red statuette with green match",
           "pull chain","push down right end","burn rope","stand on right end","wait",
           "drop flashlight","drop matchbox","get ladder","down",
           "hang ladder on hooks",
           "turn dial left 4","turn dial right 5","turn dial left 7","open safe"]:
    g.v(c, quiet=True)

o = g.v("get corpse line")
g.v("score")
o2 = g.v("get chipped peg")
o3 = g.v("get note")

# Navigate out of shelter to foyer
for c in ["up","south","east","south","west","south","south"]:
    g.v(c, quiet=True)
o = g.v("look")

# ===== P12: VAULT + WIN =====
print("===== P12: VAULT + WIN =====")
for c in ["up","open closet door","south"]:
    g.v(c, quiet=True)
o = g.v("put chipped peg in hole")
for c in ["get club"]:
    g.v(c, quiet=True)
o = g.v("kill herman")
g.v("get stick", quiet=True)
o = g.v("kill herman")
g.v("get gun", quiet=True)
o = g.v("kill herman")
o = g.v("turn off saw")
g.v("score")

g.close()
print("\n===== GAME COMPLETE =====")
