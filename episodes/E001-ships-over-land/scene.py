"""E001 TEST: the ships that crossed land, 22 April 1453. About 75 s, one wall, left to right.

Clusters: A cold open (date + harbour detail of the Le Tavernier miniature) | B the chain (Buondelmonti
map) | C Mehmed (Bellini portrait, age) | D overland (the full Le Tavernier miniature, ~70 ships)
| E two fronts and the fall (Zonaro) | F the chain today (Naval Museum photo), then the whole wall.
World units are 4K px at zoom 1; frame height in world units = 2160 / zoom. Portrait prints are
narrower so they fit whole. Every time comes from the voice: L(i), E(i), W(i, word).
"""
from engine import HILITE, BigText, Counter, Film, PenMark, Print, Stamp, StringLine

AX, BX, CX, DX, EX, FX = 0, 6600, 12000, 18200, 25400, 31600
INK = (30, 26, 22)
CREAM = (244, 238, 226)


def build_film(doc):
    L, E, W = doc.L, doc.E, doc.W
    film = Film(doc.duration, fps=30, look="wall")
    cam, foc, cue = film.cam, film.focus, film.cue

    # A  cold open (1-2): the date, then the fleet inside the harbour
    film.add(BigText("22 APRIL 1453", AX, -2000, 540, L(1) - 0.1, type_on=0.6, bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(Print("P06", AX, 600, 3000, rot=-1.2, t_in=W(1, "impossible") - 0.25,
                   label="THE GOLDEN HORN, 1453", label_t=L(2) + 0.2))
    film.add(PenMark("ellipse", AX - 150, 250, 2300, 900, t_in=W(2, "inside") - 0.2, dur=0.6, width=26, seed=3, rot=-2))
    cam(0.0, AX, -1900, 1.0, -0.8)
    cam(W(1, "defenders"), AX, -1100, 0.62, -0.3)
    cam(W(1, "impossible") + 0.4, AX, 650, 0.7, 0.0)
    cam(E(2) + 0.2, AX + 100, 500, 0.82, 0.4)
    foc(0.0, AX, -2000, 1900, 0.5)
    foc(W(1, "impossible"), AX, 600, 2600, 0.55)

    # B  the chain (3-4)
    cue("riser", L(3) - 1.0, 0.4, dur=0.9)
    film.add(StringLine((AX + 1500, -500), (BX - 950, -1250), t_in=L(3) + 0.1, dur=0.8, sag=0.04, width=16))
    film.add(Print("P05", BX, 350, 1900, rot=1.4, t_in=L(3) + 0.3, label="CONSTANTINOPLE, c. 1420", label_t=W(3, "harbor")))
    film.add(BigText("THE CHAIN", BX, -1750, 480, W(3, "chain") - 0.15, rgb=CREAM, hit=None))
    film.add(Stamp("SEALED", BX + 250, 500, size=300, rot=-9, t_in=W(4, "out") - 0.1))
    cam(L(3) + 0.4, (AX + BX) / 2, -200, 0.4, 0.0)
    cam(W(3, "chain"), BX, -700, 0.62, 0.5)
    cam(E(3) + 0.1, BX, 150, 0.6, 0.6)
    cam(W(4, "Golden"), BX + 80, 300, 0.64, 0.8)
    cam(E(4) + 0.1, BX + 150, 400, 0.68, 0.9)
    foc(L(3) + 0.3, BX, 0, 3000, 0.5)
    foc(W(4, "out") - 0.2, BX + 250, 500, 2400, 0.6)

    # C  Mehmed (5)
    film.add(StringLine((BX + 1000, -900), (CX - 850, -1300), t_in=L(5) + 0.05, dur=0.7, sag=0.05, width=16))
    film.add(Print("P02", CX, -350, 1700, rot=-1.6, t_in=L(5) + 0.15, label="SULTAN MEHMED II", label_t=W(5, "Mehmed") + 0.2))
    film.add(Counter(CX, 1750, 600, 21, W(5, "twenty") - 0.1, dur=0.8, caption="YEARS OLD"))
    cam(L(5) + 0.35, CX, -300, 0.66, -0.4)
    cam(W(5, "twenty") + 0.1, CX, 350, 0.56, -0.2)
    cam(E(5) + 0.1, CX, 300, 0.54, 0.0)
    foc(L(5) + 0.3, CX, -350, 2000, 0.6)
    foc(W(5, "twenty"), CX, 900, 2800, 0.5)

    # D  overland (6-8): the whole miniature, where the ships cross the hill
    cue("riser", L(6) - 0.9, 0.45, dur=0.9)
    film.add(StringLine((CX + 950, -1300), (DX - 1050, -1500), t_in=L(6) + 0.05, dur=0.7, sag=0.05, width=16))
    film.add(Print("P03", DX, 0, 2000, rot=1.0, t_in=L(6) + 0.1, label="SHIPS OVER THE HILL, LE TAVERNIER", label_t=W(6, "Galata")))
    film.add(BigText("OVER THE HILL", DX - 2650, -700, 400, W(6, "road") - 0.1, rgb=CREAM, hit=None))
    film.add(Counter(DX + 2500, 100, 640, 70, W(7, "seventy") - 0.15, dur=1.0, prefix="~", caption="SHIPS"))
    film.add(PenMark("underline", DX + 2500, 900, 1700, 30, t_in=W(8, "behind") - 0.2, dur=0.5, width=22, seed=8))
    cam(L(6) + 0.3, (CX + DX) / 2, -200, 0.4, 0.0)
    cam(W(6, "road") + 0.2, DX - 900, -100, 0.56, 0.4)
    cam(W(6, "Galata"), DX, 150, 0.62, 0.6)
    cam(W(7, "seventy") + 0.2, DX + 1200, 150, 0.54, 0.2)
    cam(E(7), DX + 1300, 150, 0.53, 0.0)
    cam(L(8) + 0.3, DX + 100, 100, 0.64, -0.4)
    cam(E(8) + 0.1, DX + 150, 150, 0.68, -0.6)
    foc(L(6) + 0.2, DX - 600, 0, 3800, 0.45)
    foc(W(7, "seventy"), DX + 1500, 200, 3400, 0.45)
    foc(L(8) + 0.2, DX, 0, 2600, 0.55)

    # E  two fronts, then the fall (9-10)
    film.add(StringLine((DX + 1050, -1500), (EX - 1500, -500), t_in=L(9) + 0.05, dur=0.8, sag=0.04, width=16))
    film.add(Print("P01", EX, 500, 3000, rot=-1.0, t_in=L(9) + 0.15, label="MEHMED'S ARMY AT THE WALLS (ZONARO)", label_t=W(9, "guarded")))
    film.add(BigText("TWO FRONTS", EX, -1500, 520, W(9, "harbor") - 0.1, t_out=W(10, "May") - 0.3, rgb=CREAM, hit=None))
    film.add(BigText("29 MAY 1453", EX, -1500, 540, W(10, "May") - 0.1, type_on=0.5, bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(Stamp("FALLEN", EX + 700, 900, size=360, rot=-8, t_in=W(10, "fell") - 0.05))
    for k in range(2):
        cue("heartbeat", L(9) + 0.3 + k * 0.95, 0.5)
    cam(E(8) + 0.5, (DX + EX) / 2, -300, 0.36, 0.0)
    cam(L(9) + 0.7, EX, 0, 0.53, 0.3)
    cam(E(9), EX, 50, 0.52, 0.0)
    cam(W(10, "May"), EX, -100, 0.53, -0.2)
    cam(E(10) + 0.2, EX + 300, 500, 0.66, -0.4)
    foc(L(9) + 0.6, EX, -200, 3200, 0.5)
    foc(W(10, "fell") - 0.2, EX + 500, 700, 2400, 0.6)

    # F  the chain today, then the whole wall (11)
    film.add(StringLine((EX + 1500, -500), (FX - 1300, -700), t_in=L(11) + 0.05, dur=0.7, sag=0.04, width=16))
    film.add(Print("P04", FX, 200, 2600, rot=1.6, t_in=L(11) + 0.2, label="ISTANBUL NAVAL MUSEUM", label_t=W(11, "Istanbul")))
    cam(L(11) + 0.4, FX, 300, 0.78, 0.6)
    cam(E(11) - 0.3, FX - 300, 300, 0.66, 0.3)
    cam(film.duration, 15800, 0, 0.115, 0.0)
    foc(L(11) + 0.3, FX, 200, 2400, 0.6)
    foc(E(11), 15800, 0, 26000, 0.1)

    film.fade_in, film.fade_out = 0.8, 1.8
    return film
