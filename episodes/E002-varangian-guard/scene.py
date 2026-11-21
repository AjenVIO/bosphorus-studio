"""E002: The Varangian Guard — The Emperor's Viking Bodyguard.
20 minutes (~2,710 spoken words), 12 takes across 12 clusters laid out left to right along the X axis.
World units are 4K screen px at zoom 1.0 (frame shows 3840 x 2160 world px).
Frame height in world units = 2160 / zoom.
Hits land on spoken words using doc.W(line, "word").
"""
from engine import HILITE, BigText, Card, Counter, Film, PenMark, Print, Stamp, StringLine

# Cluster center X coordinates across the evidence wall
C01_X = 0
C02_X = 7000
C03_X = 14000
C04_X = 21000
C05_X = 28000
C06_X = 35000
C07_X = 42000
C08_X = 49000
C09_X = 56000
C10_X = 63000
C11_X = 70000
C12_X = 77000

INK = (26, 22, 18)
CREAM = (244, 238, 226)
GOLD = (230, 190, 70)


def build_film(doc):
    L, E, W = doc.L, doc.E, doc.W
    film = Film(doc.duration, fps=30, look="wall")
    cam, foc, cue = film.cam, film.focus, film.cue

    # =========================================================================
    # CLUSTER 1 (T01, Lines 1-12): Cold Open — The Rune on the Marble
    # =========================================================================
    p01 = film.add(Print("P01", C01_X, 200, 2600, rot=-1.0, t_in=L(1),
                         label="HAGIA SOPHIA · RUNIC GRAFFITI", label_t=W(2, "Halfdan")))
    film.add(BigText("HALFDAN", C01_X - 1200, -1400, 520, W(2, "Halfdan") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(PenMark("ellipse", C01_X - 100, 150, 1400, 600, t_in=W(2, "homeland") - 0.2,
                     dur=0.7, width=22, rot=-2))
    film.add(BigText("THE VARANGIAN GUARD", C01_X + 1300, -1500, 500, W(6, "centuries") - 0.2,
                     rgb=CREAM, hit=None))

    cam(0.0, C01_X - 300, 200, 0.72, -0.6)
    cam(W(1, "guardsman"), C01_X, 100, 0.68, -0.4)
    cam(W(2, "Halfdan"), C01_X - 500, -400, 0.62, 0.2)
    cam(L(6), C01_X + 400, -500, 0.52, 0.4)
    cam(E(12) - 0.5, C01_X + 200, 0, 0.48, 0.0)
    foc(0.0, C01_X, 200, 2600, 0.6)
    foc(W(2, "Halfdan"), C01_X - 600, -500, 2800, 0.55)
    foc(L(6), C01_X, 0, 3400, 0.5)

    # =========================================================================
    # CLUSTER 2 (T02, Lines 13-26): Crisis of 987 — The Throne in Peril
    # =========================================================================
    cue("riser", L(13) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C01_X + 1500, -500), (C02_X - 1500, -600), t_in=L(13) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("WINTER 987", C02_X - 1600, -1500, 520, W(13, "winter") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p02 = film.add(Print("P02", C02_X - 1000, 200, 2200, rot=1.2, t_in=L(13) + 0.2,
                         label="EMPEROR BASIL II (MARCIANA PSALTER)", label_t=W(13, "Second")))
    p03 = film.add(Print("P03", C02_X + 1200, 300, 2600, rot=-1.5, t_in=L(15) + 0.1,
                         label="CLASH OF PHOKAS AND SKLEROS (SKYLITZES)", label_t=W(15, "Phokas")))
    film.add(BigText("PHOKAS & SKLEROS", C02_X + 1000, -1500, 480, W(15, "Skleros") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(BigText(">50% OVERTHROWN", C02_X, 1700, 480, W(19, "half") - 0.2,
                     rgb=GOLD, hit=None))
    film.add(Stamp("THREATENED", C02_X - 400, 800, size=320, rot=-8, t_in=L(18) + 0.2))

    cam(L(13) + 0.3, (C01_X + C02_X) / 2, 0, 0.32, 0.0)
    cam(W(13, "winter"), C02_X - 1200, -500, 0.60, 0.4)
    cam(W(15, "Phokas"), C02_X + 800, -400, 0.58, -0.3)
    cam(W(19, "history"), C02_X, 600, 0.54, 0.0)
    cam(E(26) - 0.5, C02_X + 200, 100, 0.50, 0.2)
    foc(L(13) + 0.2, C02_X - 1000, 0, 3000, 0.55)
    foc(W(15, "Skleros"), C02_X + 1000, 100, 3200, 0.5)

    # =========================================================================
    # CLUSTER 3 (T03, Lines 27-40): The Kiev Alliance & Vladimir
    # =========================================================================
    cue("riser", L(27) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C02_X + 1500, -600), (C03_X - 1500, -500), t_in=L(27) + 0.1, dur=0.9, sag=0.04, width=16))
    p04 = film.add(Print("P04", C03_X - 1200, 200, 2200, rot=-1.2, t_in=L(28) + 0.1,
                         label="GRAND PRINCE VLADIMIR OF KIEV", label_t=W(28, "Vladimir")))
    film.add(BigText("GRAND PRINCE VLADIMIR", C03_X - 1200, -1500, 460, W(28, "Vladimir") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(BigText("ANNA PORPHYROGENITA", C03_X + 100, -1400, 440, W(32, "Anna") - 0.2,
                     rgb=GOLD, hit=None))
    p05 = film.add(Print("P05", C03_X + 1100, 100, 2500, rot=1.4, t_in=L(38) + 0.1,
                         label="BAPTISM OF VLADIMIR (VASNETSOV)", label_t=L(39)))
    film.add(Counter(C03_X + 600, 1700, 600, 6000, W(40, "thousand") - 0.2, dur=1.2, caption="WARRIORS"))

    cam(L(27) + 0.3, (C02_X + C03_X) / 2, 0, 0.30, 0.0)
    cam(W(28, "Vladimir"), C03_X - 1000, -400, 0.58, -0.3)
    cam(W(32, "Anna"), C03_X, -600, 0.54, 0.2)
    cam(L(38) + 0.4, C03_X + 1000, -100, 0.56, 0.4)
    cam(W(40, "thousand"), C03_X + 700, 600, 0.52, 0.0)
    cam(E(40) - 0.4, C03_X + 200, 200, 0.46, -0.2)
    foc(L(28), C03_X - 1000, 0, 3000, 0.55)
    foc(L(38), C03_X + 1000, 100, 3200, 0.5)

    # =========================================================================
    # CLUSTER 4 (T04, Lines 41-56): Chrysopolis (988) and Abydos (989)
    # =========================================================================
    cue("riser", L(41) - 1.0, 0.5, dur=1.0)
    film.add(StringLine((C03_X + 1500, -500), (C04_X - 1500, -600), t_in=L(41) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("CHRYSOPOLIS 988", C04_X - 1400, -1500, 480, W(42, "Chrysopolis") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p08 = film.add(Print("P08", C04_X - 600, 200, 2600, rot=-1.0, t_in=L(44) + 0.1,
                         label="VARANGIANS IN BATTLE (MADRID SKYLITZES)", label_t=L(44) + 0.4))
    film.add(BigText("ABYDOS · APRIL 989", C04_X + 1200, -1500, 480, W(47, "April") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(BigText("TAGMA TON VARANGON", C04_X, 1750, 500, W(56, "Varangon") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(Stamp("VICTORY", C04_X + 600, 700, size=340, rot=-9, t_in=L(54) + 0.2))

    cam(L(41) + 0.3, (C03_X + C04_X) / 2, 0, 0.30, 0.0)
    cam(W(42, "Chrysopolis"), C04_X - 1200, -500, 0.56, 0.4)
    cam(L(44) + 0.4, C04_X - 500, 100, 0.60, 0.0)
    cam(W(47, "April"), C04_X + 1000, -500, 0.56, -0.3)
    cam(W(50, "dead"), C04_X + 300, 100, 0.58, 0.2)
    cam(W(56, "Varangon"), C04_X, 900, 0.52, 0.0)
    cam(E(56) - 0.4, C04_X + 100, 300, 0.48, -0.2)
    foc(L(42), C04_X - 1000, -200, 3200, 0.55)
    foc(W(47, "April"), C04_X + 800, 0, 3200, 0.5)

    # =========================================================================
    # CLUSTER 5 (T05, Lines 57-71): The River Road Austrvegr
    # =========================================================================
    cue("riser", L(57) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C04_X + 1500, -600), (C05_X - 1500, -500), t_in=L(57) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("MIKLAGARÐR", C05_X - 1500, -1500, 520, W(58, "City") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(BigText("AUSTRVEGR", C05_X + 300, -1500, 500, W(59, "Austrvegr") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p06 = film.add(Print("P06", C05_X, 150, 2700, rot=1.2, t_in=L(59) + 0.1,
                         label="VARANGIAN SHIPS ON THE RIVER (ROERICH)", label_t=W(59, "summer")))
    film.add(Counter(C05_X + 200, 1750, 560, 3000, W(70, "journey") - 0.2, dur=1.2, suffix=" KM", caption="EXPEDITION"))

    cam(L(57) + 0.3, (C04_X + C05_X) / 2, 0, 0.30, 0.0)
    cam(W(58, "City"), C05_X - 1200, -600, 0.56, -0.3)
    cam(W(59, "Austrvegr"), C05_X, -500, 0.58, 0.2)
    cam(L(64), C05_X, 150, 0.62, 0.4)
    cam(W(70, "journey"), C05_X + 200, 800, 0.54, 0.0)
    cam(E(71) - 0.4, C05_X + 100, 200, 0.48, -0.2)
    foc(L(58), C05_X - 800, -300, 3200, 0.5)
    foc(L(64), C05_X, 200, 3000, 0.55)

    # =========================================================================
    # CLUSTER 6 (T06, Lines 72-85): Miklagarðr & The Dane Axe
    # =========================================================================
    cue("riser", L(72) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C05_X + 1500, -500), (C06_X - 1500, -600), t_in=L(72) + 0.1, dur=0.9, sag=0.04, width=16))
    p07 = film.add(Print("P07", C06_X - 1200, 100, 2200, rot=-1.4, t_in=L(72) + 0.1,
                         label="CONSTANTINOPLE, BUONDELMONTI c. 1420", label_t=L(72) + 0.3))
    film.add(Counter(C06_X - 1200, 1600, 520, 500000, W(73, "thousand") - 0.2, dur=1.2, caption="POPULATION"))
    film.add(BigText("PELEKYPHOROI", C06_X, -1500, 480, W(76, "barbarians") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(BigText("THE DANE AXE", C06_X + 1200, -1500, 500, W(79, "axe") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p09 = film.add(Print("P09", C06_X + 200, 250, 2000, rot=1.6, t_in=L(79) + 0.1,
                         label="11TH-CENTURY VIKING BROADAXE", label_t=W(79, "weapon")))
    p10 = film.add(Print("P10", C06_X + 1500, 200, 2200, rot=-1.0, t_in=L(81) + 0.1,
                         label="SAXON HUSCARL WITH AXE (BAYEUX)", label_t=L(81) + 0.3))

    cam(L(72) + 0.3, (C05_X + C06_X) / 2, 0, 0.30, 0.0)
    cam(W(73, "thousand"), C06_X - 1100, 500, 0.54, 0.3)
    cam(W(76, "barbarians"), C06_X, -600, 0.58, -0.2)
    cam(W(79, "axe"), C06_X + 900, -300, 0.60, 0.4)
    cam(L(81), C06_X + 1200, 100, 0.58, 0.0)
    cam(E(85) - 0.4, C06_X + 200, 150, 0.48, -0.2)
    foc(L(72), C06_X - 1000, 200, 3000, 0.5)
    foc(W(79, "axe"), C06_X + 800, 100, 3200, 0.55)

    # =========================================================================
    # CLUSTER 7 (T07, Lines 86-100): Gold Nomisma & Polutasvarf & Runestones
    # =========================================================================
    cue("riser", L(86) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C06_X + 1500, -600), (C07_X - 1500, -500), t_in=L(86) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("GOLD NOMISMA", C07_X - 1400, -1500, 480, W(86, "rewards") - 0.2,
                     rgb=GOLD, hit=None))
    p11 = film.add(Print("P11", C07_X - 1100, 150, 1900, rot=1.0, t_in=L(87) + 0.1,
                         label="GOLD HISTAMENON OF BASIL II", label_t=L(87) + 0.3))
    film.add(BigText("POLUTASVARF", C07_X, -1500, 520, W(89, "Polutasvarf") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p12 = film.add(Print("P12", C07_X + 1100, 200, 2400, rot=-1.5, t_in=L(95) + 0.1,
                         label="ED RUNESTONE U 112 (RAGNVALD)", label_t=W(95, "Runestones")))
    film.add(Counter(C07_X + 1100, 1600, 520, 30, W(95, "thirty") - 0.2, dur=1.0, prefix="~", caption="RUNESTONES"))

    cam(L(86) + 0.3, (C06_X + C07_X) / 2, 0, 0.30, 0.0)
    cam(W(86, "rewards"), C07_X - 1200, -500, 0.58, -0.3)
    cam(W(89, "Polutasvarf"), C07_X, -600, 0.60, 0.2)
    cam(W(95, "thirty"), C07_X + 1000, 400, 0.56, 0.4)
    cam(E(100) - 0.4, C07_X + 200, 100, 0.48, -0.2)
    foc(L(87), C07_X - 1000, 0, 3000, 0.55)
    foc(W(95, "Runestones"), C07_X + 1000, 200, 3200, 0.5)

    # =========================================================================
    # CLUSTER 8 (T08, Lines 101-113): Basil II's Wars & Kleidion 1014
    # =========================================================================
    cue("riser", L(101) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C07_X + 1500, -500), (C08_X - 1500, -600), t_in=L(101) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("THE BULGARIAN WARS", C08_X - 1200, -1500, 460, W(103, "Samuel") - 0.2,
                     rgb=CREAM, hit=None))
    p13 = film.add(Print("P13", C08_X, 150, 2700, rot=-1.0, t_in=L(106) + 0.1,
                         label="DEFEAT OF BULGARS AT KLEIDION (SKYLITZES)", label_t=W(106, "Kleidion")))
    film.add(BigText("KLEIDION 1014", C08_X + 1000, -1500, 500, W(106, "fourteen") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))

    cam(L(101) + 0.3, (C07_X + C08_X) / 2, 0, 0.30, 0.0)
    cam(W(103, "Samuel"), C08_X - 900, -600, 0.56, 0.3)
    cam(W(106, "Kleidion"), C08_X, 0, 0.62, -0.2)
    cam(E(113) - 0.4, C08_X + 200, 150, 0.48, 0.2)
    foc(L(103), C08_X - 600, -300, 3200, 0.5)
    foc(W(106, "Kleidion"), C08_X, 150, 3200, 0.55)

    # =========================================================================
    # CLUSTER 9 (T09, Lines 114-126): Harald Hardrada & Sicily Expedition
    # =========================================================================
    cue("riser", L(114) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C08_X + 1500, -600), (C09_X - 1500, -500), t_in=L(114) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("1034 · HARALD SIGURDSSON", C09_X - 1200, -1500, 460, W(114, "Constantinople") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p14 = film.add(Print("P14", C09_X - 1000, 200, 2400, rot=1.4, t_in=L(116) + 0.1,
                         label="BATTLE OF STIKLESTAD 1030 (ARBO)", label_t=L(116) + 0.3))
    film.add(BigText("GEORGE MANIAKES", C09_X + 600, -1500, 480, W(119, "Maniakes") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(Counter(C09_X + 1000, 1600, 540, 80, W(120, "eighty") - 0.2, dur=1.0, prefix="~", caption="FORTS (SAGAS)"))

    cam(L(114) + 0.3, (C08_X + C09_X) / 2, 0, 0.30, 0.0)
    cam(W(114, "Constantinople"), C09_X - 900, -600, 0.56, -0.3)
    cam(L(116), C09_X - 800, 100, 0.60, 0.2)
    cam(W(119, "Maniakes"), C09_X + 400, -400, 0.56, 0.4)
    cam(W(120, "eighty"), C09_X + 800, 600, 0.54, 0.0)
    cam(E(126) - 0.4, C09_X + 200, 200, 0.48, -0.2)
    foc(L(114), C09_X - 800, -200, 3200, 0.55)
    foc(W(120, "eighty"), C09_X + 700, 300, 3200, 0.5)

    # =========================================================================
    # CLUSTER 10 (T10, Lines 127-142): Revolt of 1042 & Escape over Chain
    # =========================================================================
    cue("riser", L(127) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C09_X + 1500, -500), (C10_X - 1500, -600), t_in=L(127) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("APRIL 1042", C10_X - 1500, -1500, 500, W(127, "forty-two") - 0.2,
                     rgb=CREAM, hit=None))
    p15 = film.add(Print("P15", C10_X - 1000, 200, 2100, rot=-1.0, t_in=L(128) + 0.1,
                         label="EMPRESS ZOE (HAGIA SOPHIA MOSAIC)", label_t=L(128) + 0.3))
    p16 = film.add(Print("P16", C10_X + 1000, 150, 2500, rot=1.5, t_in=L(135) + 0.1,
                         label="BLINDING OF MICHAEL V (SKYLITZES)", label_t=W(135, "blinded")))
    film.add(BigText("MICHAEL V BLINDED", C10_X + 1000, -1500, 460, W(135, "blinded") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(BigText("HARALD HARDRADA", C10_X, 1750, 520, W(142, "Norway") - 0.2,
                     rgb=GOLD, hit=None))
    film.add(Stamp("ESCAPE", C10_X + 200, 700, size=320, rot=-8, t_in=W(142, "escaped") - 0.1))

    cam(L(127) + 0.3, (C09_X + C10_X) / 2, 0, 0.30, 0.0)
    cam(W(127, "forty-two"), C10_X - 1200, -600, 0.56, 0.3)
    cam(L(128), C10_X - 900, 100, 0.60, -0.2)
    cam(W(135, "blinded"), C10_X + 900, -200, 0.62, 0.4)
    cam(W(142, "escaped"), C10_X, 600, 0.54, 0.0)
    cam(E(142) - 0.4, C10_X + 200, 200, 0.48, -0.2)
    foc(L(128), C10_X - 800, 0, 3000, 0.5)
    foc(W(135, "blinded"), C10_X + 800, 100, 3200, 0.55)

    # =========================================================================
    # CLUSTER 11 (T11, Lines 143-159): 1066, Hastings & Dyrrhachium
    # =========================================================================
    cue("riser", L(143) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C10_X + 1500, -600), (C11_X - 1500, -500), t_in=L(143) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("STAMFORD BRIDGE", C11_X - 1600, -1500, 460, W(144, "Bridge") - 0.2,
                     rgb=CREAM, hit=None))
    p17 = film.add(Print("P17", C11_X - 1200, 200, 2400, rot=-1.2, t_in=L(144) + 0.1,
                         label="BATTLE OF STAMFORD BRIDGE 1066 (ARBO)", label_t=W(144, "Stamford")))
    film.add(BigText("HASTINGS 1066", C11_X - 100, -1500, 480, W(146, "Hastings") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    film.add(BigText("ENGLINOBARANGOI", C11_X + 1400, -1500, 460, W(151, "English") - 0.2,
                     rgb=GOLD, hit=None))
    p18 = film.add(Print("P18", C11_X + 1000, 200, 2300, rot=1.4, t_in=L(153) + 0.1,
                         label="NORMAN KNIGHTS & CAVALRY", label_t=W(153, "enemies")))
    film.add(BigText("DYRRACHIUM 1081", C11_X + 200, 1750, 480, W(153, "Dyrrhachium") - 0.2,
                     rgb=CREAM, hit=None))
    film.add(Stamp("INFERNO", C11_X + 600, 750, size=340, rot=-10, t_in=L(159) + 0.2))

    cam(L(143) + 0.3, (C10_X + C11_X) / 2, 0, 0.30, 0.0)
    cam(W(144, "Stamford"), C11_X - 1200, -300, 0.58, -0.3)
    cam(W(146, "Hastings"), C11_X - 200, -600, 0.56, 0.2)
    cam(W(151, "English"), C11_X + 1200, -500, 0.56, 0.4)
    cam(W(153, "Dyrrhachium"), C11_X + 600, 400, 0.58, -0.2)
    cam(E(159) - 0.4, C11_X + 200, 100, 0.48, 0.0)
    foc(L(144), C11_X - 1000, 0, 3200, 0.5)
    foc(W(153, "Dyrrhachium"), C11_X + 800, 200, 3200, 0.55)

    # =========================================================================
    # CLUSTER 12 (T12, Lines 160-175): 1204, Anna Komnene & Halfdan's Mark
    # =========================================================================
    cue("riser", L(160) - 1.0, 0.45, dur=1.0)
    film.add(StringLine((C11_X + 1500, -500), (C12_X - 1500, -600), t_in=L(160) + 0.1, dur=0.9, sag=0.04, width=16))
    film.add(BigText("\"A SACRED TRUST\"", C12_X - 1400, -1500, 480, W(161, "sacred") - 0.2,
                     rgb=CREAM, hit=None))
    p19 = film.add(Print("P19", C12_X - 800, 150, 2500, rot=-1.0, t_in=L(164) + 0.1,
                         label="CAPTURE OF CONSTANTINOPLE 1204 (PALMA)", label_t=L(164) + 0.3))
    film.add(BigText("1204 · FOURTH CRUSADE", C12_X + 600, -1500, 480, W(163, "Crusade") - 0.2,
                     bar=HILITE, bar_h=0.92, rgb=INK, shadow=False))
    p20 = film.add(Print("P20", C12_X + 1200, 200, 2300, rot=1.2, t_in=L(172) + 0.1,
                         label="HAGIA SOPHIA UPPER GALLERY", label_t=W(173, "gallery")))
    film.add(BigText("HALFDAN'S RUNES", C12_X + 800, 1750, 500, W(173, "mark") - 0.2,
                     rgb=GOLD, hit=None))

    cam(L(160) + 0.3, (C11_X + C12_X) / 2, 0, 0.30, 0.0)
    cam(W(161, "sacred"), C12_X - 1200, -600, 0.56, 0.3)
    cam(W(163, "Crusade"), C12_X + 200, -500, 0.58, -0.2)
    cam(L(166), C12_X - 500, 100, 0.62, 0.0)
    cam(W(173, "gallery"), C12_X + 1000, 300, 0.64, 0.4)
    cam(L(175), C12_X + 500, 100, 0.56, -0.2)

    # Grand finale: pull back to reveal the entire evidence board
    cam(film.duration, 38500, 0, 0.048, 0.0)
    foc(L(160), C12_X - 600, 0, 3200, 0.5)
    foc(W(173, "gallery"), C12_X + 900, 200, 3000, 0.55)
    foc(film.duration - 2.0, 38500, 0, 45000, 0.12)

    film.fade_in, film.fade_out = 1.0, 2.0
    return film
