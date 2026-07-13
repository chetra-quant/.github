#!/usr/bin/env python3
"""Generate profile/pipeline.svg — the chetra-quant gate chain, two-row snake, one adversary connector."""
from html import escape

W, H = 1600, 640
BG = "#0A0E17"
NODE = "#111826"
STROKE = "#1E293B"
WHITE = "#F8FAFC"
CYAN = "#22D3EE"
EMER = "#34D399"
AMBER = "#F59E0B"
MUTE = "#94A3B8"

BW, BH = 220, 68
COLS = 6
X0 = 40
STEP = 260  # 220 box + 40 gap
R1Y = 96
R2Y = 300

def cx(i): return X0 + i * STEP + BW / 2
def left(i): return X0 + i * STEP
def right(i): return X0 + i * STEP + BW

# (label, sub, kind)  kind: process | gate | paper | human | live
row1 = [
    ("Signal", None, "process"),
    ("Backtest", None, "process"),
    ("Causality", "gate", "gate"),
    ("Sel-block select", None, "process"),
    ("Pre-register", None, "process"),
    ("Holdout", "opened once, ever", "gate"),
]
row2 = [
    ("Spread stress", "1.5× stress", "gate"),
    ("Correlation", "gate", "gate"),
    ("MT5 real-spread", "broker replay", "gate"),
    ("Paper book", "autonomous", "paper"),
    ("Human gate", "approval", "human"),
    ("Live", "human-gated", "live"),
]

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-sans-serif, -apple-system, Segoe UI, Helvetica, Arial, sans-serif">')
parts.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# arrow marker
parts.append(f'''<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 z" fill="{CYAN}"/>
  </marker>
  <marker id="arrA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 z" fill="{MUTE}"/>
  </marker>
</defs>''')

def node(i, y, label, sub, kind):
    x = left(i)
    fill, stk, txt, sw = NODE, STROKE, WHITE, 1.5
    tag = None
    if kind == "gate":
        stk, sw = WHITE, 1.5
    elif kind == "paper":
        fill, stk, txt = EMER, EMER, "#062A1E"
    elif kind == "human":
        fill, stk = NODE, AMBER
        sw = 2
    elif kind == "live":
        fill, stk, txt = "#241A08", AMBER, "#FBBF24"
        sw = 1.5
    out = [f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="13" fill="{fill}" stroke="{stk}" stroke-width="{sw}"/>']
    cxx = x + BW / 2
    if kind == "human":
        # lock glyph left of text
        lx, ly = x + 26, y + BH/2
        out.append(f'<rect x="{lx-9}" y="{ly-4}" width="18" height="15" rx="3" fill="none" stroke="{AMBER}" stroke-width="2"/>')
        out.append(f'<path d="M {lx-5} {ly-4} v-5 a5 5 0 0 1 10 0 v5" fill="none" stroke="{AMBER}" stroke-width="2"/>')
        cxx = x + BW / 2 + 14
    if sub == "gate":
        # tiny 'gate' eyebrow, main label centered
        out.append(f'<text x="{cxx}" y="{y+28}" fill="{CYAN}" font-size="11" font-weight="700" letter-spacing="2" text-anchor="middle">GATE</text>')
        out.append(f'<text x="{cxx}" y="{y+51}" fill="{txt}" font-size="19" font-weight="600" text-anchor="middle">{escape(label)}</text>')
    elif sub:
        out.append(f'<text x="{cxx}" y="{y+34}" fill="{txt}" font-size="19" font-weight="600" text-anchor="middle">{escape(label)}</text>')
        subcol = CYAN if kind in ("gate",) else (MUTE if kind in ("paper","live","human") else MUTE)
        if kind == "paper": subcol = "#0A3D2A"
        out.append(f'<text x="{cxx}" y="{y+53}" fill="{subcol}" font-size="12.5" font-weight="600" text-anchor="middle">{escape(sub)}</text>')
    else:
        out.append(f'<text x="{cxx}" y="{y+BH/2+6}" fill="{txt}" font-size="19" font-weight="600" text-anchor="middle">{escape(label)}</text>')
    return "\n".join(out)

# horizontal arrows within a row
def harrow(i, y):
    x1 = right(i) + 4
    x2 = left(i+1) - 4
    yy = y + BH/2
    return f'<line x1="{x1}" y1="{yy}" x2="{x2}" y2="{yy}" stroke="{CYAN}" stroke-width="2.2" marker-end="url(#arr)"/>'

# draw row1 arrows
for i in range(COLS-1):
    parts.append(harrow(i, R1Y))
# return connector: Holdout (row1 col5) bottom -> down/left -> Spread stress (row2 col0) left
hx = cx(5); hy = R1Y + BH
sx = left(0); sy = R2Y + BH/2
midy = (R1Y + BH + R2Y) / 2
path = f'M {hx} {hy} C {hx} {hy+50}, {sx-70} {midy}, {sx-70} {R2Y+BH/2} L {sx-4} {R2Y+BH/2}'
parts.append(f'<path d="{path}" fill="none" stroke="{CYAN}" stroke-width="2.2" marker-end="url(#arr)"/>')
# draw row2 arrows
for i in range(COLS-1):
    parts.append(harrow(i, R2Y))

# nodes
for i,(l,s,k) in enumerate(row1):
    parts.append(node(i, R1Y, l, s, k))
for i,(l,s,k) in enumerate(row2):
    parts.append(node(i, R2Y, l, s, k))

# Adversary row — one box, one labelled connector up to the pipeline
ADY = 500
adx, adw = 300, 560
parts.append(f'<rect x="{adx}" y="{ADY}" width="{adw}" height="66" rx="13" fill="{NODE}" stroke="{CYAN}" stroke-width="1.5" stroke-dasharray="6 4"/>')
parts.append(f'<text x="{adx+adw/2}" y="{ADY+28}" fill="{CYAN}" font-size="13" font-weight="700" letter-spacing="2" text-anchor="middle">ADVERSARY</text>')
parts.append(f'<text x="{adx+adw/2}" y="{ADY+50}" fill="{WHITE}" font-size="15" font-weight="500" text-anchor="middle">label-shuffle · look-ahead probe · spread-double</text>')
# one connector from top of adversary box up to row2 (points at the gate band)
ax = adx + adw/2
parts.append(f'<line x1="{ax}" y1="{ADY}" x2="{ax}" y2="{R2Y+BH+6}" stroke="{MUTE}" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#arrA)"/>')
parts.append(f'<text x="{ax+16}" y="{(ADY + R2Y+BH)/2+5}" fill="{MUTE}" font-size="14" font-weight="600" text-anchor="start">tries to kill every survivor</text>')

# caption bottom
parts.append(f'<text x="{X0}" y="{H-24}" fill="{MUTE}" font-size="14" font-weight="500">Autonomous through paper — a human hand gates live. Every gate is a place to say no.</text>')

parts.append('</svg>')
svg = "\n".join(parts)
open("/tmp/cq-profile/profile/pipeline.svg", "w").write(svg)
# html wrapper for exact-size screenshot
open("/private/tmp/claude-501/-Users-mac/f1dd7d83-37a4-4942-8abb-4709b6d15a70/scratchpad/pipeline.html", "w").write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;padding:0}}body{{background:{BG}}}</style></head><body>{svg}</body></html>')
print("wrote svg", len(svg), "bytes")
