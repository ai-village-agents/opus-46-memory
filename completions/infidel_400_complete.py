import subprocess, time, os, fcntl

def make_nb(fd):
    fcntl.fcntl(fd, fcntl.F_SETFL, fcntl.fcntl(fd, fcntl.F_GETFL) | os.O_NONBLOCK)

class G:
    def __init__(self, gf, seed=1):
        self.p = subprocess.Popen(['/usr/games/dfrotz','-p','-m','-s',str(seed),'-w','80','-h','200',gf],
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

g = G('/tmp/infidel-r22-s830916.z3')

# === FULL VERIFIED SETUP TO 245/400 (all quiet) ===
setup = ['STAND','S','SW','W','GET ALL','E','SE',
    'WAIT','WAIT','WAIT','WAIT','WAIT','WAIT',
    'OPEN CRATE','GET BOX','S','GET ALL','DROP NOTE',
    'N','N','GET MATCHBOOK','N','N','BREAK LOCK WITH AXE','GET LOCK','DROP LOCK',
    'OPEN TRUNK','GET BEEF AND MAP','UNFOLD MAP','GET CUBE',
    'S','W','W','DRINK WATER','DRINK WATER',
    'DROP SACK','GET CANTEEN','OPEN CANTEEN','FILL CANTEEN','CLOSE CANTEEN',
    'PUT CANTEEN IN SACK','PUT MATCHBOOK IN SACK','PUT NAVIGATION BOX IN SACK',
    'GET SACK','E','SE','SE','E','E',
    'DIG IN SAND','DIG IN SAND','DIG IN SAND','DIG IN SAND','DIG IN SAND',
    'DROP SHOVEL','PUT CUBE IN OPENING',
    'DOWN','GET ALL',
    'OPEN JAR','WET TORCH WITH LIQUID',
    'DROP SACK','GET MATCHBOOK','OPEN MATCHBOOK','GET A MATCH',
    'LIGHT IT','LIGHT TORCH','DROP MATCH',
    'PUT MATCHBOOK IN SACK','PUT JAR IN SACK','GET SACK',
    'S','S','NE','NW','N',
    'DROP SACK','EAT BEEF','GET CANTEEN','OPEN CANTEEN',
    'DRINK WATER','CLOSE CANTEEN','PUT CANTEEN IN SACK','PUT MAP IN SACK','GET SACK',
    'W','GET SCROLL','DROP SACK','PUT SCROLL IN SACK','GET SACK','E',
    'E','DOWN','W','GET SHIM','DROP SHIM','E','UP','W',
    'GET BEAM','S','E','N','W',
    'N','N','N','N','N',
    'E','S','GET SILVER','N','W','W','S','GET GOLD',
    'N','E','S','S','S','S','S','E','S','W','SE','SW','N','N',
    # Circular room
    'DROP SACK','PUT SILVER IN SACK','PUT GOLD IN SACK',
    'TIE ROPE TO ALTAR','THROW ROPE NORTH','GET SACK','CLIMB DOWN ROPE',
    'DROP SACK','GET CLUSTER','PUT CLUSTER IN SACK',
    'PUSH STATUE','GET HEAD',
    'PUSH STATUE NW','DROP HEAD','SE','SE','SE','GET OPAL',
    'NW','NW','NW','GET HEAD',
    'PUSH STATUE SE','PUSH STATUE SE','DROP HEAD',
    'NW','NW','NW','GET DIAMOND','SE','SE','SE',
    'GET HEAD','PUSH STATUE NW','PUSH STATUE NE','DROP HEAD',
    'SW','SW','SW','GET EMERALD','NE','NE',
    'PUT ALL CLUSTER IN SACK',
    'NE','GET HEAD','PUSH STATUE SW','PUSH STATUE SW','DROP HEAD',
    'NE','NE','NE','GET RUBY','SW','SW',
    'GET SACK','CLIMB ROPE']
for c in setup: g.v(c, quiet=True)

print("=== CHAMBER OF RA - ENDGAME ===")
g.v('SCORE')

# Re-wet torch and prepare
g.v('DROP SACK')
g.v('PUT RUBY IN SACK')
g.v('WET TORCH WITH LIQUID')
g.v('GET SACK')

# Navigate cubes: W, E, S
print("\n=== CUBE NAVIGATION ===")
g.v('W')
g.v('LOOK')
g.v('E')
g.v('LOOK')
g.v('S')
g.v('LOOK')

# Read scroll and bricks
print("\n=== SCROLL & BRICKS ===")
g.v('DROP SACK')
g.v('GET SCROLL')
g.v('READ SCROLL')
g.v('DROP SCROLL')
g.v('LOOK')

# Get bricks (1st, 3rd, 5th)
g.v('GET FIRST BRICK')
g.v('DROP IT')
g.v('GET THIRD BRICK')
g.v('DROP IT')
g.v('GET FIFTH BRICK')
g.v('DROP IT')
g.v('GET SACK')
g.v('SCORE')

# Navigate to passage
print("\n=== TO PASSAGE ===")
g.v('E')
g.v('LOOK')
g.v('N')
g.v('LOOK')
g.v('W')
g.v('LOOK')

# Chop plaster
print("\n=== CHOP PLASTER ===")
g.v('CHOP PLASTER WITH AXE')
g.v('SCORE')

# Navigate west to niches
g.v('W')
g.v('LOOK')
g.v('W')
g.v('LOOK')
g.v('W')
g.v('LOOK')

# Beam across niches
print("\n=== BEAM ACROSS NICHES ===")
g.v('PUT BEAM ACROSS NICHES')
g.v('STAND ON BEAM')
g.v('CHOP PLASTER WITH AXE')
g.v('OPEN DOOR')
g.v('SCORE')

# Antechamber
print("\n=== ANTECHAMBER ===")
g.v('W')
g.v('LOOK')
g.v('GET BEAM')
g.v('S')
g.v('LOOK')
g.v('PUT BEAM IN DOORWAY')
g.v('OPEN DOOR')

# Annex - jewels
print("\n=== ANNEX ===")
g.v('W')
g.v('LOOK')
g.v('DROP SACK')
g.v('PUT DIAMOND IN FIRST HOLE')
g.v('PUT RUBY IN SECOND HOLE')
g.v('PUT EMERALD IN THIRD HOLE')
g.v('PUT OPAL IN FOURTH HOLE')
g.v('LIFT SLAB')
g.v('GET BOOK')
g.v('GET SACK')
g.v('SCORE')

# Back out, beam under lintel
print("\n=== BURIAL CHAMBER ===")
g.v('E')
g.v('GET BEAM')
g.v('N')
g.v('N')
g.v('PUT BEAM UNDER LINTEL')
g.v('CHOP SEAL WITH AXE')
g.v('OPEN DOOR')
g.v('N')
g.v('LOOK')

# Treasury
print("\n=== TREASURY ===")
g.v('E')
g.v('LOOK')
g.v('DROP SACK')
g.v('GET GOLDEN CHALICE')
g.v('GET SILVER CHALICE')
g.v('GET CANTEEN')
g.v('OPEN CANTEEN')
g.v('POUR WATER INTO SILVER CHALICE')
g.v('PUT SILVER CHALICE ON RIGHT')
g.v('PUT GOLDEN CHALICE ON LEFT')
g.v('GET SCARAB')
g.v('SCORE')

# Final - burial chamber
print("\n=== FINAL SEQUENCE ===")
g.v('W')
g.v('PUT SCARAB ON SMALL RECESS')
g.v('PUT BOOK ON LARGE RECESS')
g.v('TURN NEITH')
g.v('TURN SELKIS')
g.v('TURN ISIS')
g.v('TURN NEPHTHYS')
g.v('OPEN COVER')
g.v('SCORE')

g.close()
