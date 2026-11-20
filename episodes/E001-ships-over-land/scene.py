"""E001 TEST: the ships that crossed land, 22 April 1453. About 60 s, one wall, left to right.

Clusters: A cold open (date + fleet painting) | B the chain (city map) | C Mehmed (portrait, age)
| D overland (road painting, route, counter) | E two fronts, the fall | F the chain today.
World units are 4K px at zoom 1. Every time comes from the voice: L(i), E(i), W(i, word).
"""
from engine import HILITE, RUST, BigText, Counter, Film, PenMark, Print, Route, Stamp, StringLine

AX, BX, CX, DX, EX, FX = 0, 6800, 12800, 19200, 25600, 31200
INK = (30, 26, 22)
CREAM = (244, 238, 226)


def build_film(doc):
    L, E, W = doc.L, doc.E, doc.W
    film = Film(doc.duration, fps=30, look="wall")
    cam, foc, cue = film.cam, film.focus, film.cue

    # A  cold open (1-2)
    film.add(BigText("22 APRIL 1453", AX, -2150, 560, L(1) - 0.1, type_on=0.6, bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    fleet = film.add(Print("P03", AX, 450, 3000, rot=-1.2, t_in=W(1, "impossible") - 0.2, label="THE GOLDEN HORN", label_t=L(2) + 0.2))
    film.add(PenMark("ellipse", AX, 450, 2400, 1300, t_in=W(2, "inside") - 0.2, dur=0.6, width=26, seed=3, rot=-2))
    cam(0.0, AX, -1900, 1.05, -0.8)
    cam(W(1, "defenders"), AX, -1300, 0.6, -0.3)
    cam(W(1, "impossible") + 0.4, AX, 550, 0.66, 0.0)
    cam(E(2) + 0.2, AX + 100, 550, 0.74, 0.4)
    foc(0.0, AX, -2100, 1900, 0.5)
    foc(W(1, "impossible"), AX, 400, 2600, 0.55)

    # B  the chain (3-4)
    cue("riser", L(3) - 1.0, 0.4, dur=0.9)
    film.add(StringLine((AX + 1500, -700), (BX - 1700, -800), t_in=L(3) + 0.1, dur=0.8, sag=0.04, width=16))
    city = film.add(Print("P05", BX, 300, 3000, rot=1.4, t_in=L(3) + 0.3, label="CONSTANTINOPLE", label_t=W(3, "harbor")))
    film.add(BigText("THE CHAIN", BX, -2250, 520, W(3, "chain") - 0.15, rgb=CREAM, hit=None))
    film.add(Stamp("SEALED", BX + 300, 700, size=320, rot=-9, t_in=W(4, "out") - 0.1))
    cam(L(3) + 0.4, (AX + BX) / 2, -300, 0.42, 0.0)
    cam(W(3, "chain"), BX, -800, 0.68, 0.5)
    cam(E(3) + 0.1, BX, 200, 0.62, 0.6)
    cam(W(4, "Golden"), BX + 100, 450, 0.68, 0.8)
    cam(E(4) + 0.1, BX + 200, 550, 0.74, 0.9)
    foc(L(3) + 0.3, BX, 0, 3000, 0.5)
    foc(W(4, "out") - 0.2, BX + 300, 600, 2200, 0.6)

    # C  Mehmed (5)
    film.add(StringLine((BX + 1500, -900), (CX - 900, -1200), t_in=L(5) + 0.05, dur=0.7, sag=0.05, width=16))
    film.add(Print("P02", CX, -300, 1900, rot=-1.6, t_in=L(5) + 0.15, label="SULTAN MEHMED II", label_t=W(5, "Mehmed") + 0.2))
    film.add(Counter(CX, 1900, 640, 21, W(5, "twenty") - 0.1, dur=0.8, caption="YEARS OLD"))
    cam(L(5) + 0.35, CX, -200, 0.7, -0.4)
    cam(W(5, "twenty") + 0.1, CX, 500, 0.56, -0.2)
    cam(E(5) + 0.1, CX, 450, 0.54, 0.0)
    foc(L(5) + 0.3, CX, -300, 2000, 0.6)
    foc(W(5, "twenty"), CX, 1300, 2600, 0.5)

    # D  overland (6-8)
    cue("riser", L(6) - 0.9, 0.45, dur=0.9)
    road = film.add(Print("P01", DX, 200, 3300, rot=1.0, t_in=L(6) + 0.1, label="OVER THE HILL BEHIND GALATA", label_t=W(6, "Galata")))
    film.add(BigText("OVER THE HILL", DX, -2300, 520, W(6, "road") - 0.1, rgb=CREAM, hit=None))
    film.add(Route((DX - 2400, 2350), (DX + 2400, 2350), t_in=W(6, "logs") - 0.1, dur=1.4, bend=-0.35, width=48, rgb=RUST))
    film.add(Counter(DX, 3150, 700, 70, W(7, "seventy") - 0.15, dur=1.0, prefix="~", caption="SHIPS"))
    film.add(PenMark("underline", DX, 2050, 3000, 40, t_in=W(8, "behind") - 0.2, dur=0.5, width=24, seed=8))
    cam(L(6) + 0.3, (CX + DX) / 2, -200, 0.4, 0.0)
    cam(W(6, "road") + 0.2, DX, -900, 0.66, 0.4)
    cam(W(6, "Galata"), DX, 500, 0.62, 0.6)
    cam(W(7, "seventy") + 0.2, DX, 1800, 0.55, 0.2)
    cam(E(7), DX, 1700, 0.53, 0.0)
    cam(L(8) + 0.3, DX + 200, 600, 0.66, -0.4)
    cam(E(8) + 0.1, DX + 250, 650, 0.72, -0.6)
    foc(L(6) + 0.2, DX, 0, 3400, 0.5)
    foc(W(7, "seventy"), DX, 3000, 2600, 0.55)
    foc(L(8) + 0.2, DX, 300, 2600, 0.55)

    # E  two fronts, the fall (9-10)
    film.add(BigText("TWO FRONTS", EX, -1300, 600, W(9, "harbor") - 0.1, rgb=CREAM, hit=None))
    film.add(PenMark("underline", EX, -900, 3600, 40, t_in=W(9, "thinner") - 0.3, dur=0.5, width=26, seed=11))
    film.add(BigText("29 MAY 1453", EX, 700, 600, W(10, "May") - 0.1, type_on=0.5, bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(Stamp("FALLEN", EX + 400, 1600, size=360, rot=-8, t_in=W(10, "fell") - 0.05))
    for k in range(2):
        cue("heartbeat", L(9) + 0.3 + k * 0.95, 0.5)
    cam(E(8) + 0.5, (DX + EX) / 2, 0, 0.36, 0.0)
    cam(L(9) + 0.6, EX, -900, 0.66, 0.3)
    cam(E(9), EX, -600, 0.6, 0.0)
    cam(W(10, "May") - 0.2, EX, 300, 0.52, -0.2)
    cam(E(10) + 0.2, EX + 200, 600, 0.56, -0.4)
    foc(L(9) + 0.2, EX, -1200, 2600, 0.55)
    foc(W(10, "May"), EX, 1100, 2600, 0.55)

    # F  the chain today, then the whole wall (11)
    film.add(StringLine((EX + 1800, -1300), (FX - 1400, -1400), t_in=L(11) + 0.05, dur=0.7, sag=0.04, width=16))
    film.add(Print("P04", FX, 0, 2700, rot=1.6, t_in=L(11) + 0.2, label="ISTANBUL NAVAL MUSEUM", label_t=W(11, "Istanbul")))
    cam(L(11) + 0.4, FX, 150, 0.74, 0.6)
    cam(E(11) - 0.3, FX - 300, 150, 0.62, 0.3)
    cam(film.duration, 15600, 400, 0.118, 0.0)
    foc(L(11) + 0.3, FX, 0, 2400, 0.6)
    foc(E(11), 15600, 200, 26000, 0.1)

    film.fade_in, film.fade_out = 0.8, 1.8
    return film
