# -*- coding: utf-8 -*-
"""Protocole de passation papier + saisie — application « Non au harcèlement »."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
SH = "/workspace/nah"
URL = "https://hassanijacques-boop.github.io/non-au-harcelement/"
VERSION = "20261027-7"

IND = (67, 56, 202)
IND_L = (238, 242, 255)
INK = (15, 23, 42)
GREY = (90, 100, 120)
ROUGE = (190, 30, 30)
ORANGE = (165, 72, 5)
VERT = (18, 130, 65)
LINE = (222, 227, 238)
LM = 18
W = 174


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(True, margin=17)
        self.set_margins(LM, 15, LM)

    def footer(self):
        self.set_y(-12)
        self.set_font("D", "", 7.2)
        self.set_text_color(*GREY)
        self.cell(0, 6, "Non au harcèlement — protocole papier et saisie · " + URL + " · v" + VERSION)
        self.set_y(-12)
        self.cell(0, 6, "page %d" % self.page_no(), align="R")


def bandeau(pdf, titre, sous1, sous2, h=34):
    pdf.set_fill_color(*IND)
    pdf.rect(0, 0, 210, h, style="F")
    pdf.set_xy(LM, 7.5)
    pdf.set_font("D", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 9, titre)
    pdf.set_xy(LM, 17)
    pdf.set_font("D", "", 9.4)
    pdf.cell(0, 5, sous1)
    if sous2:
        pdf.set_xy(LM, 22.5)
        pdf.set_font("D", "", 8.3)
        pdf.multi_cell(174, 4.6, sous2, align="L")
    pdf.set_y(h + 6)


def h1(pdf, txt, y=None):
    if y:
        pdf.set_y(y)
    else:
        pdf.ln(0.5)
    pdf.set_font("D", "B", 14.5)
    pdf.set_text_color(*IND)
    pdf.set_x(LM)
    pdf.multi_cell(W, 7.6, txt, align="L")
    pdf.set_x(LM)
    pdf.ln(1.6)


def h2(pdf, txt, color=INK, avant=2.4):
    if pdf.get_y() > 248:
        pdf.add_page()
    pdf.ln(avant)
    pdf.set_font("D", "B", 10.6)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, 6.0, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)
    pdf.ln(0.9)


def para(pdf, txt, size=9.2, color=INK, lh=5.15):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, titre, txt, color=IND, size=9.1):
    if pdf.get_y() > 263:
        pdf.add_page()
    contenu = ("**" + titre + "** : " + txt) if titre else txt
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.multi_cell(W, 5.15, "•  " + contenu, align="L", markdown=True)
    pdf.set_x(LM)
    pdf.ln(1.15)


def num(pdf, n, titre, lignes):
    y = pdf.get_y()
    pdf.set_fill_color(*IND)
    pdf.ellipse(LM, y + 0.6, 7.2, 7.2, style="F")
    pdf.set_font("D", "B", 9.6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, y + 1.6)
    pdf.cell(7.2, 5, str(n), align="C")
    pdf.set_xy(LM + 10.5, y)
    pdf.set_text_color(*IND)
    pdf.set_font("D", "B", 10)
    pdf.cell(0, 5.4, titre)
    pdf.ln(6.4)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_x(LM + 10.5)
        pdf.set_font("D", "", 9)
        pdf.multi_cell(W - 10.5, 5.0, l, align="L")
    pdf.ln(1.5)


def encadre(pdf, titre, lignes, bg=(255, 251, 235), bord=(253, 230, 138), tc=ORANGE, size=8.8):
    pdf.ln(0.8)
    pdf.set_font("D", "", size)
    h = 8.0
    for l in lignes:
        h += 4.9 * max(1, len(l) // 92 + (1 if len(l) % 92 else 0))
    h += 2
    y0 = pdf.get_y()
    if y0 + h > 271:
        pdf.add_page()
        y0 = pdf.get_y()
    pdf.set_fill_color(*bg)
    pdf.set_draw_color(*bord)
    pdf.set_line_width(0.5)
    pdf.rect(LM, y0, W, h, style="DF")
    pdf.set_xy(LM + 3, y0 + 2.5)
    pdf.set_font("D", "B", 9.2)
    pdf.set_text_color(*tc)
    pdf.cell(0, 5, titre)
    pdf.set_xy(LM + 3, y0 + 8.4)
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_x(LM + 3)
        pdf.multi_cell(W - 6, 4.9, l, align="L")
    pdf.set_y(y0 + h + 2.6)


def tableau_croisement(pdf):
    lignes = ["0", "1 ou 2", "3 à 4", "5 ou plus"]
    cols = ["0", "1 ou 2", "3 ou 4", "5 à 7", "8 ou plus"]
    T = [["rien", "rien", "surv", "surv", "harc"],
         ["rien", "rien", "surv", "surv", "harc"],
         ["surv", "surv", "surv", "surv", "harc"],
         ["harc", "harc", "harc", "harc", "harc"]]
    COUL = {"harc": ((254, 202, 202), (150, 20, 20)),
            "surv": ((253, 230, 138), (140, 80, 10)),
            "rien": ((236, 253, 243), (20, 110, 60))}
    x0 = LM
    wl, wc, hh = 30, 22.8, 7
    pdf.set_fill_color(*IND)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("D", "B", 8.4)
    pdf.set_x(x0)
    pdf.cell(wl, hh, "Total A", border=1, fill=True, align="C")
    pdf.cell(wc * 5, hh, "Total B + Total C", border=1, fill=True, align="C")
    pdf.ln()
    pdf.set_x(x0)
    pdf.cell(wl, hh, "", border=1, fill=True)
    pdf.set_font("D", "B", 8)
    for c in cols:
        pdf.cell(wc, hh, c, border=1, fill=True, align="C")
    pdf.ln()
    for i, lab in enumerate(lignes):
        pdf.set_x(x0)
        pdf.set_fill_color(*IND_L)
        pdf.set_text_color(*INK)
        pdf.set_font("D", "", 8.4)
        pdf.cell(wl, hh, lab, border=1, fill=True, align="C")
        for j in range(5):
            st = T[i][j]
            bg, fg = COUL[st]
            pdf.set_fill_color(*bg)
            pdf.set_text_color(*fg)
            pdf.set_font("D", "B", 7.2)
            txt = "HARCÈLEMENT" if st == "harc" else ("à surveiller" if st == "surv" else "—")
            pdf.cell(wc, hh, txt, border=1, fill=True, align="C")
        pdf.ln()
    pdf.set_text_color(*INK)


def fiche_suivi(pdf):
    pdf.add_page()
    bandeau(pdf, "Fiche de suivi de la campagne",
            "À tenir par le directeur pendant toute la période de passation",
            "Une ligne par classe · cocher au fur et à mesure · l’export est la seule sauvegarde")
    pdf.set_y(44)
    pdf.set_font("D", "B", 9.4)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.cell(0, 7, "École : " + "." * 46)
    pdf.ln(9)
    pdf.set_x(LM)
    pdf.cell(0, 7, "Période de passation : du ....... / ....... / 2026  au  ....... / ....... / 2026")
    pdf.ln(12)

    cols = [("Classe", 30), ("Enseignant", 40), ("Grilles\nremplies", 22),
            ("Saisie\nfaite", 20), ("Export\n.json", 20), ("Importé\nsur le PC", 42)]
    pdf.set_fill_color(*IND)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("D", "B", 7.8)
    pdf.set_x(LM)
    for nom, w in cols:
        x, y = pdf.get_x(), pdf.get_y()
        pdf.multi_cell(w, 3.6, nom, border=1, fill=True, align="C")
        pdf.set_xy(x + w, y)
    pdf.ln(8.6)

    classes = ["CE2 A", "CE2 B", "CM1 A", "CM1 B", "CM1 C", "CM2", "CM1/CM2", "", "", ""]
    hb = 13.0
    for cl in classes:
        pdf.set_x(LM)
        pdf.set_text_color(*INK)
        pdf.set_font("D", "B", 8.6)
        pdf.cell(30, hb, cl, border=1, align="C")
        pdf.set_font("D", "", 9)
        pdf.cell(40, hb, "", border=1)
        pdf.cell(22, hb, "", border=1)
        for k in range(3):
            w = [20, 20, 42][k]
            x = pdf.get_x()
            pdf.cell(w, hb, "", border=1)
            pdf.set_draw_color(150, 155, 170)
            pdf.set_line_width(0.35)
            pdf.rect(x + w / 2 - 3.2, pdf.get_y() + hb / 2 - 3.2, 6.4, 6.4)
        pdf.ln()

    pdf.ln(3)
    pdf.set_font("D", "", 8.4)
    for txt in ["Nombre de classes ayant rendu leur saisie : ................ / 7",
                "Nombre de postes affiché par le PC dans l’onglet Données : ................",
                "Ces deux nombres doivent être identiques avant tout envoi à la circonscription.",
                "Signature du directeur : ..................................................        Date : ....... / ....... / 2026"]:
        pdf.set_x(LM)
        pdf.cell(0, 6.4, txt)
        pdf.ln(6.4)

    pdf.ln(1)
    encadre(pdf, "Rappel",
            ["Un poste dont l’historique Chrome est vidé perd ses réponses : il n’y a pas de rattrapage "
             "possible. L’export est donc à faire dès que la classe a terminé sa saisie.",
             "Les grilles papier, elles, restent la pièce de référence : elles sont conservées par l’école "
             "jusqu’à la fin de l’année scolaire."],
            bg=(254, 242, 242), bord=(254, 202, 202), tc=ROUGE)


pdf = PDF()

# ============================ PAGE 1 — L'ESSENTIEL ============================
pdf.add_page()
bandeau(pdf, "Non au harcèlement",
        "Enquête d’auto-évaluation · école élémentaire CE2-CM2 · année scolaire 2026-2027",
        "Protocole de passation sur papier et de saisie des résultats — à l’attention des professeurs, "
        "du directeur, du CPC et de l’IEN")

h1(pdf, "Le principe retenu cette année", 40)
para(pdf,
     "Les élèves remplissent la grille officielle sur papier, en classe, comme les années précédentes. "
     "Chaque enseignant recopie ensuite les résultats de sa classe dans l’application. L’application "
     "calcule les trois indices officiels, situe chaque élève dans la table de croisement, rédige "
     "l’interprétation et produit le rapport destiné à la circonscription.")
pdf.ln(1)
para(pdf, "Ce qui change : l’exploitation. Les grilles étaient remplies, mais les résultats n’étaient pas "
          "interprétés. Ici, l’interprétation est automatique, identique pour toutes les classes, et "
          "disponible le soir même.", color=IND)

h2(pdf, "Les deux étapes")
num(pdf, 1, "La passation en classe, sur papier", [
    "Le professeur présente la grille, lit la mention informative, explique les quatre modalités de "
    "réponse, puis laisse les élèves remplir. Les grilles sont ramassées par le professeur."])
num(pdf, 2, "La saisie par l’enseignant, dans l’application", [
    "Chaque enseignant recopie les réponses de sa classe, un questionnaire par écran, au clavier. "
    "Une minute environ par questionnaire, soit 25 minutes pour une classe de 25."])

h2(pdf, "Ouvrir l’application")
y0 = pdf.get_y()
pdf.set_font("D", "", 9.0)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.multi_cell(104, 5.0,
    "Sur un ordinateur ou une tablette : ouvrir Chrome, taper l’adresse ci-dessous, ou scanner le QR code. "
    "Puis, dans le menu de Chrome (trois points en haut à droite), choisir « Ajouter à l’écran d’accueil » : "
    "l’application s’installe et fonctionne ensuite sans connexion.", align="L")
pdf.ln(1.6)
pdf.set_font("D", "B", 8.9)
pdf.set_text_color(*IND)
pdf.set_x(LM)
pdf.multi_cell(104, 4.5, "hassanijacques-boop.github.io/", align="L")
pdf.set_x(LM)
pdf.multi_cell(104, 4.5, "non-au-harcelement/", align="L")
pdf.ln(0.6)
pdf.set_font("D", "", 8.1)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(104, 4.4, "Aucun compte · aucun paiement · aucune donnée envoyée sur Internet", align="L")
pdf.set_font("D", "B", 8.1)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.multi_cell(104, 4.4, "Version de référence de ce document : " + VERSION, align="L")
pdf.set_font("D", "B", 9.0)
pdf.set_text_color(*VERT)
pdf.set_x(LM)
pdf.multi_cell(104, 4.8, "Code d’accès adulte : 2026", align="L")
pdf.set_font("D", "", 7.8)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(104, 4.2, "(modifiable dans Espace adulte → Réglages)", align="L")
y1 = pdf.get_y()

pdf.image(SH + "/qr-code.png", x=141, y=y0, w=30)
pdf.set_xy(134, y0 + 31)
pdf.set_font("D", "", 6.8)
pdf.set_text_color(*GREY)
pdf.multi_cell(44, 3.8, "À scanner avec l’appareil photo", align="C")

pdf.set_y(max(y1, y0 + 41) + 2)

encadre(pdf, "Ce que fait l’application — et ce qu’elle ne fait pas",
        ["Elle ne modifie pas le protocole : la grille est remplie sur papier, en classe, comme le prévoit "
         "le guide de passation. L’application intervient après, pour l’exploitation.",
         "Elle ne modifie pas la grille : les 24 questions et les 9 questions de contexte sont recopiées à "
         "l’identique, et le calcul suit la table officielle (page 6).",
         "Elle ne remplace aucun acte professionnel : l’entretien avec l’élève, l’information des familles "
         "et le signalement relèvent des adultes.",
         "Elle n’envoie rien sur Internet : chaque poste garde ses données, et la consolidation se fait par "
         "export de fichier."],
        bg=IND_L, bord=(199, 210, 254), tc=IND)

pdf.set_y(pdf.get_y() + 3)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(W, 4.5, "Qui fait quoi : le professeur fait passer la grille dans sa classe puis saisit ses "
                      "élèves ; le directeur consolide les sept fichiers et produit le rapport ; l’IEN et le "
                      "CPC reçoivent le rapport et la synthèse (pages 2 et 6 pour la vérification).", align="L")

# ======================= PAGE 2 — LE CADRE OFFICIEL =======================
pdf.add_page()
h1(pdf, "Le cadre officiel", 18)
para(pdf, "Cette page est destinée au directeur, au CPC et à l’IEN : elle situe la démarche par rapport aux "
          "textes, et vérifie qu’elle ne s’en écarte pas.")

h2(pdf, "Textes de référence")
puce(pdf, "Grille d’auto-évaluation — version 2025", "questionnaire élève du CE2 au CM2, 24 questions "
     "graduées de 1 (jamais) à 4 (très souvent), complétées par 9 questions de contexte.")
puce(pdf, "Guide de passation — octobre 2026", "année scolaire 2026-2027 : deux heures banalisées entre "
     "le jeudi 5 novembre et le vendredi 11 décembre 2026 ; passation assurée par le professeur de la "
     "classe dans le premier degré ; exploitation par le professeur, puis partage avec le directeur.")
puce(pdf, "Objectifs officiels", "détecter les situations de harcèlement, faciliter la prévention, "
     "mobiliser l’ensemble de la communauté éducative.")

h2(pdf, "Ce qui reste inchangé, et ce qui est ajouté")
puce(pdf, "Inchangé : la passation", "les élèves remplissent la grille papier en classe, sous la "
     "responsabilité de leur professeur, pendant les deux heures banalisées. Rien n’est dématérialisé.")
puce(pdf, "Inchangé : l’instrument", "mêmes questions, même ordre, mêmes modalités de réponse, même règle "
     "de comptage, même table de croisement.")
puce(pdf, "Ajouté : l’exploitation", "la recopie des réponses dans un outil qui calcule et rédige "
     "l’interprétation, afin que les résultats soient effectivement lus et exploités — ce qui faisait "
     "défaut les années précédentes.")
puce(pdf, "Ajouté : la traçabilité", "un état des lieux chiffré, comparable d’une classe à l’autre et "
     "d’une année sur l’autre, mobilisable dans le dossier de labellisation.")

h2(pdf, "Information des élèves et des familles")
para(pdf, "Le guide prévoit que le professeur lise aux élèves la mention informative du questionnaire. "
          "Elle figure au dos de la grille : les réponses ne sont pas obligatoires, le prénom n’est pas "
          "demandé, les adultes de l’école lisent les réponses pour aider les élèves qui en ont besoin.")
para(pdf, "Destinataires, conformément à la grille : les adultes qui font passer le questionnaire, le "
          "directeur, l’IEN, les adultes chargés de résoudre les situations, les personnes désignées par "
          "le directeur, et les parents ou responsables légaux. La recopie dans l’application ne change "
          "pas cette liste : elle est faite par le professeur, pour son propre usage et celui de la "
          "direction.")

h2(pdf, "Conservation des données")
puce(pdf, "Grilles papier", "la pièce de référence. Conservées jusqu’à la fin de l’année scolaire, puis "
     "détruites dans des conditions ne permettant pas leur réutilisation.")
puce(pdf, "Grilles nominatives révélant une situation de harcèlement", "conservées trois ans au maximum, "
     "dans des conditions garantissant leur confidentialité, le temps de la résolution.")
puce(pdf, "Fichiers numériques", "la sauvegarde exportée contient les réponses et, le cas échéant, les "
     "prénoms : conservée par le directeur dans les mêmes conditions, sur un support maîtrisé par l’école. "
     "L’export CSV ne contient aucun prénom.")

encadre(pdf, "Point de vigilance pour la circonscription",
        ["L’outil n’est adossé à aucun serveur : il n’existe pas de base de données académique, et ce sont "
         "les fichiers exportés par l’école qui constituent la trace. Il convient donc de désigner un "
         "adulte responsable de leur conservation, et de les détruire à l’échéance prévue."],
        bg=(255, 251, 235), bord=(253, 230, 138), tc=ORANGE)

# ====================== PAGE 3 — AVANT LA CAMPAGNE ======================
pdf.add_page()
h1(pdf, "Avant la campagne : organiser", 18)
para(pdf, "Le cas visé : sur les 18 classes de l’école, 7 passent le questionnaire (2 CE2, 1 CE2-CM1, "
          "2 CM1, 1 CM1-CM2, 1 CM2). Les 11 classes de CP et de CE1 ont des activités adaptées le même jour, "
          "décrites dans le complément CP-CE1 : elles ne remplissent pas la grille. Chaque enseignant "
          "saisit sa propre classe, sur son propre poste.")

h2(pdf, "1. Imprimer les grilles", avant=2)
para(pdf, "Autant d’exemplaires que d’élèves, à partir du PDF officiel de la grille 2025 (une page "
          "recto-verso : les 24 questions au recto, les 9 questions de contexte et l’encadré de "
          "l’enseignant au verso). Prévoir quelques exemplaires supplémentaires pour les élèves absents "
          "qui reviendront plus tard dans la période.")

h2(pdf, "2. Répartir les rôles")
puce(pdf, "Chaque professeur", "fait passer la grille dans sa classe, ramasse les copies, puis saisit "
     "les résultats de sa classe dans l’application.")
puce(pdf, "Le directeur", "tient la fiche de suivi (dernière page), rappelle l’échéance, et consolide "
     "les saisies sur le poste de référence.")
puce(pdf, "Le poste de référence", "un ordinateur de l’école qui ne sert pas à la saisie : c’est lui qui "
     "réunira les sept fichiers, calculera les résultats de l’école et produira le rapport.")

h2(pdf, "3. Vérifier l’application sur chaque poste")
puce(pdf, "Ouvrir le lien, puis « Ajouter à l’écran d’accueil »", "l’application fonctionne ensuite hors "
     "connexion, ce qui évite les mauvaises surprises le jour de la saisie.")
puce(pdf, "Vérifier la version", "en bas de l’écran d’accueil doit apparaître « " + VERSION + " ». Si un "
     "autre numéro s’affiche, fermer complètement l’application et la rouvrir ; au besoin, supprimer "
     "l’icône et la recréer depuis le lien.")
puce(pdf, "Rien à configurer", "les sept classes concernées sont déjà pré-remplies dans l’application. "
     "Aucune liste à saisir, sur aucun poste.", color=VERT)

h2(pdf, "4. Ce que représente le temps de saisie")
para(pdf, "Un questionnaire se recopie en une minute environ au clavier (33 réponses à cocher). Pour une "
          "classe de 25 élèves, compter 25 à 30 minutes, à faire au calme, une fois les grilles ramassées. "
          "Ce temps n’a pas à être pris sur les deux heures banalisées de la passation : il peut être "
          "fractionné sur plusieurs jours, tant que la saisie est terminée avant la fin de la période.")

encadre(pdf, "Ordre de grandeur pour l’école",
        ["7 classes × 25 élèves = environ 175 questionnaires, soit 175 minutes de saisie réparties entre "
         "les sept enseignants : une demi-heure chacun.",
         "C’est le point sur lequel il faut être vigilant : une classe non saisie fausse les résultats de "
         "l’école, et rien ne le signale — d’où la fiche de suivi."],
        bg=(240, 253, 244), bord=(187, 247, 208), tc=VERT)

# ===================== PAGE 4 — LA PASSATION EN CLASSE =====================
pdf.add_page()
h1(pdf, "La passation en classe, sur papier", 18)
para(pdf, "Cette page reprend les obligations du guide de passation. Elle est à lire avant la séance.",
          color=GREY, size=8.9)
pdf.ln(1)

num(pdf, 1, "Expliquer avant de distribuer", [
    "Rappeler ce qu’est le harcèlement et le cyberharcèlement, et ce que l’école en fait. Des ressources "
    "sont disponibles sur éduscol et sur la plateforme Phare.",
    "Préciser que les réponses ne sont pas obligatoires, que le prénom n’est pas demandé, et que les "
    "adultes de l’école lisent les réponses pour aider les élèves qui en ont besoin. Lire la mention "
    "informative figurant au dos de la grille."])
num(pdf, 2, "Distribuer et accompagner", [
    "Expliquer les quatre modalités de réponse : Jamais, Parfois, Souvent, Très souvent, en tenant compte "
    "de ce qui s’est passé depuis le début de l’année scolaire.",
    "Les élèves prennent le temps qu’ils souhaitent. Mettre en confiance, rassurer sur la confidentialité, "
    "encourager la sincérité.",
    "Les élèves à besoins éducatifs particuliers (Ulis, UPE2A) peuvent disposer d’un temps et d’un "
    "accompagnement spécifiques, avec un travail préalable sur le sens des questions."])
num(pdf, 3, "Ramasser et écouter", [
    "Les grilles sont ramassées par le professeur de la classe.",
    "La passation peut entraîner une libération de la parole. Un élève qui pleure, qui se bloque ou qui "
    "reste silencieux doit pouvoir parler à un adulte tout de suite : personnels sociaux et de santé, "
    "RASED, psychologue scolaire sont mobilisés à cette occasion."])
num(pdf, 4, "Avant la fin de la séance, redire", [
    "La violence, sous toutes ses formes, est inacceptable à l’école comme en dehors : une moquerie, une "
    "insulte, un coup ne sont jamais « pour rire ».",
    "Tous les adultes de l’école sont disponibles pour écouter, à tout moment de l’année, même si l’élève "
    "n’a pas écrit son prénom. Les noms des adultes référents et des élèves ambassadeurs peuvent être "
    "affichés.",
    "3018 : numéro gratuit, anonyme et confidentiel, 7 jours sur 7 de 9 h à 23 h."])

encadre(pdf, "L’alternative tablette, pour un élève isolé",
        ["L’application propose aussi le questionnaire directement à l’écran : « Répondre au questionnaire "
         "(élève) ».",
         "C’est utile pour un élève absent le jour de la passation, ou pour un petit groupe qui ne peut pas "
         "attendre. Les questions y sont les mêmes, avec en plus une lecture à voix haute et une "
         "reformulation en français simple — un appui pour les élèves en difficulté de lecture.",
         "Ce mode reste marginal : la méthode retenue pour l’école est le papier."],
        bg=IND_L, bord=(199, 210, 254), tc=IND)

# ==================== PAGE 5 — LA SAISIE PAR L'ENSEIGNANT ====================
pdf.add_page()
h1(pdf, "La saisie par l’enseignant", 18)
para(pdf, "C’est l’étape nouvelle. Elle se fait au calme, une fois les grilles ramassées.")

num(pdf, 1, "Ouvrir la saisie et choisir sa classe", [
    "Bouton « Saisir les réponses (enseignant) », puis la classe. Elle est mémorisée pour toute la "
    "série : inutile de la choisir à chaque élève."])
num(pdf, 2, "Recopier un questionnaire par écran", [
    "24 lignes de questions, puis 9 lignes oui/non, dans le même ordre que la grille papier : on lit la "
    "copie ligne par ligne et on coche en face.",
    "Fille / garçon, année de naissance et prénom sont facultatifs. Le prénom, s’il est saisi, permet au "
    "directeur de retrouver nominativement l’élève dans la liste « Élèves à recevoir »."])
num(pdf, 3, "Utiliser le clavier, pas la souris", [
    "Les touches 1 à 4 remplissent la ligne surlignée et passent automatiquement à la suivante. Pour les "
    "questions oui/non, 1 = oui et 2 = non. La touche Entrée enregistre le questionnaire, remet le "
    "formulaire à zéro et conserve la classe : l’élève suivant est immédiat.",
    "Une ligne laissée vide n’est pas comptée, comme sur le papier. Un questionnaire dont aucune réponse "
    "n’est cochée n’est pas enregistré."])
num(pdf, 4, "Se corriger", [
    "« Annuler le dernier » supprime le questionnaire qui vient d’être enregistré pour cette classe : "
    "c’est la réponse à une erreur de recopie. Les questionnaires déjà enregistrés ne peuvent pas être "
    "modifiés un par un — mieux vaut vérifier la copie avant de valider la suivante."])

y = pdf.get_y() + 1.5
pdf.image(SH + "/shots/crop-saisie.png", x=LM, y=y, w=88)
pdf.set_xy(LM + 94, y + 1)
pdf.set_font("D", "B", 9.4)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "L’écran de saisie")
pdf.ln(6)
pdf.set_x(LM + 94)
pdf.set_font("D", "", 8.6)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 94, 4.85,
    "La ligne en cours est surlignée. Les réponses cochées prennent la couleur de la grille : vert, jaune, "
    "orange, rouge.", align="L")
pdf.ln(2.0)
pdf.set_x(LM + 94)
pdf.multi_cell(W - 94, 4.85,
    "Le bandeau rappelle la classe et le nombre de questionnaires déjà recopiés : c’est le compteur à "
    "comparer avec le nombre de copies ramassées.", align="L")
pdf.ln(2.0)
pdf.set_x(LM + 94)
pdf.multi_cell(W - 94, 4.85,
    "Une fois les copies saisies : onglet Données → « Sauvegarde complète (.json) ». Un fichier par "
    "enseignant, à transmettre au directeur.", align="L")

pdf.set_y(max(pdf.get_y(), y + 78) + 4)
encadre(pdf, "Combien de temps ?",
        ["Une minute environ par questionnaire : 33 réponses à cocher, sans changer de page.",
         "25 à 30 minutes pour une classe de 25 élèves. Ce temps n’a pas à être pris sur les deux heures "
         "banalisées de la passation : il peut être fractionné, tant que la saisie est terminée avant la "
         "fin de la période."],
        bg=(240, 253, 244), bord=(187, 247, 208), tc=VERT)

# ======================= PAGE 6 — LIRE LES RÉSULTATS =======================
pdf.add_page()
h1(pdf, "Lire les résultats", 18)
para(pdf, "Espace adulte → code 2026. L’onglet « Vue d’ensemble » donne les chiffres et l’interprétation ; "
          "l’onglet « Rapport » produit le document à imprimer.")

h2(pdf, "Comment sont calculés les scores", avant=1)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 8.3)
pdf.set_fill_color(*IND_L)
pdf.set_text_color(*INK)
pdf.cell(62, 7, "Indice", border=1, fill=True)
pdf.cell(90, 7, "Ce qui est compté", border=1, fill=True)
pdf.cell(22, 7, "Étendue", border=1, fill=True, align="C")
pdf.ln()
rows = [("Total A — qualité de vie", "réponses 3 ou 4 aux questions 2 à 8", "0 à 7"),
        ("Total B — atteintes subies", "réponses 3 ou 4 aux questions 11 à 20", "0 à 10"),
        ("Total C — atteintes graves", "réponses 2, 3 ou 4 aux questions 21 à 24", "0 à 4"),
        ("Score de victimation", "total B + total C", "0 à 14")]
pdf.set_font("D", "", 8.4)
for a, b, c in rows:
    pdf.cell(62, 7, a, border=1)
    pdf.cell(90, 7, b, border=1)
    pdf.cell(22, 7, c, border=1, align="C")
    pdf.ln()
pdf.ln(2.5)

h2(pdf, "La table de croisement officielle", avant=1)
para(pdf, "L’application applique exactement cette table : les deux indices élevés, la situation est "
          "retenue comme du harcèlement ; un seul indice élevé, l’élève est « à surveiller ».")
pdf.ln(1)
tableau_croisement(pdf)
pdf.ln(1.2)
para(pdf, "Lecture : un élève qui déclare 8 atteintes ou plus, quel que soit son niveau de mal-être, est "
          "en zone harcèlement. À l’inverse, un élève qui exprime un mal-être important (total A de 5 ou "
          "plus) sans atteinte déclarée est également en zone harcèlement : la souffrance installée fait "
          "présumer des faits que l’élève ne nomme pas.", size=8.9)

encadre(pdf, "Exemple de lecture, de bout en bout",
        ["Un élève répond « souvent » aux questions 3, 7, 8 et « très souvent » à la question 2 : total A = 4. "
         "Il déclare 6 atteintes répétées (questions 11 à 20), aucune atteinte grave : B + C = 6.",
         "Ligne « 3 à 4 », colonne « 5 à 7 » → zone « à surveiller » : la souffrance est réelle et les faits "
         "sont répétés, l’élève doit être revu et écouté, même sans harcèlement au sens de la grille."],
        bg=IND_L, bord=(199, 210, 254), tc=IND, size=8.4)

h2(pdf, "Comment lire les chiffres", avant=1)
puce(pdf, "Le pourcentage compte des élèves, pas des faits", "12 % sur 33 élèves, cela fait 4 élèves. "
     "Sur un petit effectif, un élève pèse 3 points : l’application affiche systématiquement cette prudence.")
puce(pdf, "3 % et 13 % sont des repères, pas des objectifs", "ce sont les résultats nationaux de novembre "
     "2025 pour les écoliers du CE2 au CM2. Être au-dessus ne signifie pas « école en échec » : cela "
     "signifie que le travail à mener est identifié.", color=ORANGE)
puce(pdf, "Les faits graves ne relèvent pas de la prévention", "violence sexuelle, violences physiques, "
     "cyberviolence : ils sont signalés nommément et appellent un signalement immédiat.", color=ROUGE)

# ==================== PAGE 7 — CONSOLIDER LES SAISIES ====================
pdf.add_page()
h1(pdf, "Consolider les sept saisies", 18)
para(pdf, "Chaque poste conserve ses propres données : rien ne se synchronise automatiquement. La "
          "consolidation se fait par fichiers, en trois temps.")
pdf.ln(1)

num(pdf, 1, "Chaque enseignant exporte sa saisie", [
    "Espace adulte → onglet Données → « Sauvegarde complète (.json) ». Le fichier arrive dans les "
    "téléchargements du poste.",
    "Le renommer avec le nom de la classe (CM1-B.json) et le transmettre au directeur — par messagerie "
    "ou sur une clé. C’est la seule sauvegarde : un poste dont l’historique Chrome est vidé perd tout, "
    "sans rattrapage."])
num(pdf, 2, "Le directeur fusionne sur le poste de référence", [
    "Ouvrir la même adresse sur ce poste, puis Espace adulte → Données → « Fusionner plusieurs postes de "
    "saisie » et sélectionner les sept fichiers en une seule fois. Les doublons sont écartés "
    "automatiquement : on peut réimporter sans risque.",
    "L’onglet Données affiche alors « Postes de saisie » : le nombre doit correspondre au nombre "
    "d’enseignants. S’il en manque un, c’est que son fichier n’a pas été importé — c’est le contrôle à "
    "faire avant tout envoi."])
num(pdf, 3, "Compléter et produire les documents", [
    "Réglages → Classes et effectifs : renseigner les effectifs des sept classes. Eux seuls permettent de "
    "calculer les taux de participation, par classe et par niveau.",
    "Rapport → « Imprimer / Enregistrer en PDF » pour le conseil des maîtres et la circonscription ; "
    "« Copier la synthèse » pour le courrier ou le message à l’IEN."])

h2(pdf, "Ce que montre le tableau de bord")
puce(pdf, "Vue d’ensemble", "les quatre indicateurs, la comparaison au baromètre national, "
     "l’interprétation rédigée, les faits les plus déclarés, et le nombre de postes fusionnés.")
puce(pdf, "Par classe, puis par niveau", "les sept classes, et le regroupement CE2 / CM1 / CM2 / CM1-CM2.")
puce(pdf, "Par question", "les 24 questions classées par fréquence : c’est ce qui désigne les thèmes de "
     "prévention à travailler en priorité.")
puce(pdf, "Élèves à recevoir", "les situations classées de la plus préoccupante à la moins préoccupante, "
     "avec les numéros de questions en jeu. Les questionnaires sans prénom restent anonymes et servent à "
     "l’analyse collective.")

encadre(pdf, "À ne pas faire",
        ["Vider l’historique ou les données de Chrome sur un poste avant l’export.",
         "Saisir deux fois la même copie : le questionnaire compterait deux fois dans les statistiques.",
         "Oublier de saisir une classe : les résultats de l’école seraient faux, et rien ne le signalerait.",
         "Consolider sur un poste qui a servi à la saisie alors que le poste de référence est disponible : "
         "la confusion entre données locales et données fusionnées est alors inutile."],
        bg=(254, 242, 242), bord=(254, 202, 202), tc=ROUGE)

# ============== PAGE 8 — PRISE EN CHARGE, LABELLISATION, SUITE ==============
pdf.add_page()
h1(pdf, "Prise en charge et suite du dispositif", 18)

h2(pdf, "Que faire des élèves repérés", avant=1)
puce(pdf, "Questionnaire nominatif en situation de harcèlement", "entretien obligatoire avec l’élève, "
     "mesures conservatoires nécessaires, information de la famille, ouverture du protocole national de "
     "traitement des situations de harcèlement.")
puce(pdf, "Questionnaire anonyme en situation de harcèlement", "l’élève ne peut pas être identifié, mais "
     "une action d’information et de sensibilisation doit être organisée dans la classe concernée.")
puce(pdf, "Faits graves", "signalement immédiat à la direction et à l’équipe ressource Phare, sans "
     "attendre l’analyse collective.", color=ROUGE)
puce(pdf, "Élèves « à surveiller »", "pas de protocole, mais une vigilance : les revoir, les observer en "
     "récréation, parler avec eux avant que la situation ne s’installe.", color=ORANGE)

h2(pdf, "Restitution")
para(pdf, "Une restitution à l’attention des élèves et des parents est organisée, selon des modalités à "
          "l’initiative de l’école : atelier des parents, réunion par classe ou par niveau. Il ne s’agit "
          "pas de donner le détail des réponses, mais de faire apparaître les grandes tendances et les "
          "principaux comportements subis, observés ou commis. Un courrier type adressé aux parents est "
          "disponible sur éduscol.")

h2(pdf, "Le dossier de labellisation (niveau 1)")
pdf.set_draw_color(*LINE)
rows2 = [
    ("Axe 1 — S’engager", "Une enquête menée auprès de tous les élèves, des résultats interprétés et "
     "partagés en conseil des maîtres : un diagnostic local, pas une intention."),
    ("Axe 2 — Prévenir", "Des thèmes prioritaires désignés par les élèves eux-mêmes, donc des séances "
     "ciblées, et un indicateur pour mesurer leur effet."),
    ("Axe 3 — Former", "Un protocole commun à tous les collègues, réutilisable chaque année : passation "
     "identique, saisie identique, exploitation identique."),
    ("Axe 4 — Prendre en charge", "Les situations identifiées, nominatives ou non, avec la trace des "
     "élèves reçus et des faits graves signalés."),
]
for a, b in rows2:
    y = pdf.get_y()
    hb = 4.8 * max(1, len(b) // 84 + (1 if len(b) % 84 else 0)) + 5
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(LM, y, 40, hb, style="DF")
    pdf.rect(LM + 40, y, W - 40, hb)
    pdf.set_xy(LM + 2, y + 2.2)
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*INK)
    pdf.multi_cell(36, 4.6, a, align="L")
    pdf.set_xy(LM + 42, y + 2.2)
    pdf.set_font("D", "", 8.5)
    pdf.multi_cell(W - 44, 4.6, b, align="L")
    pdf.set_y(y + hb + 1.2)

h2(pdf, "Calendrier proposé", avant=1.4)
puce(pdf, "5 novembre – 11 décembre 2026", "passation sur papier dans les sept classes, puis saisie par "
     "chaque enseignant.")
puce(pdf, "Décembre 2026", "consolidation sur le poste de référence, conseil des maîtres, restitution aux "
     "familles.")
puce(pdf, "Janvier – mai 2027", "actions de prévention ciblées sur les thèmes sortis en tête.")
puce(pdf, "Juin 2027", "seconde passation avec le même protocole. La comparaison des deux mesures "
     "constitue la preuve qu’un dispositif fonctionne : c’est ce que demandent les dossiers de "
     "labellisation, et ce qui manque le plus souvent.", color=VERT)

h2(pdf, "Checklist avant transmission à la circonscription", avant=1.4)
for item in ["Les sept classes ont rendu leurs grilles et leur saisie.",
             "L’onglet Données affiche sept postes de saisie.",
             "Les effectifs des sept classes sont renseignés (taux de participation).",
             "L’onglet « Élèves à recevoir » a été examiné et les entretiens sont programmés.",
             "Les faits graves ont été signalés à la direction.",
             "Le rapport est enregistré en PDF et la synthèse est prête pour le courrier."]:
    pdf.set_x(LM)
    pdf.set_font("D", "", 8.9)
    pdf.set_draw_color(150, 155, 170)
    pdf.set_line_width(0.35)
    yy = pdf.get_y()
    pdf.rect(LM + 1, yy + 0.8, 3.6, 3.6)
    pdf.set_x(LM + 7)
    pdf.multi_cell(W - 7, 4.85, item, align="L")
    pdf.ln(0.2)

# ========================= PAGE 9 — FICHE DE SUIVI =========================
fiche_suivi(pdf)

out = "/workspace/nah/mode-emploi-non-au-harcelement.pdf"
pdf.output(out)
print("PDF:", out, os.path.getsize(out), "octets,", pdf.page_no(), "pages")
