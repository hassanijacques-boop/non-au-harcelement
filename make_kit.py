# -*- coding: utf-8 -*-
"""Kit « Journée du 5 novembre » — supports imprimables, CE2 à CM2."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"

INK = (20, 25, 35)
GREY = (95, 100, 110)
LGREY = (232, 234, 238)
MGREY = (176, 181, 190)
LINE = (200, 205, 214)
LM = 12
W = 186          # largeur utile (210 - 24)


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


def entete(pdf, surtitre, titre, sous=""):
    pdf.set_fill_color(*INK)
    pdf.rect(0, 0, 210, 21, style="F")
    pdf.set_xy(LM, 4)
    pdf.set_font("D", "", 7.4)
    pdf.set_text_color(230, 232, 236)
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


def h2(pdf, txt, y=None, size=10.4):
    if y is not None:
        pdf.set_y(y)
    else:
        pdf.set_y(pdf.get_y() + 2)
    pdf.set_font("D", "B", size)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.cell(0, 5.6, txt)
    pdf.set_y(pdf.get_y() + 6.6)


def para(pdf, txt, size=8.8, lh=4.7, color=INK, w=W):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(w, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, txt, size=8.8, lh=4.66):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    pdf.set_x(LM + 1)
    pdf.multi_cell(W - 1, lh, "\u2022  " + txt, align="L")
    pdf.set_x(LM)


def bloc(pdf, titre, lignes, y, size=8.6, w=W, x=None, h=None, fill=None):
    x = LM if x is None else x
    hh = 6.4
    for l in lignes:
        hh += 4.6 * max(1, len(l) // int(w / 1.95) + (1 if len(l) % int(w / 1.95) else 0))
    hh += 1.8
    if fill:
        pdf.set_fill_color(*fill)
        pdf.rect(x, y, w, hh, style="DF")
    else:
        pdf.set_draw_color(*LINE)
        pdf.set_line_width(0.35)
        pdf.rect(x, y, w, hh)
    pdf.set_xy(x + 2.5, y + 2)
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*INK)
    pdf.cell(0, 4.4, titre)
    yy = y + 7.4
    pdf.set_font("D", "", size)
    for l in lignes:
        pdf.set_xy(x + 2.5, yy)
        pdf.multi_cell(w - 5, 4.6, l, align="L")
        yy = pdf.get_y()
    return y + hh


# ---------------------------------------------------------------- cartes
def carte(pdf, x, y, w, h, num, texte, taille=8.6, gras=False):
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.4)
    pdf.set_dash_pattern(dash=1.4, gap=1.4)
    pdf.rect(x, y, w, h)
    pdf.set_dash_pattern()
    pdf.set_fill_color(*INK)
    pdf.ellipse(x + 3.5, y + 3.5, 7, 7, style="F")
    pdf.set_font("D", "B", 8.2)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(x + 3.5, y + 4.7)
    pdf.cell(7, 4, str(num), align="C")
    pdf.set_xy(x + 12.5, y + 4.6)
    pdf.set_font("D", "B" if gras else "", taille)
    pdf.set_text_color(*INK)
    pdf.multi_cell(w - 16, 4.6, texte, align="L")


def grille(pdf, liste, y0, cols=2, h=53, marges=3):
    w = (W - marges) / cols
    for i, (num, txt) in enumerate(liste):
        cx = LM + (i % cols) * (w + marges)
        cy = y0 + (i // cols) * (h + 2.2)
        carte(pdf, cx, cy, w, h, num, txt)


# ---------------------------------------------------------------- contenu
CARTES = [
    (1, "Deux élèves veulent le même ballon à la récréation. Ils se disputent, crient, puis se séparent fâchés."),
    (2, "Nadia dit à Halima qu’elle triche au jeu. Halima répond qu’elle ment. Elles ne se parlent plus pendant deux jours, puis elles se réconcilient."),
    (3, "Dans le couloir, un élève bouscule un plus petit par accident. Il s’excuse tout de suite et l’aide à ramasser ses affaires."),
    (4, "Deux amis ne sont pas d’accord : l’un veut jouer au foot, l’autre au ballon prisonnier. Ils finissent par tirer au sort."),
    (5, "Un élève rit de la nouvelle coiffure d’un camarade, une seule fois, et arrête quand l’autre dit que ça le blesse."),
    (6, "Un élève se trompe au tableau. Un autre fait un bruit avec sa bouche pour faire rire. Une seule fois."),
    (7, "Un élève imite l’accent d’un camarade pour faire rire la classe. Il le fait une fois, ce jour-là."),
    (8, "Depuis un mois, trois élèves répètent chaque jour le prénom d’Anli en le déformant, et toute la classe rit."),
    (9, "Chaque midi à la cantine, on enlève la chaise de la même élève. Tout le monde rit. Cela fait trois semaines."),
    (10, "Chaque soir, dans le groupe de classe, plusieurs élèves envoient des messages méchants à un élève. Cela dure depuis la rentrée."),
    (11, "Quand Salim s’approche du jeu, les autres partent vers un autre coin de la cour. Tous les jours depuis deux mois."),
    (12, "Un élève de CM2 prend chaque jour le goûter d’un CE2 et le menace s’il en parle à quelqu’un."),
    (13, "Un élève frappe un camarade au visage parce qu’il a perdu au foot. C’est la première fois."),
    (14, "Des élèves coincent une fille contre le mur du préau et tirent ses cheveux pour l’empêcher de partir."),
    (15, "Des élèves baissent le pantalon d’un camarade de force, devant les autres, pendant la récréation."),
    (16, "Un élève prend une photo d’un autre aux toilettes et la montre à la classe sur son téléphone."),
]

CORRECTION = [
    ("1, 2, 3, 4", "CONFLIT", "Désaccord entre deux personnes de force égale. Ça s’arrête, ça se règle, ça peut même se réconcilier."),
    ("5, 6, 7", "MOQUERIE", "Une atteinte isolée, qui blesse, mais qui ne se répète pas et ne vise pas à écraser l’autre."),
    ("8, 9, 10, 11, 12", "HARCÈLEMENT", "Trois signes réunis : ça se répète, c’est fait exprès pour faire mal, et l’un est plus fort que l’autre (nombre, âge, taille, popularité)."),
    ("13, 14, 15, 16", "VIOLENCE", "Atteinte au corps ou à l’intimité. Même une seule fois, ce n’est pas du conflit : c’est grave, et un adulte doit le savoir."),
]

THERMO = [
    (1, "Yanis rate son exercice. Amine rit et dit « t’es nul » une fois."),
    (2, "Depuis la rentrée, deux élèves enlèvent le bonnet de Fatima chaque matin dans la cour."),
    (3, "Deux élèves se disputent la place à côté de la fenêtre, chacun cède un jour."),
    (4, "Un groupe envoie chaque soir des messages à un élève pour se moquer de sa famille."),
    (5, "Un élève traite une fois un camarade de « sale » pendant un match, puis s’excuse."),
    (6, "Chaque récréation, un élève est applaudi quand il arrache le sac d’un autre."),
    (7, "Des élèves se moquent de l’accent d’un camarade, mais seulement quand le maître a le dos tourné."),
    (8, "Une élève refuse de prêter son stylo à sa voisine : elles se boudent jusqu’au soir."),
]

AFFIRMATIONS = [
    "« Se moquer, c’est pour rire : celui qui se plaint n’a pas d’humour. »",
    "« Celui qui parle à un adulte, c’est une balance. »",
    "« Si je ne dis rien et que je ne ris pas, je ne suis pas concerné. »",
    "« Un surnom, ce n’est pas grave, tout le monde en a un. »",
    "« Quand on est plusieurs, ce n’est plus pareil : ce n’est pas vraiment du harcèlement. »",
    "« Les filles et les garçons, ce n’est pas le même problème. »",
    "« Sur les réseaux, ce n’est pas l’école : ça ne la regarde pas. »",
    "« Un élève harcelé, c’est qu’il le cherche un peu. »",
]

SENES = [
    ("Saynète 1 — La cantine", "3 personnages : Samira (la victime), Moussa (l’auteur), Naïla (la témoin)", [
        "Moussa : Hé, Samira, tu manges encore ! Tu vas exploser, la baleine.",
        "Samira : Arrête…",
        "Moussa : (aux autres) Vous avez vu ? Elle parle, la baleine !",
        "Naïla : (assis à côté, baisse la tête, ne dit rien)",
        "Samira : Laisse-moi manger.",
        "Moussa : Et si je ne veux pas ? Tu vas faire quoi ?",
    ], "Ce que Naïla pourrait faire ou dire : trois solutions, à trouver avec la classe."),
    ("Saynète 2 — Le groupe de classe", "3 personnages : Zaïnaba (la victime), Anli (l’auteur), Said (le témoin, ami d’Anli)", [
        "Anli : (à Said) Regarde ce qu’elle a mis aujourd’hui. J’envoie une photo au groupe.",
        "Zaïnaba : Non, s’il te plaît, ne l’envoie pas.",
        "Anli : Trop tard. (Il envoie.)",
        "Said : (rit, puis regarde Zaïnaba qui pleure) …",
        "Anli : Ce n’est rien, on rigole.",
    ], "Ce que Said, qui est l’ami d’Anli, pourrait faire : trois solutions, à trouver avec la classe."),
    ("Saynète 3 — La cour", "3 personnages : Halima (la victime), Youssouf (l’auteur), Naïla (la témoin)", [
        "Youssouf : (attrape le ballon de Halima) C’est mon ballon maintenant.",
        "Halima : Rends-le, c’est le mien !",
        "Youssouf : Si tu le veux, viens le chercher. (Il le lance à un autre élève.)",
        "Halima : (reste seule au milieu de la cour)",
        "Naïla : (voit la scène depuis le banc)",
    ], "Ce que Naïla pourrait faire : trois solutions, et à qui elle peut s’adresser."),
]

QUIZ = [
    ("Quel est le numéro gratuit contre le harcèlement ?", "3018"),
    ("Ce numéro est-il payant ?", "Non, l’appel est gratuit."),
    ("Peut-on appeler sans donner son nom ?", "Oui, l’appel est anonyme et confidentiel."),
    ("À quelles heures peut-on appeler ?", "7 jours sur 7, de 9 h à 23 h."),
    ("Qui répond au téléphone ?", "Des psychologues, des juristes et des spécialistes du numérique."),
    ("Cite deux adultes de l’école à qui tu peux parler.", "À compléter avec les noms de l’école."),
    ("Que peut-on faire sur l’application 3018 ?", "Échanger avec un professionnel, stocker des preuves, s’auto-évaluer, lire des conseils."),
    ("Si tu vois un élève harcelé, que peux-tu faire en premier ?", "Ne pas rire, ne pas filmer, aller le voir, et prévenir un adulte."),
]

pdf = PDF()

# ==================== 1. MODE D'EMPLOI DU KIT ====================
pdf.add_page()
pdf.set_fill_color(*INK)
pdf.rect(0, 0, 210, 34, style="F")
pdf.set_xy(LM, 8)
pdf.set_font("D", "B", 19)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 9, "Kit « Journée du 5 novembre »")
pdf.set_xy(LM, 18)
pdf.set_font("D", "", 9.4)
pdf.cell(0, 5, "Journée nationale de lutte contre le harcèlement · CE2, CM1, CM2 · école élémentaire")
pdf.set_xy(LM, 23.6)
pdf.set_font("D", "", 8.4)
pdf.cell(0, 5, "Sept classes · un menu par niveau · supports à découper · fiches animateur")

h2(pdf, "Comment fonctionne ce kit", 40)
para(pdf, "Chaque classe reçoit une enveloppe : la fiche animateur de son niveau, les supports à découper et "
          "les fiches élèves. Aucune préparation à la maison, aucun matériel à acheter, aucun compte rendu "
          "à écrire. Le collègue suit la fiche, coche ce qu’il a fait, et remet la trace produite.")
pdf.set_y(pdf.get_y() + 1)

h2(pdf, "Le menu par niveau")
y = pdf.get_y() - 1
y = bloc(pdf, "CE2  —  comprendre ce que c’est (45 min)", [
    "1. Les 4 visages : trier 16 cartes en 4 familles (conflit, moquerie, harcèlement, violence).",
    "2. La feuille froissée : les traces que laissent les mots.",
    "3. L’affiche de la classe."], y)
y = bloc(pdf, "CM1  —  mesurer et agir (45 min)", [
    "1. Le thermomètre : les 3 signes du harcèlement (répétition, intention, rapport de force).",
    "2. Le plan du témoin : ce que je peux dire, à qui, et ce que je ne fais pas.",
    "3. Le mur des mots qui réparent."], y + 3)
y = bloc(pdf, "CM2 et CM1/CM2  —  argumenter et s’entraîner (50 min)", [
    "1. Débat mouvant : 8 affirmations à départager.",
    "2. Théâtre-forum : 3 saynètes, un joker, la classe cherche des solutions.",
    "3. Désignation de 2 élèves ambassadeurs."], y + 3)

h2(pdf, "La trame des deux heures")
y = pdf.get_y() - 1
lignes = [
    ("0 à 10 min", "Rituel commun à toute l’école : la même lecture, les trois mots choisis par la classe."),
    ("10 à 40 min", "Activité 1 du niveau (nommer ou mesurer)."),
    ("40 à 50 min", "Activité 2 (ressentir, agir, ou débat)."),
    ("50 à 55 min", "Retour au calme. On range, on annonce le questionnaire."),
    ("55 à 85 min", "Le questionnaire papier. Calme, silence, la mention au dos est lue."),
    ("85 à 110 min", "Activité 3 : la trace (affiche, mur, mains)."),
    ("110 à 120 min", "Clôture : ce qu’on retient, les noms des adultes, le 3018."),
]
for t, d in lignes:
    pdf.set_font("D", "B", 8.4)
    pdf.set_x(LM)
    pdf.cell(26, 4.9, t)
    pdf.set_font("D", "", 8.6)
    pdf.multi_cell(W - 26, 4.9, d, align="L")
    pdf.set_x(LM)

h2(pdf, "Les six règles d’or", pdf.get_y() + 5)
for r in ["On ne fait jamais témoigner un élève sur sa propre situation, même s’il lève la main.",
          "On ne joue jamais une scène réellement vécue : les saynètes sont inventées.",
          "On n’utilise jamais le prénom d’un élève de l’école dans une mise en situation.",
          "On ne part pas en chasse au harceleur : on parle des actes, pas des personnes.",
          "On termine toujours par ce qu’on peut faire et par les noms des adultes.",
          "Une boîte aux mots s’ouvre chaque semaine, sinon on ne l’installe pas."]:
    puce(pdf, r)

bloc(pdf, "Ce que fait la personne ressource, en dehors de sa classe", [
    "Avant : 20 minutes de présentation en conseil des maîtres, et sept enveloppes préparées.",
    "Le jour même : elle circule, elle ne remplace personne, elle prend trois photos et elle récupère "
    "les traces produites.",
    "Après : elle rassemble les affiches et le mur, et écrit les cinq lignes du bilan pour le rapport "
    "d’établissement."], pdf.get_y() + 5)

pdf.pied("Kit Journée du 5 novembre · école élémentaire · à distribuer un exemplaire par classe")

# ==================== 2. CE2 — FICHE ANIMATEUR ====================
pdf.add_page()
entete(pdf, "CE2 · fiche animateur", "Les 4 visages du harcèlement",
       "Objectif : que les élèves sachent faire la différence entre un conflit, une moquerie, du harcèlement "
       "et une violence. Durée : 45 minutes, avant le questionnaire.")

h2(pdf, "Déroulé", 42)
for i, (t, d) in enumerate([
    ("5 min — Annoncer", "« Aujourd’hui, toute l’école parle de ça. On va apprendre à reconnaître quatre "
     "choses différentes, parce que ce n’est pas la même chose de se disputer et d’être harcelé. »"),
    ("10 min — Trier", "Poser les 4 en-têtes sur la table. Distribuer les 16 cartes. Par groupes de 4, les "
     "élèves placent chaque carte sous un en-tête. Ils doivent pouvoir dire pourquoi."),
    ("15 min — Mettre en commun", "Reprendre les cartes une par une. La classe se met d’accord. Écrire au "
     "tableau ce qui fait basculer une carte dans une autre famille."),
    ("10 min — Le critère décisif", "Écrire les trois signes du harcèlement : ça se répète · c’est fait "
     "exprès pour faire mal · l’un est plus fort que l’autre. Reprendre les cartes 8 à 12 avec ces trois "
     "signes."),
    ("5 min — Afficher", "Coller le tableau de la classe (4 colonnes) sur le mur. C’est la trace à rendre."),
]):
    pdf.set_font("D", "B", 8.8)
    pdf.set_x(LM)
    pdf.cell(0, 5, t)
    pdf.set_y(pdf.get_y() + 5)
    para(pdf, d, size=8.6)
    pdf.set_y(pdf.get_y() + 1.4)

h2(pdf, "Correction des 16 cartes", pdf.get_y() + 1)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.8)
pdf.set_fill_color(*LGREY)
pdf.cell(26, 6, "Cartes", border=1, fill=True)
pdf.cell(30, 6, "Famille", border=1, fill=True)
pdf.cell(0, 6, "Pourquoi", border=1, fill=True)
pdf.set_y(pdf.get_y() + 6)
for nums, fam, rap in CORRECTION:
    yy = pdf.get_y()
    pdf.set_font("D", "B", 8)
    pdf.set_x(LM)
    pdf.cell(26, 12, nums, border=1)
    pdf.cell(30, 12, fam, border=1)
    pdf.set_font("D", "", 7.9)
    pdf.set_xy(LM + 56, yy + 1.4)
    pdf.multi_cell(W - 56, 4.4, rap, align="L")
    pdf.set_y(yy + 12)

h2(pdf, "Les trois cas limites — à traiter avec la classe", pdf.get_y() + 2)
for t in ["Carte 7 : imiter l’accent, une fois, c’est une moquerie. La même chose tous les jours devient du "
          "harcèlement. C’est la répétition qui change la nature du fait.",
          "Carte 3 : un accident n’est pas une violence. Ce qui compte, c’est l’intention et ce qui se passe "
          "après.",
          "Carte 5 et 6 : rire une fois blesse quand même. On peut dire « c’était une moquerie » sans dire "
          "« ce n’était rien »."]:
    puce(pdf, t)

bloc(pdf, "La phrase à retenir, écrite au tableau", [
    "« Une fois, c’est une moquerie. Tous les jours, c’est du harcèlement. Et quand le plus fort s’en prend "
    "toujours au même plus petit, ce n’est jamais un jeu. »"], pdf.get_y() + 3)

pdf.pied("Kit Journée du 5 novembre · CE2 · fiche animateur")

# ==================== 3-4. CE2 — CARTES ====================
pdf.add_page()
entete(pdf, "CE2 · supports à découper", "Les 16 situations",
       "Découper sur les pointillés. Prévoir un jeu par groupe de 4 élèves (soit 6 jeux par classe de 25).")
grille(pdf, CARTES[:8], 42)
pdf.pied("Kit Journée du 5 novembre · CE2 · cartes 1 à 8")

pdf.add_page()
entete(pdf, "CE2 · supports à découper", "Les 16 situations (suite)",
       "Découper sur les pointillés.")
grille(pdf, CARTES[8:], 42)
pdf.pied("Kit Journée du 5 novembre · CE2 · cartes 9 à 16")

# ==================== 5. CE2 — EN-TETES ====================
pdf.add_page()
entete(pdf, "CE2 · supports à découper", "Les 4 familles",
       "Découper ces quatre en-têtes et les poser sur la table : les élèves y placent les cartes.")
ent = [("1", "CONFLIT", "Deux personnes de force égale. Ça s’arrête, ça se règle."),
       ("2", "MOQUERIE", "Une atteinte isolée. Ça blesse, mais ça ne se répète pas."),
       ("3", "HARCÈLEMENT", "Ça se répète. C’est fait exprès. L’un est plus fort que l’autre."),
       ("4", "VIOLENCE", "On touche au corps ou à l’intimité. Même une fois, c’est grave.")]
w = (W - 6) / 2
for i, (num, titre, defi) in enumerate(ent):
    x = LM + (i % 2) * (w + 6)
    y = 44 + (i // 2) * 78
    pdf.set_draw_color(*INK)
    pdf.set_line_width(1.1)
    pdf.rect(x, y, w, 72)
    pdf.set_font("D", "B", 30)
    pdf.set_text_color(*LINE)
    pdf.set_xy(x + 4, y + 3)
    pdf.cell(0, 12, num)
    pdf.set_xy(x + 4, y + 20)
    pdf.set_font("D", "B", 16)
    pdf.set_text_color(*INK)
    pdf.cell(0, 8, titre)
    pdf.set_xy(x + 4, y + 32)
    pdf.set_font("D", "", 9.4)
    pdf.multi_cell(w - 8, 5.2, defi, align="L")

pdf.set_y(215)
h2(pdf, "Pendant le tri, trois questions à poser", 208)
for q in ["Est-ce que c’est arrivé une seule fois, ou plusieurs fois ?",
          "Est-ce que celui qui le fait veut faire mal, ou est-ce qu’il ne s’en rend pas compte ?",
          "Est-ce que l’un des deux peut arrêter quand il veut, ou est-ce qu’il est coincé ?"]:
    puce(pdf, q, size=9.2)

pdf.pied("Kit Journée du 5 novembre · CE2 · les 4 familles")

# ==================== 6. CM1 — FICHE ANIMATEUR ====================
pdf.add_page()
entete(pdf, "CM1 · fiche animateur", "Le thermomètre et le plan du témoin",
       "Objectif : donner aux élèves un outil pour mesurer une situation, et un plan d’action quand ils sont "
       "témoins. Durée : 45 minutes.")

h2(pdf, "Partie 1 — Le thermomètre (20 min)", 42)
para(pdf, "Distribuer la fiche élève (page suivante). Les élèves lisent les 8 situations et cochent, pour "
          "chacune, les trois cases : est-ce que ça se répète ? est-ce que c’est fait exprès pour faire mal ? "
          "est-ce qu’il y a un plus fort et un plus faible ?")
pdf.set_y(pdf.get_y() + 1.5)
para(pdf, "Règle du jeu : ce n’est pas la gravité qui décide, c’est le nombre de cases cochées. Zéro case : "
          "c’est un conflit. Une seule : c’est une moquerie ou un accident. Les trois : c’est du harcèlement.")
pdf.set_y(pdf.get_y() + 1.5)

h2(pdf, "Correction du thermomètre")
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.6)
pdf.set_fill_color(*LGREY)
pdf.cell(10, 6, "N°", border=1, fill=True)
pdf.cell(0, 6, "Réponse attendue", border=1, fill=True)
pdf.set_y(pdf.get_y() + 6)
corr = [("1", "Moquerie : une fois, pas de rapport de force."),
        ("2", "Harcèlement : répété tous les jours, deux contre un."),
        ("3", "Conflit : force égale, chacun cède un jour, ça se règle."),
        ("4", "Harcèlement : répété, fait pour nuire, le groupe est plus fort."),
        ("5", "Moquerie : une fois, avec des excuses ensuite."),
        ("6", "Harcèlement : répété, applaudissements = le groupe soutient l’auteur."),
        ("7", "Harcèlement : la répétition et le fait de se cacher le prouvent."),
        ("8", "Conflit : ponctuel, entre égaux, sans volonté de faire mal.")]
for n, r in corr:
    yy = pdf.get_y()
    pdf.set_font("D", "B", 8)
    pdf.set_x(LM)
    pdf.cell(10, 6.4, n, border=1, align="C")
    pdf.set_font("D", "", 8.2)
    pdf.set_xy(LM + 10, yy)
    pdf.multi_cell(W - 10, 6.4, r, align="L", border=0)
    pdf.set_y(yy + 6.6)

h2(pdf, "Partie 2 — Le plan du témoin (25 min)", pdf.get_y() + 2)
para(pdf, "C’est la partie la plus utile de la journée : la plupart des élèves sont témoins, jamais victimes "
          "ni auteurs. On travaille donc le rôle du témoin, en trois colonnes, sur la fiche élève.")
pdf.set_y(pdf.get_y() + 1.5)
for t in ["Ce que je peux dire : trois phrases courtes, que l’élève s’entraîne à prononcer à voix haute. "
          "« Arrête. » « Ça ne me fait pas rire. » « Viens, on va voir la maîtresse. »",
          "À qui je peux le dire : deux adultes de l’école (noms écrits sur la fiche), un camarade de "
          "confiance, et le 3018.",
          "Ce que je ne fais pas : rire, filmer, répéter ce qui a été dit, ou rester à côté sans rien faire "
          "en faisant semblant de ne pas voir."]:
    puce(pdf, t)

bloc(pdf, "À faire jouer, pas seulement écrire", [
    "Faire répéter les trois phrases à voix haute, en binôme, deux minutes. Un témoin qui n’a jamais "
    "prononcé la phrase ne la prononcera pas dans la cour."], pdf.get_y() + 3)

pdf.pied("Kit Journée du 5 novembre · CM1 · fiche animateur")

# ==================== 7. CM1 — FICHE ELEVE THERMOMETRE ====================
pdf.add_page()
entete(pdf, "CM1 · fiche élève", "Le thermomètre du harcèlement",
       "Pour chaque situation, coche les cases. Ce n’est pas la gravité qui décide, c’est le nombre de cases cochées.")
pdf.set_y(40)
pdf.set_font("D", "B", 8.2)
pdf.set_x(LM)
pdf.cell(60, 5, "Prénom : ......................................")
pdf.cell(60, 5, "Classe : ......................")
pdf.cell(0, 5, "Date : ......../......../ 2026")

y0 = 50
pdf.set_fill_color(*INK)
pdf.set_text_color(255, 255, 255)
pdf.set_font("D", "B", 7.6)
pdf.set_xy(LM, y0)
pdf.cell(9, 11, "N°", border=1, fill=True, align="C")
pdf.cell(108, 11, "La situation", border=1, fill=True, align="C")
pdf.cell(23, 11, "Ça se répète ?", border=1, fill=True, align="C")
pdf.cell(23, 11, "Fait exprès ?", border=1, fill=True, align="C")
pdf.cell(23, 11, "Un plus fort ?", border=1, fill=True, align="C")
yy = y0 + 11
pdf.set_text_color(*INK)
for n, s in THERMO:
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.35)
    pdf.rect(LM, yy, 9, 17)
    pdf.set_font("D", "B", 8.6)
    pdf.set_text_color(*INK)
    pdf.set_xy(LM, yy + 6.3)
    pdf.cell(9, 4, str(n), align="C")
    pdf.rect(LM + 9, yy, 108, 17)
    pdf.set_font("D", "", 8.5)
    pdf.set_xy(LM + 11, yy + 3.6)
    pdf.multi_cell(104, 4.4, s, align="L")
    for k in range(3):
        cx = LM + 9 + 108 + k * 23
        pdf.set_draw_color(*MGREY)
        pdf.set_line_width(0.35)
        pdf.rect(cx, yy, 23, 17)
        pdf.set_draw_color(150, 155, 165)
        pdf.set_line_width(0.4)
        pdf.rect(cx + 8.2, yy + 5.2, 6.6, 6.6)
    yy += 17

pdf.set_y(yy + 6)
pdf.set_font("D", "B", 9.2)
pdf.set_x(LM)
pdf.cell(0, 5, "Mon verdict pour chaque situation :")
pdf.set_y(yy + 12)
for i in range(8):
    pass
pdf.set_font("D", "", 8.6)
for i, (n, _) in enumerate(THERMO):
    xx = LM + (i % 4) * 46
    if i % 4 == 0 and i:
        pdf.set_y(pdf.get_y() + 6)
    pdf.set_x(xx)
    pdf.cell(46, 6, "%d : .................." % n)
pdf.set_y(pdf.get_y() + 8)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*GREY)
pdf.multi_cell(W, 4.6, "À écrire à la place des pointillés : C (conflit), M (moquerie), H (harcèlement) ou V (violence).",
               align="L")
bloc(pdf, "Les trois signes du harcèlement — à recopier au dos de cette fiche", [
    "1. Ça se répète : ce n’est pas une fois, c’est tous les jours ou presque.",
    "2. C’est fait exprès pour faire mal, et celui qui le fait le sait.",
    "3. L’un est plus fort que l’autre : plus nombreux, plus grand, plus âgé, plus écouté dans la classe."],
    pdf.get_y() + 6)
pdf.pied("Kit Journée du 5 novembre · CM1 · fiche élève thermomètre")

# ==================== 8. CM1/CM2 — PLAN DU TEMOIN ====================
pdf.add_page()
entete(pdf, "CM1 / CM2 · fiche élève", "Mon plan du témoin",
       "La plupart du temps, on n’est ni la victime ni l’auteur : on est le témoin. Voici ce que je peux faire.")

def zone(pdf, titre, consigne, y, h, nlig=3):
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.8)
    pdf.rect(LM, y, W, h)
    pdf.set_xy(LM + 3, y + 2.4)
    pdf.set_font("D", "B", 10.2)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5.4, titre)
    pdf.set_x(LM + 3)
    pdf.set_y(y + 8.8)
    pdf.set_font("D", "", 8.2)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(W - 6, 4.4, consigne, align="L")
    ytop = pdf.get_y() + 3.5
    pdf.set_text_color(*INK)
    if nlig:
        bas = y + h - 6
        pas = (bas - ytop) / nlig
        pdf.set_draw_color(*MGREY)
        pdf.set_line_width(0.3)
        for i in range(nlig):
            ly = ytop + pas * (i + 0.72)
            pdf.line(LM + 4, ly, LM + W - 4, ly)

y = 40
zone(pdf, "1. Ce que je peux dire",
     "Trois phrases courtes, à répéter à voix haute jusqu’à les dire sans hésiter.", y, 50, 3)
zone(pdf, "2. À qui je peux le dire",
     "Deux adultes de l’école, un camarade de confiance, et le 3018.", y + 54, 50, 3)
z3 = y + 108
pdf.set_draw_color(*INK)
pdf.set_line_width(0.8)
pdf.rect(LM, z3, W, 46)
pdf.set_xy(LM + 3, z3 + 2.4)
pdf.set_font("D", "B", 10.2)
pdf.cell(0, 5.4, "3. Ce que je ne fais pas")
pdf.set_xy(LM + 3, z3 + 8.8)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*GREY)
pdf.cell(0, 4.4, "Coche ce que tu t’engages à ne plus faire quand tu es témoin.")
items = ["Rire avec les autres", "Filmer ou prendre en photo",
         "Répéter ce qui a été dit", "Faire semblant de ne pas voir"]
for i, it in enumerate(items):
    bx = LM + 5 + (i % 2) * 88
    by = z3 + 17 + (i // 2) * 10
    pdf.set_draw_color(140, 145, 155)
    pdf.set_line_width(0.4)
    pdf.rect(bx, by, 5.4, 5.4)
    pdf.set_xy(bx + 8, by - 0.8)
    pdf.set_font("D", "", 9)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5.6, it)

pdf.set_y(z3 + 52)
pdf.set_font("D", "B", 9.4)
pdf.set_x(LM)
pdf.cell(0, 5.4, "Le numéro à connaître : 3018 — gratuit, anonyme, 7 jours sur 7 de 9 h à 23 h.")

y = z3 + 62
y = bloc(pdf, "Pourquoi cette fiche sert vraiment", [
    "Un témoin qui n’a jamais prononcé la phrase ne la prononcera pas dans la cour. C’est pour cela qu’on "
    "fait répéter à voix haute, en binôme, les trois phrases écrites dans le cadre 1.",
    "Garder la fiche dans le cahier : elle resservira toute l’année, et c’est la trace de la séance."], y)
pdf.pied("Kit Journée du 5 novembre · CM1 / CM2 · plan du témoin")

# ==================== 9. CM2 — DEBAT MOUVANT ====================
pdf.add_page()
entete(pdf, "CM2 · fiche animateur", "Le débat mouvant",
       "Objectif : faire argumenter les élèves sur leurs représentations, avant le questionnaire. Durée : 25 minutes.")

h2(pdf, "Organisation", 42)
for t in ["Placer deux affiches aux deux extrémités de la classe : D’ACCORD et PAS D’ACCORD. Le milieu de la "
          "pièce est la zone « je ne sais pas ».",
          "Lire une affirmation. Chaque élève se place là où il se sent. On ne commente pas encore.",
          "Donner la parole à un élève de chaque côté. Puis demander : « quelqu’un a changé d’avis ? » et "
          "laisser les élèves se déplacer.",
          "Ne jamais dire qui a raison. Le but n’est pas la bonne réponse, c’est d’entendre les arguments et "
          "de voir que d’autres pensent autrement."]:
    puce(pdf, t)

h2(pdf, "Les règles à annoncer avant de commencer")
for t in ["On argumente, on n’insulte pas, et on parle de l’idée, pas de la personne.",
          "Chacun parle une fois par affirmation.",
          "On a le droit de changer d’avis : c’est même le but.",
          "Ce qui se dit ici ne sort pas de la classe avec des noms."]:
    puce(pdf, t)

h2(pdf, "Les 8 affirmations, et ce qu’il faut attendre")
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.6)
pdf.set_fill_color(*LGREY)
pdf.cell(10, 6, "N°", border=1, fill=True)
pdf.cell(88, 6, "Affirmation", border=1, fill=True)
pdf.cell(0, 6, "Ce qu’on cherche à faire dire", border=1, fill=True)
pdf.set_y(pdf.get_y() + 6)
reperes = [
    ("1", "« Se moquer, c’est pour rire »", "La différence entre l’intention de celui qui rit et l’effet sur celui qui reçoit."),
    ("2", "« Celui qui parle est une balance »", "Le courage de parler, et ce que protège le silence."),
    ("3", "« Si je ne dis rien, je ne suis pas concerné »", "Le rôle du témoin : ne rien faire, c’est déjà laisser faire."),
    ("4", "« Un surnom, ce n’est pas grave »", "La répétition et l’usure ; ce n’est pas le mot seul qui blesse, c’est le tous les jours."),
    ("5", "« À plusieurs, ce n’est pas du harcèlement »", "Le groupe aggrave : le rapport de force devient écrasant."),
    ("6", "« Filles et garçons, ce n’est pas le même problème »", "Les stéréotypes, et le fait que les garçons parlent moins."),
    ("7", "« Sur les réseaux, ce n’est pas l’école »", "Le harcèlement suit l’élève jusqu’à sa chambre ; le cadre légal."),
    ("8", "« Il le cherche un peu »", "Le renversement de responsabilité : la victime n’est jamais responsable."),
]
for n, a, r in reperes:
    yy = pdf.get_y()
    pdf.set_font("D", "B", 8)
    pdf.set_x(LM)
    pdf.cell(10, 13, n, border=1, align="C")
    pdf.set_font("D", "", 8)
    pdf.set_xy(LM + 10, yy + 1.2)
    pdf.multi_cell(88, 4.4, a, align="L")
    pdf.set_xy(LM + 98, yy + 1.2)
    pdf.multi_cell(W - 98, 4.4, r, align="L")
    pdf.set_y(yy + 13)

bloc(pdf, "Le piège à éviter", [
    "Si le débat part sur un élève de la classe, on arrête : « on ne parle pas des personnes, on parle des "
    "idées ». C’est la seule règle non négociable de l’exercice."], pdf.get_y() + 3)
pdf.pied("Kit Journée du 5 novembre · CM2 · débat mouvant, fiche animateur")

# ==================== 10. CM2 — AFFIRMATIONS A AFFICHER ====================
pdf.add_page()
entete(pdf, "CM2 · supports", "Les 8 affirmations",
       "À découper et à afficher (ou à tenir) : une affirmation à la fois, deux affiches D’ACCORD / PAS D’ACCORD aux extrémités.")
w2 = (W - 5) / 2
for i, a in enumerate(AFFIRMATIONS):
    x = LM + (i % 2) * (w2 + 5)
    y = 40 + (i // 2) * 51
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.4)
    pdf.set_dash_pattern(dash=1.4, gap=1.4)
    pdf.rect(x, y, w2, 44)
    pdf.set_dash_pattern()
    pdf.set_font("D", "B", 8)
    pdf.set_text_color(*LGREY)
    pdf.set_xy(x + 4, y + 3)
    pdf.cell(0, 5, "%d" % (i + 1))
    pdf.set_xy(x + 5, y + 11)
    pdf.set_font("D", "B", 11.4)
    pdf.set_text_color(*INK)
    pdf.multi_cell(w2 - 10, 6.4, a, align="L")

# deux affiches A4 paysage réduites en bas de page
for j, (txt, x) in enumerate([("D’ACCORD", LM), ("PAS D’ACCORD", LM + w2 + 5)]):
    pdf.set_draw_color(*INK)
    pdf.set_line_width(1.2)
    pdf.rect(x, 250, w2, 22)
    pdf.set_font("D", "B", 15)
    pdf.set_text_color(*INK)
    pdf.set_xy(x, 256.5)
    pdf.cell(w2, 8, txt, align="C")
pdf.pied("Kit Journée du 5 novembre · CM2 · affirmations du débat mouvant")

# ==================== 11. CM2 — THEATRE-FORUM ====================
pdf.add_page()
entete(pdf, "CM2 · fiche animateur", "Théâtre-forum : trois saynètes",
       "Objectif : s’entraîner à réagir. Les scènes sont inventées : aucune ne doit ressembler à ce qu’un élève a vécu.")
para(pdf, "Trois élèves jouent la scène une première fois, jusqu’au bout. Puis le maître (le « joker ») "
          "arrête : « qui veut prendre la place de la témoin et essayer autre chose ? » On rejoue. La classe "
          "cherche, on ne juge pas. À la fin, on écrit au tableau les solutions qui marchent.")
pdf.set_y(pdf.get_y() + 2)
for titre, roles, dial, question in SENES:
    y = pdf.get_y()
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.6)
    pdf.rect(LM, y, W, 68 if len(dial) > 5 else 60)
    pdf.set_xy(LM + 3, y + 2.4)
    pdf.set_font("D", "B", 9.6)
    pdf.cell(0, 5, titre)
    pdf.set_xy(LM + 3, y + 8)
    pdf.set_font("D", "", 7.8)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 4.2, roles)
    yy = y + 13
    pdf.set_text_color(*INK)
    for l in dial:
        pdf.set_xy(LM + 4, yy)
        pdf.set_font("D", "", 8.2)
        pdf.multi_cell(W - 8, 4.4, l, align="L")
        yy = pdf.get_y() + 0.6
    pdf.set_xy(LM + 4, yy + 0.6)
    pdf.set_font("D", "B", 8.2)
    pdf.multi_cell(W - 8, 4.4, question, align="L")
    pdf.set_y(y + (70 if len(dial) > 5 else 62))
pdf.pied("Kit Journée du 5 novembre · CM2 · théâtre-forum, saynètes")

# ==================== 12. CM2 — REGLES DU JOKER ====================
pdf.add_page()
entete(pdf, "CM2 · animateur et observateurs", "Les règles du jeu et la grille d’observation",
       "À lire à la classe avant la première saynète. Le joker, c’est l’adulte : il arrête, il relance, il ne juge pas.")

h2(pdf, "Les quatre règles du théâtre-forum", 42)
for i, t in enumerate([
    "On joue des scènes inventées. On ne joue jamais une scène que quelqu’un a vraiment vécue.",
    "On ne joue pas son propre rôle : celui qui a été témoin dans la vraie vie peut jouer l’auteur.",
    "Le joker frappe dans ses mains : la scène s’arrête. Un élève remplace un personnage et on rejoue.",
    "On ne cherche pas le coupable : on cherche ce qui pourrait changer la situation."]):
    pdf.set_fill_color(*INK)
    pdf.ellipse(LM, pdf.get_y() + 0.4, 6.4, 6.4, style="F")
    pdf.set_font("D", "B", 8.6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, pdf.get_y() + 1.3)
    pdf.cell(6.4, 4, str(i + 1), align="C")
    pdf.set_xy(LM + 9.5, pdf.get_y())
    pdf.set_text_color(*INK)
    pdf.set_font("D", "", 8.8)
    pdf.multi_cell(W - 9.5, 4.9, t, align="L")
    pdf.set_y(pdf.get_y() + 2.2)

h2(pdf, "Grille d’observation — un élève observe, une saynète à la fois", pdf.get_y() + 2)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 7.6)
pdf.set_fill_color(*LGREY)
pdf.set_x(LM)
pdf.cell(0, 6.4, "Ce que fait le témoin", border=1, fill=True)
pdf.set_y(pdf.get_y() + 6.4)
lignes_obs = ["Il ne dit rien et détourne le regard", "Il rit avec les autres",
              "Il filme ou prend en photo", "Il va chercher un adulte",
              "Il dit une phrase pour arrêter", "Il parle à la victime après",
              "Il prévient un camarade", "Il répète ce qu’il a vu à d’autres"]
for l in lignes_obs:
    pdf.set_x(LM)
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.35)
    pdf.set_font("D", "", 8.8)
    pdf.cell(W - 46, 8.6, l, border=1)
    pdf.set_x(LM + W - 46)
    pdf.set_font("D", "B", 8)
    pdf.cell(23, 8.6, "Vu ?", border=1, align="C")
    pdf.cell(23, 8.6, "Efficace ?", border=1, align="C")
    pdf.set_y(pdf.get_y() + 8.6)

pdf.set_y(pdf.get_y() + 4)
bloc(pdf, "La question à poser à la fin", [
    "« Parmi tout ce qu’on a essayé, qu’est-ce qui a vraiment changé la scène ? » Écrire les réponses au "
    "tableau, et n’en garder que trois : ce sont les trois choses que la classe s’engage à faire."],
    pdf.get_y())
pdf.pied("Kit Journée du 5 novembre · CM2 · théâtre-forum, règles et observation")

# ==================== 13. COMMUN — FEUILLE FROISSEE + SAC A DOS ====================
pdf.add_page()
entete(pdf, "Tous niveaux · fiche élève", "La feuille froissée et le sac à dos invisible",
       "Deux activités courtes, sans matériel, à faire juste avant le questionnaire.")

h2(pdf, "1. La feuille froissée  (10 minutes)", 42)
for t in ["Chaque élève prend une feuille. Il la froisse le plus fort possible, en boule.",
          "Le maître demande : « maintenant, lissez-la parfaitement, comme avant. »",
          "C’est impossible : les plis restent. Même avec beaucoup de bonne volonté.",
          "La phrase à dire : « une parole qui blesse laisse une trace qu’on ne peut pas effacer, même quand "
          "on s’excuse. C’est pour ça qu’on ne peut pas dire : c’était pour rire. »"]:
    puce(pdf, t, size=9)

h2(pdf, "2. Le sac à dos invisible  (20 minutes)", pdf.get_y() + 2)
para(pdf, "Chaque élève dessine un élève de dos, avec un sac à dos, et écrit dans le sac ce qu’un enfant "
          "porte en arrivant à l’école quand il est embêté : une boule au ventre, peur de la récré, "
          "personne à qui parler, mal dormir, honte…", size=9)
pdf.set_y(pdf.get_y() + 2)

y = pdf.get_y() + 2
pdf.set_draw_color(*INK)
pdf.set_line_width(0.9)
pdf.rect(LM, y, W, 128)
pdf.set_xy(LM + 4, y + 3)
pdf.set_font("D", "", 8)
pdf.set_text_color(*GREY)
pdf.cell(0, 4.4, "Dessine ici. Une seule règle : on ne dessine personne de la classe.")
pdf.set_dash_pattern(dash=2, gap=2)
pdf.set_draw_color(*MGREY)
pdf.set_line_width(0.3)
for i in range(1, 9):
    pdf.line(LM + 6, y + 14 + i * 13, LM + W - 6, y + 14 + i * 13)
pdf.set_dash_pattern()
pdf.set_y(y + 132)
pdf.set_x(LM)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*GREY)
pdf.multi_cell(W, 4.6, "Puis, par deux, chacun montre son sac sans expliquer : l’autre doit deviner ce qui "
                       "pèse le plus. Mettre en commun ce que la classe a trouvé, et l’écrire au tableau.", align="L")
pdf.pied("Kit Journée du 5 novembre · tous niveaux · feuille froissée et sac à dos")

# ==================== 14. COMMUN — BANDELETTES ====================
pdf.add_page()
entete(pdf, "Tous niveaux · supports à découper", "« Si un jour ça m’arrive, je peux le dire à… »",
       "Une bandelette par élève. À remplir, puis à coller côte à côte pour former le mur des alliés.")
w1 = W
for i in range(8):
    y = 36 + i * 28
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.4)
    pdf.set_dash_pattern(dash=1.4, gap=1.4)
    pdf.rect(LM, y, w1, 25)
    pdf.set_dash_pattern()
    pdf.set_xy(LM + 4, y + 3.4)
    pdf.set_font("D", "B", 9.4)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5, "Si un jour ça m’arrive, je peux le dire à")
    pdf.set_xy(LM + 4, y + 12)
    pdf.set_font("D", "", 8.6)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 5, "Nom : ....................................................     Classe : ..................")
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.3)
    pdf.line(LM + 100, y + 19, LM + W - 6, y + 19)
pdf.pied("Kit Journée du 5 novembre · tous niveaux · bandelettes du mur des alliés")

# ==================== 15. COMMUN — AFFICHE DE CLASSE ====================
pdf.add_page()
pdf.set_draw_color(*INK)
pdf.set_line_width(1.3)
pdf.rect(10, 8, 190, 281)
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.5)
pdf.rect(14, 12, 182, 273)
pdf.set_xy(20, 22)
pdf.set_font("D", "B", 26)
pdf.set_text_color(*INK)
pdf.cell(0, 12, "DANS NOTRE CLASSE")
pdf.set_xy(20, 36)
pdf.set_font("D", "B", 34)
pdf.cell(0, 15, "on ne rit pas")
pdf.set_xy(20, 52)
pdf.cell(0, 15, "de quelqu’un.")
pdf.set_xy(20, 74)
pdf.set_font("D", "", 11)
pdf.set_text_color(*GREY)
pdf.cell(0, 6, "Affiche à compléter par les élèves : slogan, dessins, signatures.")
# cadre dessin
pdf.set_draw_color(*MGREY)
pdf.set_line_width(0.4)
pdf.set_dash_pattern(dash=2, gap=2)
pdf.rect(20, 88, 170, 150)
pdf.set_dash_pattern()
pdf.set_xy(24, 90)
pdf.set_font("D", "", 8)
pdf.set_text_color(*MGREY)
pdf.cell(0, 5, "espace pour le dessin de la classe")
# signatures
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.3)
for i in range(4):
    pdf.line(24, 252 + i * 7, 186, 252 + i * 7)
pdf.set_xy(20, 244)
pdf.set_font("D", "", 8)
pdf.set_text_color(*GREY)
pdf.cell(0, 5, "Les signatures de la classe :")

# ==================== 16. COMMUN — MUR, BOITE, QUIZ ====================
pdf.add_page()
entete(pdf, "Tous niveaux · supports", "Le mur des mots, la boîte aux mots, le quiz 3018",
       "Trois supports pour la trace collective et pour la mémoire du numéro.")

h2(pdf, "Le mur des mots qui réparent", 42)
para(pdf, "À coller en haut du rouleau de papier installé dans le couloir. Chaque classe y ajoute ses cinq "
          "mots après la récréation.", size=8.6)
y = pdf.get_y() + 2
pdf.set_fill_color(*INK)
pdf.rect(LM, y, W, 26, style="F")
pdf.set_font("D", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(LM, y + 6)
pdf.cell(W, 8, "LES MOTS QU’ON VEUT ENTENDRE ICI", align="C")
pdf.set_xy(LM, y + 15)
pdf.set_font("D", "", 8.4)
pdf.cell(W, 5, "mur de l’école · journée du 5 novembre 2026", align="C")

h2(pdf, "L’étiquette de la boîte aux mots", pdf.get_y() + 22)
para(pdf, "À coller sur une boîte à chaussures fermée, avec une fente sur le couvercle. À ouvrir une fois "
          "par semaine, et à répondre — sinon ne pas l’installer.", size=8.6)
y = pdf.get_y() + 2
pdf.set_draw_color(*INK)
pdf.set_line_width(0.9)
pdf.rect(LM, y, W, 34)
pdf.set_xy(LM + 4, y + 4)
pdf.set_font("D", "B", 13)
pdf.cell(0, 7, "BOÎTE AUX MOTS")
pdf.set_xy(LM + 4, y + 13)
pdf.set_font("D", "", 9)
pdf.cell(0, 5, "J’écris ce que je n’arrive pas à dire à voix haute. Je peux signer, ou pas.")
pdf.set_xy(LM + 4, y + 20)
pdf.set_font("D", "", 8.4)
pdf.set_text_color(*GREY)
pdf.cell(0, 5, "Ouverte chaque semaine par le maître ou la maîtresse · si c’est grave, un adulte doit le savoir.")

h2(pdf, "Le quiz 3018 — 8 questions, à poser à l’oral", pdf.get_y() + 38)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "", 8.5)
for q, r in QUIZ:
    pdf.set_x(LM)
    pdf.set_font("D", "B", 8.4)
    pdf.multi_cell(W - 4, 4.6, "•  " + q, align="L")
    pdf.set_x(LM + 6)
    pdf.set_font("D", "", 8.1)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(W - 8, 4.4, "Réponse : " + r, align="L")
    pdf.set_text_color(*INK)
    pdf.set_y(pdf.get_y() + 0.8)
pdf.pied("Kit Journée du 5 novembre · mur des mots, boîte aux mots, quiz 3018")

# ==================== 17. FICHE ADULTE ====================
pdf.add_page()
entete(pdf, "Pour l’adulte · à garder", "Les pièges et les contacts",
       "Une page à ne pas distribuer aux élèves : elle reste avec la fiche animateur, dans l’enveloppe.")

h2(pdf, "Les six pièges, pendant et après la séance", 42)
pieges = [
    ("Faire témoigner un élève", "Même s’il lève la main. On l’écoute après, seul, et on l’oriente vers un "
     "adulte. Jamais devant la classe."),
    ("Jouer une scène vécue", "Le théâtre-forum ne fonctionne que si les rôles ne collent pas aux personnes."),
    ("Partir en chasse au harceleur", "Désigner un coupable collectif renforce le groupe contre un bouc "
     "émissaire. On parle des actes."),
    ("Installer une boîte qu’on n’ouvre pas", "Un élève qui écrit sans réponse apprend que parler ne sert à "
     "rien. Si personne ne peut la relever, ne pas la mettre."),
    ("Terminer sur le négatif", "Chaque activité finit par ce qu’on peut faire, et par les noms des adultes."),
    ("Annoncer « il y a du harcèlement chez nous » sans données", "On attend les résultats du questionnaire "
     "pour parler chiffres. D’ici là, on parle des faits, pas de l’ampleur."),
]
for t, d in pieges:
    pdf.set_x(LM)
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W, 4.8, "•  " + t, align="L")
    pdf.set_x(LM + 6)
    pdf.set_font("D", "", 8.3)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(W - 8, 4.5, d, align="L")
    pdf.set_text_color(*INK)
    pdf.set_y(pdf.get_y() + 0.8)

h2(pdf, "Si un élève se confie pendant la séance", pdf.get_y() + 3)
for t in ["On ne promet pas le secret. On dit : « je ne peux pas garder ça pour moi, mais je vais t’aider, "
          "et je te dirai à qui je parle. »",
          "On note les faits : qui, quoi, quand, combien de fois, qui a vu. Sans interpréter.",
          "On transmet le jour même au directeur, qui décide de la suite (protocole national).",
          "On ne confronte jamais l’élève à l’auteur dans l’heure qui suit une confidence."]:
    puce(pdf, t, size=8.6)

h2(pdf, "Les contacts de l’école — à compléter avant la distribution", pdf.get_y() + 3)
y = pdf.get_y()
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.35)
for lab in ["Référent harcèlement (personne ressource) :", "Directeur / directrice :",
            "Psychologue scolaire :", "Infirmière scolaire :", "RASED :"]:
    pdf.set_x(LM)
    pdf.set_font("D", "", 8.8)
    pdf.cell(78, 7.4, lab)
    pdf.set_draw_color(*MGREY)
    pdf.line(LM + 78, pdf.get_y() + 6.2, LM + W, pdf.get_y() + 6.2)
    pdf.set_y(pdf.get_y() + 9)

pdf.set_y(pdf.get_y() + 3)
pdf.set_font("D", "B", 9.4)
pdf.set_x(LM)
pdf.cell(0, 5.4, "3018   ·   gratuit, anonyme, confidentiel   ·   7 jours sur 7, de 9 h à 23 h")

bloc(pdf, "Quatre signes qui doivent alerter, même quand l’élève ne dit rien", [
    "Il ne veut plus venir à l’école, ou il a mal au ventre et à la tête le matin, avant de partir.",
    "Il change de chemin, il évite un endroit précis : la cantine, les toilettes, un coin de la cour.",
    "Il décroche, il s’isole, il devient irritable, ou il passe d’un extrême à l’autre dans ses résultats.",
    "Ses affaires disparaissent, reviennent abîmées, ou il demande de l’argent sans explication."],
    pdf.get_y() + 6)
pdf.pied("Kit Journée du 5 novembre · fiche adulte : pièges et contacts")

pdf.output("/workspace/nah/kit-journee-5-novembre.pdf")
print("kit:", os.path.getsize("/workspace/nah/kit-journee-5-novembre.pdf"), "octets,", pdf.page_no(), "pages")
