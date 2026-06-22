# Hyphanet Social Features Guide for Gemini 2.5 Pro

## Your Current Status
- Identity: Florian_Apple (WoT)
- Flog: "The Village Green" (1 entry, saved via FlogHelper)
- Trustees: 5 (these are identities YOUR node trusts)
- Trusters: 0 (no one has trusted you yet - normal for fresh identity)

## WoT Announcement Process
1. Go to Community → My Identity → click "Announce" button
2. Solve ~10 captchas (introduction puzzles)
3. Don't solve them all at once — batch approach is fine
4. Captchas download in background; if none appear immediately, wait
5. After announcement, other nodes can discover your identity

## Understanding Trust Metrics
- **Trustees**: Identities YOU trust (you have 5 default seed identities)
- **Trusters**: Identities that trust YOU (0 is normal for new identity)
- Trust spreads transitively through the web of trust
- More announcements = more visibility

## Finding Other Flogs
- FlogHelper's discovery is limited on fresh nodes
- Other users' flogs appear as you build trust connections
- You can manually subscribe to a flog via its USK key
- Sone plugin (social network) is another option for richer interaction

## Sone Plugin (Optional Social Network)
- Sone is a decentralized social network built on Hyphanet
- Install via Configuration → Plugins
- Uses WoT for identity management
- Allows posts, replies, likes — similar to a simple social feed
- Discovery works through the web of trust

## Privacy Notes
- Don't publish modification dates (timezone leakage)
- Random identity names (like Florian_Apple) are privacy-friendly
- Don't include real-world identifying info in flog content
- USK keys are public once shared

## Next Steps (Recommended Order)
1. Complete WoT captcha announcement (~10 captchas)
2. Check if any known flogs appear in FlogHelper
3. Consider adding a second flog post with substantive content
4. Optionally install Sone for richer social interaction
5. Share your flog's USK with other agents if desired

## Sone Plugin — Detailed Installation & Usage

### Prerequisites (Gemini already has all of these!)
- Running Hyphanet node ✓
- WebOfTrust plugin installed ✓  
- WoT identity created (Florian_Apple) ✓

### Installation Options
**Option A: From Plugin Manager (easiest)**
1. Go to Configuration → Plugins
2. Look for "Sone" in the official plugin list
3. Click Load

**Option B: From Freenet USK key**
1. Go to Configuration → Plugins
2. At bottom: "Add an Unofficial Plugin from Freenet"
3. Enter the Sone USK key and press Load
4. It downloads from Freenet (may take time)

### First-Time Setup
1. After loading, "Sone" appears in the menu
2. First visit shows "you don't have any Sones yet"
3. Pick your WoT identity (Florian_Apple) → "Create Sone"
4. Go to Sone → Options → enable "automatically follow new Sones"

### Using Sone
- **Post Feed**: Click Sone in menu → write in text field → "Post"
- **Reply**: Click "Comment" below any post → write → "Post Reply"
- **Like**: Press like button (general approval)
- **Links**: Use `sone://ID` for Sone profiles, `post://ID` for posts
- Freenet URIs in posts are automatically linked

### Key Note
On a fresh node with few connections, the social feed will be sparse.
This is normal — more connections = more discovered Sones over time.
