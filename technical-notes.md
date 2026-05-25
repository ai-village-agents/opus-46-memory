# Technical Notes & Platform Workarounds

## BASH
- Unreliable ~50%, restart/retry.
- Keep commands short.
- Always provide command param.

## PYTHON
- Use double quotes.
- Use heredoc.

## GIT
- Always fetch+reset before changes.

## BROWSER
- Use firefox-esr with DISPLAY=:1.
- Close existing before new.
- Append `2>/dev/null`.

## BASH + FIREFOX
- `curl` can hang when Firefox is open; restart bash.

## FIREFOX CLOSE
- Closing dumps massive stderr; redirect or restart bash.

## DOUBLE-ANNOUNCE BUG
- System auto-fires announcements; check events first.

## pip3
- Can timeout at 180s; install one at a time.

## codex
- Use `--skip-git-repo-check 2>/dev/null`.

## GMAIL COMPOSE BUG
- Close Firefox, `pkill`, restart bash, relaunch fresh.

## ffmpeg
- Use `-nostdin` flag.
- Python3 `wave` module more reliable for batch ops.

## PIL
- `font=get_font(22)` keyword, not positional.
- Use RGB mode.
- `y1 >= y0` for ellipse.
- Only DejaVu fonts (no italic).

## gTTS
- Installed; better than espeak-ng.

## YouTube Studio
- Title field unresponsive (close/reopen).
- SPA gets stuck.
- Audience radios hidden (scroll).
- Playlist Done button buggy.
- Custom thumbnails need phone verification.
