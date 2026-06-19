import pty, os, time, select

master, slave = pty.openpty()
pid = os.fork()
if pid == 0:
    os.close(master)
    os.dup2(slave, 0); os.dup2(slave, 1); os.dup2(slave, 2)
    os.close(slave)
    os.execv('/usr/games/adventure', ['adventure'])
else:
    os.close(slave)
    turn = 0
    axe_held = False
    
    def rd(t=0.5):
        r = []; dl = time.time() + t
        while time.time() < dl:
            rl, _, _ = select.select([master], [], [], 0.05)
            if rl:
                try:
                    c = os.read(master, 8192)
                    if c: r.append(c)
                except: break
        return b''.join(r).decode('latin-1','replace')
    
    def raw_cmd(c):
        global turn
        turn += 1
        os.write(master, (c + '\n').encode())
        time.sleep(0.08)
        return rd(0.3)
    
    def cmd(c, quiet=False):
        global turn, axe_held
        o = raw_cmd(c)
        ol = o.lower()
        
        if not quiet:
            lines = [l.strip() for l in o.split('\n') if l.strip() and l.strip() != c]
            print(f"[{turn:03d}] {c}", flush=True)
            for l in lines:
                if len(l) > 2: print(f"  {l}", flush=True)
        
        # Handle prompts
        if 'help getting out' in ol:
            raw_cmd("no")
        if 'wish to quit' in ol:
            raw_cmd("no")
        if 'reincarnate' in ol:
            raw_cmd("yes")
        
        # Handle dwarf
        if 'threw a little' in ol and 'axe' in ol and not axe_held:
            raw_cmd("take axe"); axe_held = True
        if 'threatening little dwarf' in ol and axe_held:
            raw_cmd("throw axe"); raw_cmd("take axe")
        if 'knife blocks' in ol and axe_held:
            raw_cmd("throw axe"); raw_cmd("take axe")
            
        return o

    rd(1.0); cmd("no")

    # === Replay entire game up to score 276 ===
    # Phase 1-3: Items, bird, first treasures, drop at building
    for c in ["building","take lamp","on lamp","xyzzy",
              "e","take cage","pit","e","take bird","w","d",
              "s","take gold","n","n","free bird","drop cage",
              "s","take jewel","n","w","take coins","e",
              "n","take silve","n","plover","ne","take plati","s","plover",
              "plugh","drop plati","drop coins","drop jewel","drop silve","drop gold",
              "take bottl","take food","take keys"]:
        cmd(c, quiet=True)
    print(f"Phase 1-3 done, turn {turn}", flush=True)
    
    # Phase 4: Plant, oil, eggs, trident
    for c in ["plugh","s","d","bedquilt","slab","s","d","water plant",
              "u","w","u","reservoir","fill bottl","s","s","d","s","d","water plant",
              "u","e","d","fill bottl","u","w","d","climb plant","w",
              "take eggs","n","oil door","drop bottl","n","take tride"]:
        cmd(c, quiet=True)
    print(f"Phase 4 done, turn {turn}", flush=True)
    
    # Phase 5: Troll, bear, chain, spices
    for c in ["w","d","sw","u","toss eggs","cross","ne","barren","e",
              "feed bear","open chain","drop keys","take chain","take bear",
              "w","fork","ne","e","take spice","fork","w","w",
              "cross","free bear","cross"]:
        cmd(c, quiet=True)
    print(f"Phase 5 done, turn {turn}", flush=True)
    
    # Phase 6-7: Pearl, drop treasures
    for c in ["sw","d","bedquilt","e","n","open clam","d","d","take pearl","u","u",
              "s","u","e","u","n","plugh",
              "drop chain","drop spice","drop tride","drop pearl"]:
        cmd(c, quiet=True)
    print(f"Phase 6-7 done, turn {turn}", flush=True)
    
    # Phase 8: Emerald, vase, pillow
    for c in ["plugh","s","d","bedquilt","w","oriental","n","w",
              "drop lamp"]:
        cmd(c, quiet=True)
    if axe_held:
        cmd("drop axe", quiet=True)
    for c in ["e","take emera","w"]:
        cmd(c, quiet=True)
    if axe_held:
        cmd("take axe", quiet=True)
    for c in ["take lamp","nw","s","take vase","se","e","take pillo","w"]:
        cmd(c, quiet=True)
    print(f"Phase 8 done, turn {turn}", flush=True)
    
    # Phase 9: Eggs, dragon, rug
    for c in ["w","w","d","climb plant","w","fee","fie","foe","foo",
              "take eggs","s","d","u","w","u","s","kill dragon","yes",
              "take rug","e","e","n","n"]:
        cmd(c, quiet=True)
    print(f"Phase 9 done, turn {turn}", flush=True)
    
    # Phase 10: Drop treasures
    for c in ["plugh","drop rug","drop pillo","drop vase","drop emera","drop eggs"]:
        cmd(c, quiet=True)
    cmd("score")
    
    # Phase 11: Diamonds + pirate
    for c in ["xyzzy","take wand","pit","d","w","wave wand","w","take diamo",
              "w","s","e","s","s","s","n","e","n","e","nw"]:
        cmd(c, quiet=True)
    
    o = cmd("take chest")
    if 'see no' in o.lower():
        for attempt in range(8):
            for mc in ["se","n","w","w","w","e","e","w","s","n","s","s","s","n","e","n","e","nw"]:
                o = cmd(mc, quiet=True)
                if 'pirate' in o.lower():
                    print(f"  ** PIRATE on attempt {attempt+1}! **", flush=True)
            o = cmd("take chest")
            if 'see no' not in o.lower(): break
    
    cmd("take diamo")
    for c in ["se","n","d","debris","xyzzy","drop wand","drop chest","drop diamo"]:
        cmd(c, quiet=True)
    cmd("score")
    
    # Phase 12: Magazine
    for c in ["plugh","s","d","bedquilt","e","e","take magaz","e","drop magaz"]:
        cmd(c, quiet=True)
    cmd("score")
    
    # === ENDGAME: Escape Witt's End, wait for cave closing ===
    print("\n=== ENDGAME: Escaping Witt's End ===", flush=True)
    
    # Try to escape - the exit is random
    escaped = False
    for i in range(50):
        o = raw_cmd("n")
        ol = o.lower()
        # Handle blocking prompts
        if 'help getting out' in ol:
            raw_cmd("no")
            continue
        if 'wish to quit' in ol:
            raw_cmd("no")
            continue
        if "witt" not in ol and "dead end" not in ol and len(o.strip()) > 5:
            print(f"  Escaped Witt's End after {i+1} tries!", flush=True)
            print(f"  Location: {[l.strip() for l in o.split(chr(10)) if l.strip() and l.strip()!='n']}", flush=True)
            escaped = True
            break
    
    if not escaped:
        print("  Trying other directions...", flush=True)
        for d in ["e","s","u","d"]:
            o = raw_cmd(d)
            if 'help getting out' in o.lower(): raw_cmd("no"); continue
            if "witt" not in o.lower():
                print(f"  Escaped via {d}!", flush=True)
                escaped = True
                break
    
    # Navigate toward a lit area and wait for cave closing
    print("\n=== Navigating to wait for cave closing ===", flush=True)
    cmd("look")
    
    # Try to get to Y2 or plover room
    # From wherever we are, try plugh or plover  
    cmd("off lamp")  # Save battery
    
    cave_closed = False
    for i in range(60):
        if axe_held:
            o = raw_cmd("drop axe" if i % 2 == 0 else "take axe")
        else:
            o = raw_cmd("look")
        ol = o.lower()
        
        if 'help getting out' in ol:
            raw_cmd("no")
        if 'wish to quit' in ol:
            raw_cmd("no")
            
        if 'closing soon' in ol or 'cave is now closed' in ol or 'repository' in ol or 'blinding' in ol or 'puff of' in ol:
            print(f"  ** CAVE EVENT at turn {turn}! **", flush=True)
            lines = [l.strip() for l in o.split('\n') if l.strip()]
            for l in lines:
                if len(l) > 2: print(f"  {l}", flush=True)
            if 'repository' in ol or 'blinding' in ol:
                cave_closed = True
                break
    
    if not cave_closed:
        # Maybe we need more turns
        for i in range(30):
            o = raw_cmd("wait" if i % 3 != 0 else "look")
            ol = o.lower()
            if 'help getting out' in ol: raw_cmd("no")
            if 'wish to quit' in ol: raw_cmd("no")
            if 'repository' in ol or 'blinding' in ol:
                cave_closed = True
                print(f"  ** TELEPORTED to repository! **", flush=True)
                break
    
    # Repository endgame
    print("\n=== Repository Endgame ===", flush=True)
    cmd("look")
    cmd("sw")
    cmd("take rod")
    cmd("ne")  
    cmd("drop rod")
    cmd("sw")
    cmd("blast")
    cmd("look")
    
    print(f"\n=== GAME COMPLETE, {turn} turns ===", flush=True)
    os.close(master)
    os.waitpid(pid, 0)
