# -*- coding: utf-8 -*-
"""Complément CP et CE1 — même identité que le kit du 5 novembre."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"

INK = (20, 25, 35)
GREY = (95, 100, 110)
MGREY = (176, 181, 190)
LINE = (200, 205, 214)
IND = (58, 48, 176)
IND_C = (232, 233, 250)
VERT = (22, 132, 76)
VERT_C = (231, 247, 238)
AMBRE = (176, 106, 8)
AMBRE_C = (253, 246, 228)
ROUGE = (192, 38, 44)
ROUGE_C = (253, 233, 233)
PRUNE = (146, 42, 96)
PRUNE_C = (250, 234, 242)
LM = 12
W = 186


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(False)
        self.set_margins(LM, 10, LM)

    def pied(self, txt):
        self.set_y(-9)
        self.set_font("D", "", 6.8)
        self.set_text_color(*GREY)
        self.set_x(LM)
        self.cell(150, 4, txt)
        self.set_x(LM + 150)
        self.cell(36, 4, "%d" % self.page_no(), align="R")


def entete(pdf, surtitre, titre, sous="", col=IND):
    pdf.set_fill_color(*col)
    pdf.rect(0, 0, 210, 21, style="F")
    pdf.set_xy(LM, 4)
    pdf.set_font("D", "", 7.4)
    pdf.set_text_color(232, 234, 240)
    pdf.cell(0, 4, surtitre.upper())
    pdf.set_xy(LM, 8.4)
    pdf.set_font("D", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 7, titre)
    pdf.set_y(25)
    if sous:
        pdf.set_font("D", "", 8.6)
        pdf.set_text_color(*GREY)
        pdf.set_x(LM)
        pdf.multi_cell(W, 4.6, sous, align="L")
        pdf.set_y(pdf.get_y() + 2)


def h2(pdf, txt, y=None, size=10.4, col=INK):
    pdf.set_y(y if y is not None else pdf.get_y() + 2)
    pdf.set_font("D", "B", size)
    pdf.set_text_color(*col)
    pdf.set_x(LM)
    pdf.cell(0, 5.6, txt)
    pdf.set_y(pdf.get_y() + 6.6)


def para(pdf, txt, size=8.9, lh=4.7, color=INK):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, a, b=None, size=8.9, lh=4.7):
    """puce(txt) ou puce(titre_gras, txt)."""
    if b is None:
        head, txt = None, a
    else:
        head, txt = a, b
    pdf.set_x(LM + 1)
    pdf.set_text_color(*INK)
    if head:
        pdf.set_font("D", "B", size)
        pdf.write(lh, "\u2022  " + head + "  ")
        pdf.set_font("D", "", size)
        pdf.write(lh, txt)
    else:
        pdf.set_font("D", "", size)
        pdf.write(lh, "\u2022  " + txt)
    pdf.ln(lh + 1.2)
    pdf.set_x(LM)


def scene(pdf, n, txt, y):
    pdf.set_fill_color(*IND)
    pdf.ellipse(LM, y + 0.4, 5.4, 5.4, style="F")
    pdf.set_font("D", "B", 7.6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, y + 1.1)
    pdf.cell(5.4, 4, str(n), align="C")
    pdf.set_xy(LM + 8, y)
    pdf.set_font("D", "", 9.2)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W - 8, 4.8, txt, align="L")
    return pdf.get_y() + 1.4


def bloc(pdf, titre, lignes, y, size=8.6, fill=None, bord=LINE):
    hh = 6.4
    for l in lignes:
        hh += 4.6 * max(1, len(l) // 95 + (1 if len(l) % 95 else 0))
    hh += 2
    if fill:
        pdf.set_fill_color(*fill)
        pdf.rect(LM, y, W, hh, style="DF")
    else:
        pdf.set_draw_color(*bord)
        pdf.set_line_width(0.35)
        pdf.rect(LM, y, W, hh)
    pdf.set_xy(LM + 2.5, y + 2)
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*INK)
    pdf.cell(0, 4.4, titre)
    yy = y + 7.4
    pdf.set_font("D", "", size)
    for l in lignes:
        pdf.set_xy(LM + 2.5, yy)
        pdf.multi_cell(W - 5, 4.6, l, align="L")
        yy = pdf.get_y()
    return y + hh


PDF_CP = [
    (1, "Lina joue seule dans un coin de la cour. Personne ne vient la chercher."),
    (2, "Deux enfants rient très fort parce que Tom est tombé devant tout le monde."),
    (3, "Chaque jour, on cache le cartable de Sacha, et tout le monde rit."),
    (4, "Anaïs prête son crayon à son voisin qui n’en a pas."),
    (5, "Un grand arrache le goûter d’un petit et le mange devant lui. Tous les jours."),
    (6, "Deux enfants veulent le même ballon et se fâchent. Puis ils jouent ensemble."),
    (7, "Depuis la rentrée, on appelle toujours Youssouf par un surnom qu’il n’aime pas."),
    (8, "Un enfant dit à un autre : « viens jouer avec nous »."),
]

PDF_CE1 = [
    (1, "Deux élèves se disputent la place à la fenêtre. Chacun cède un jour.", "Conflit"),
    (2, "Chaque récréation, on empêche Mia de jouer au ballon.", "Harcèlement"),
    (3, "Un élève se moque une fois de la coiffure de son voisin.", "Moquerie"),
    (4, "Un élève frappe un autre parce qu’il a perdu au foot.", "Violence"),
    (5, "Depuis un mois, trois élèves se moquent du prénom de Yanis.", "Harcèlement"),
    (6, "Un élève rit quand son camarade se trompe au tableau. Une seule fois.", "Moquerie"),
    (7, "Deux amis ne sont pas d’accord sur le jeu. Ils tirent au sort.", "Conflit"),
    (8, "Des élèves coincent une fille contre le mur et tirent ses cheveux.", "Violence"),
]

COMPTINE = ["Un mot qui pique,", "un mot qui pique,", "je le dis à ma maîtresse.",
            "Un mot qui fait du bien,", "un mot qui fait du bien,", "je le dis à mon copain.",
            "Et si ça recommence,", "si c’est tous les jours,", "je le dis encore,",
            "et ça s’arrête."]

pdf = PDF()

# ================ 1. CP — FICHE ANIMATEUR ================
pdf.add_page()
entete(pdf, "CP · fiche animateur", "Ça fait mal, ou pas ?",
       "Objectif : reconnaître ce qui fait mal, et savoir à qui le dire. Durée : 45 minutes. "
       "Aucun matériel à préparer, aucune lecture pour les élèves.", AMBRE)

h2(pdf, "Déroulé", 40)
etapes = [
    ("5 min — Le cadre", "« Aujourd’hui, toute l’école parle de ça : les choses qui font mal. On ne va "
     "pas raconter ce qui nous est arrivé. On va apprendre à reconnaître. »"),
    ("15 min — Pouce en l’air, pouce en bas", "Les élèves écoutent une scène, puis montrent le pouce en "
     "l’air si « ça va » et le pouce en bas si « ça ne va pas ». Lire les huit scènes sans commenter. "
     "Noter au tableau les deux ou trois qui divisent la classe : ce sont celles sur lesquelles on revient."),
    ("10 min — Les trois mots qui changent tout", "Écrire au tableau : TOUS LES JOURS · EXPRÈS · "
     "TOUJOURS LE MÊME. Reprendre la scène 2 et la scène 3 : ce sont les mêmes gestes, mais l’un arrive "
     "une fois et l’autre tous les jours. C’est cela qui fait mal."),
    ("10 min — La forêt de mains", "Chacun trace sa main, écrit STOP au feutre (ou le fait écrire), "
     "colorie et découpe. Toutes les mains sont collées sur une grande feuille : le STOP de la classe. "
     "C’est la trace à rendre."),
    ("5 min — À qui on le dit", "Nommer à voix haute les trois adultes de l’école, et faire répéter : "
     "« je le dis à… ». Puis la phrase de la classe : « si c’est tous les jours, je le dis. »"),
]
y = 47
for t, d in etapes:
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*AMBRE)
    pdf.set_xy(LM, y)
    pdf.cell(0, 5, t)
    y += 5.4
    pdf.set_y(y)
    pdf.set_font("D", "", 8.7)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.multi_cell(W, 4.6, d, align="L")
    y = pdf.get_y() + 2.2

h2(pdf, "Les huit scènes à lire à voix haute", y + 2)
y = pdf.get_y() - 2
for n, txt in PDF_CP:
    y = scene(pdf, n, txt, y)

bloc(pdf, "Ce qu’il faut attendre — pour l’enseignant", [
    "Scènes 3, 5 et 7 : c’est tous les jours, c’est fait exprès, c’est toujours le même. Ce sont celles "
    "qui doivent être dites à un adulte.",
    "Scènes 1 et 2 : ça fait de la peine, mais ce n’est pas tous les jours. La bonne réponse n’est pas "
    "la punition, c’est le geste : on va la chercher, on l’invite.",
    "Scènes 4 et 8 : c’est bien. On les garde pour ne pas terminer sur le négatif.",
    "Scène 6 : c’est une dispute. Ça se règle, ça ne se signale pas."],
    y + 1)

pdf.pied("Kit du 5 novembre · CP · fiche animateur")

# ================ 2. CP — CARTES A DECOUPER ================
pdf.add_page()
entete(pdf, "CP · supports à découper", "Les cartes « ça va » / « ça ne va pas »",
       "Une page donne six paires de cartes : pour une classe de 25, l’imprimer quatre fois. "
       "Si l’on préfère ne rien imprimer, l’activité se fait au pouce : en l’air ou en bas.", AMBRE)

y0 = 40
w = (W - 8) / 2
for i in range(6):
    for j, (col, colc, signe) in enumerate([(VERT, VERT_C, "check"), (ROUGE, ROUGE_C, "cross")]):
        x = LM + j * (w + 8)
        y = y0 + i * 40
        pdf.set_fill_color(*colc)
        pdf.set_draw_color(*col)
        pdf.set_line_width(0.7)
        pdf.set_dash_pattern(dash=1.6, gap=1.6)
        pdf.rect(x, y, w, 36, style="DF")
        pdf.set_dash_pattern()
        # rond + signe
        cx, cy, r = x + w / 2, y + 15, 8.5
        pdf.set_draw_color(*col)
        pdf.set_line_width(1.6)
        pdf.ellipse(cx - r, cy - r, r * 2, r * 2)
        if signe == "check":
            pdf.line(cx - 4.2, cy, cx - 1.2, cy + 3.4)
            pdf.line(cx - 1.2, cy + 3.4, cx + 4.4, cy - 3.6)
        else:
            pdf.line(cx - 4, cy - 4, cx + 4, cy + 4)
            pdf.line(cx - 4, cy + 4, cx + 4, cy - 4)
        pdf.set_font("D", "B", 12)
        pdf.set_text_color(*col)
        pdf.set_xy(x, y + 25)
        pdf.cell(w, 6, "ÇA VA" if signe == "check" else "ÇA NE VA PAS", align="C")

pdf.pied("Kit du 5 novembre · CP · cartes à découper")

# ================ 3. CE1 — FICHE ANIMATEUR ================
pdf.add_page()
entete(pdf, "CE1 · fiche animateur", "Les quatre images et les trois rôles",
       "Objectif : trier des situations, puis faire agir celui qui regarde. Durée : 50 minutes. "
       "Les quatre couleurs sont les mêmes que celles des CE2 : toute l’école utilise le même code.", VERT)

h2(pdf, "Déroulé", 40)
etapes = [
    ("5 min — Le cadre", "« On va trier des situations. Aucune n’est arrivée à quelqu’un de la classe : "
     "elles sont inventées. On parle des choses, pas des personnes. »"),
    ("15 min — Le tri", "Afficher les quatre images au tableau. Lire les huit situations. Chaque groupe "
     "pose une gommette sous l’image qui convient. Mise en commun : deux situations au moins se discutent."),
    ("10 min — Les trois rôles", "Écrire au tableau : celui qui est embêté · celui qui embête · celui qui "
     "regarde. Question : « lequel des trois peut arrêter la scène le plus vite ? » Réponse attendue : "
     "celui qui regarde, parce qu’il est plusieurs."),
    ("15 min — La scène à rejouer", "Trois enfants portent les cartes-rôles (page suivante). Le maître "
     "joue la scène 2 en trente secondes. Puis un autre enfant prend la carte « celui qui regarde » et "
     "rejoue : la classe cherche ce qui change la scène."),
    ("5 min — La comptine", "Apprendre la comptine à gestes (page suivante) et la réciter ensemble. "
     "Elle sera dite devant les autres classes à la fin de la journée."),
]
y = 47
for t, d in etapes:
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*VERT)
    pdf.set_xy(LM, y)
    pdf.cell(0, 5, t)
    y += 5.4
    pdf.set_y(y)
    pdf.set_font("D", "", 8.7)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.multi_cell(W, 4.6, d, align="L")
    y = pdf.get_y() + 2.2

h2(pdf, "Les huit situations à lire, et la bonne image", y + 2)
y = pdf.get_y() - 1
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.6)
pdf.set_fill_color(IND_C)
pdf.cell(8, 6, "N°", border=1, fill=True, align="C")
pdf.cell(0, 6, "La situation", border=1, fill=True)
pdf.cell(26, 6, "Image", border=1, fill=True, align="C")
pdf.set_y(pdf.get_y() + 6)
for n, txt, rep in PDF_CE1:
    yy = pdf.get_y()
    pdf.set_font("D", "B", 8)
    pdf.set_x(LM)
    pdf.cell(8, 9.6, str(n), border=1, align="C")
    pdf.set_font("D", "", 8.3)
    pdf.set_xy(LM + 8, yy + 1.4)
    pdf.multi_cell(W - 34, 4.4, txt, align="L")
    pdf.set_xy(LM + W - 26, yy)
    pdf.set_draw_color(*LINE)
    pdf.rect(LM + W - 26, yy, 26, 9.6)
    pdf.set_font("D", "B", 7.6)
    pdf.set_xy(LM + W - 25, yy + 2.8)
    pdf.cell(24, 4, rep.upper(), align="C")
    pdf.set_y(yy + 9.6)

bloc(pdf, "Le point à ne pas manquer", [
    "Les situations 2 et 5 sont celles qui doivent être dites à un adulte. Les situations 3 et 6 "
    "blessent aussi, mais on n’en fait pas la même chose : on en parle, on ne convoque pas.",
    "Si un élève dit « ça m’arrive », on ne rebondit pas devant la classe. On note, et on le prend à "
    "part dans les cinq minutes."],
    pdf.get_y() + 3)

pdf.pied("Kit du 5 novembre · CE1 · fiche animateur")

# ================ 4. CE1 — LES 4 IMAGES ================
pdf.add_page()
entete(pdf, "CE1 · supports", "Les quatre images du tri",
       "À afficher au tableau, ou à poser au sol. Les couleurs sont celles utilisées par toute l’école.", VERT)
ent = [("1", "ON SE DISPUTE", "Deux personnes de force égale. Ça s’arrête, ça se règle.", VERT, VERT_C),
       ("2", "ON SE MOQUE", "Une fois. Ça blesse, mais ça ne se répète pas.", AMBRE, AMBRE_C),
       ("3", "ON EMBÊTE TOUS LES JOURS", "Ça se répète, c’est fait exprès, et c’est toujours le même.", ROUGE, ROUGE_C),
       ("4", "ON FAIT MAL", "On touche au corps. Même une fois, c’est grave.", PRUNE, PRUNE_C)]
w = (W - 6) / 2
for i, (num, titre, defi, col, colc) in enumerate(ent):
    x = LM + (i % 2) * (w + 6)
    y = 44 + (i // 2) * 78
    pdf.set_fill_color(*colc)
    pdf.set_draw_color(*col)
    pdf.set_line_width(1.1)
    pdf.rect(x, y, w, 72, style="DF")
    pdf.set_font("D", "B", 26)
    pdf.set_text_color(*col)
    pdf.set_xy(x + 5, y + 4)
    pdf.cell(0, 11, num)
    pdf.set_xy(x + 5, y + 19)
    pdf.set_font("D", "B", 14)
    pdf.multi_cell(w - 10, 6.2, titre, align="L")
    pdf.set_xy(x + 5, y + 44)
    pdf.set_font("D", "", 9.4)
    pdf.set_text_color(*INK)
    pdf.multi_cell(w - 10, 5.2, defi, align="L")
pdf.pied("Kit du 5 novembre · CE1 · les quatre images")

# ================ 5. CE1 — CARTES-ROLES ET COMPTINE ================
pdf.add_page()
entete(pdf, "CE1 · supports", "Les trois cartes-rôles et la comptine",
       "Découper les trois cartes, les accrocher avec une ficelle autour du cou. Elles servent à jouer, "
       "pas à désigner quelqu’un.", VERT)

w3 = (W - 8) / 3
roles = [("CELUI QUI EST EMBÊTÉ", VERT, VERT_C), ("CELUI QUI EMBÊTE", ROUGE, ROUGE_C),
         ("CELUI QUI REGARDE", AMBRE, AMBRE_C)]
for i, (txt, col, colc) in enumerate(roles):
    x = LM + i * (w3 + 4)
    y = 42
    pdf.set_fill_color(*colc)
    pdf.set_draw_color(*col)
    pdf.set_line_width(0.8)
    pdf.set_dash_pattern(dash=1.6, gap=1.6)
    pdf.rect(x, y, w3, 46, style="DF")
    pdf.set_dash_pattern()
    pdf.set_font("D", "B", 9.6)
    pdf.set_text_color(*col)
    pdf.set_xy(x + 2, y + 6)
    pdf.multi_cell(w3 - 4, 5.2, txt, align="C")
    pdf.set_font("D", "", 7.6)
    pdf.set_text_color(*INK)
    pdf.set_xy(x + 2, y + 26)
    pdf.multi_cell(w3 - 4, 4.4, "Je porte cette carte pour jouer la scène.", align="C")
    # trou pour la ficelle
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.4)
    pdf.circle(x + w3 / 2, y + 4, 1.4)

h2(pdf, "La comptine à gestes", 100)
para(pdf, "Un geste par ligne : la main qui pique (doigts tendus), la main sur le cœur (le bien), la main "
          "qui se pose (ça s’arrête).", size=8.4, color=GREY)
y = pdf.get_y() + 3
pdf.set_fill_color(*VERT_C)
pdf.rect(LM, y, W, 96, style="F")
yy = y + 8
for i, l in enumerate(COMPTINE):
    pdf.set_xy(LM, yy)
    pdf.set_font("D", "B" if i in (0, 3, 6) else "", 13)
    pdf.set_text_color(*(VERT if i in (0, 3, 6) else INK))
    pdf.cell(W, 8.2, l, align="C")
    yy += 8.4
pdf.pied("Kit du 5 novembre · CE1 · cartes-rôles et comptine")

# ================ 6. ORGANISATION A 15 CLASSES ================
pdf.add_page()
entete(pdf, "Personne ressource", "Organiser la journée à quinze classes",
       "Quatre CP, quatre CE1, deux CE2, trois CM1, un CM2, un CM1/CM2 : environ 375 élèves. "
       "Ce qui change par rapport à un dispositif à sept classes.")

h2(pdf, "Qui fait quoi", 40)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.6)
pdf.set_fill_color(IND_C)
pdf.cell(24, 7, "Niveau", border=1, fill=True)
pdf.cell(14, 7, "Nb", border=1, fill=True, align="C")
pdf.cell(72, 7, "Ce que fait la classe", border=1, fill=True)
pdf.cell(0, 7, "Durée", border=1, fill=True)
pdf.set_y(pdf.get_y() + 7)
lignes = [("CP", "4", "Ça fait mal ou pas ? + forêt de mains", "45 min"),
          ("CE1", "4", "Les quatre images + les trois rôles + la comptine", "50 min"),
          ("CE2", "2", "Les 4 visages + feuille froissée + affiche", "45 min"),
          ("CM1", "3", "Thermomètre + plan du témoin + mur des mots", "45 min"),
          ("CM2", "1", "Débat mouvant + théâtre-forum + ambassadeurs", "50 min"),
          ("CM1/CM2", "1", "Menu CM2", "50 min"),
          ("CE2 à CM2", "7", "Puis le questionnaire officiel, sur papier", "30 min")]
for a, b, c, d in lignes:
    yy = pdf.get_y()
    pdf.set_font("D", "B", 8)
    pdf.set_x(LM)
    pdf.cell(24, 7, a, border=1)
    pdf.cell(14, 7, b, border=1, align="C")
    pdf.set_font("D", "", 7.8)
    pdf.cell(72, 7, c, border=1)
    pdf.cell(0, 7, d, border=1, align="C")
    pdf.set_y(yy + 7)

h2(pdf, "Les trois points de vigilance d’une journée à quinze classes")
puce(pdf, "Le bruit et les circulations.",
     "Quinze classes qui changent de salle en même temps, dans des couloirs étroits, c’est le premier "
     "risque de la journée. Faire circuler un seul niveau à la fois, et garder les CP dans leur classe.")
puce(pdf, "Les grands et les petits dans la même cour.",
     "Une journée où toute l’école parle de harcèlement est aussi une journée où les grands croisent les "
     "petits plus longtemps que d’habitude. Renforcer la présence adulte aux récréations ce jour-là, sans "
     "en faire une annonce.")
puce(pdf, "Une seule parole publique.",
     "À quinze classes, il y aura forcément une ou deux confidences. Prévoir un adulte disponible et un "
     "lieu pour écouter, sinon les élèves parleront dans le couloir.")

h2(pdf, "Le rituel de 10 h — ce qui fait tenir les quinze classes ensemble")
for t in ["La même lecture courte dans toutes les classes, à la même heure : cinq lignes, lues par le "
          "maître, pas par un élève.",
          "Chaque classe choisit trois mots et les écrit sur une bande de papier. Les quinze bandes sont "
          "accrochées ensemble dans le hall : c’est le mur de l’école, et il est fait de quinze classes.",
          "Les CP et CE1 récitent leur comptine pendant que les autres accrochent : c’est le seul moment "
          "où toute l’école regarde la même chose au même moment.",
          "Une photo à 10 h 30, un seul appareil, un seul adulte. Une photo par niveau suffit pour la "
          "restitution aux familles."]:
    puce(pdf, t)

bloc(pdf, "Ce que tu ne peux pas faire seule", [
    "À quinze classes, la personne ressource ne peut pas animer. Elle prépare les quinze enveloppes, "
    "présente vingt minutes en conseil des maîtres, et circule le jour J.",
    "Ce qui décide de la réussite, ce n’est pas la qualité de l’activité : c’est que chaque professeur "
    "ait, sur son bureau, une fiche qui tient debout toute seule. C’est le seul objectif du kit."],
    pdf.get_y() + 3, fill=(248, 249, 252))

pdf.pied("Kit du 5 novembre · organisation à quinze classes")

out = "/workspace/nah/kit-cycle-2.pdf"
pdf.output(out)
print("cycle 2:", os.path.getsize(out), "octets,", pdf.page_no(), "pages")
