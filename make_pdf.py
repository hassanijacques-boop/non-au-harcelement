# -*- coding: utf-8 -*-
"""Mode d'emploi / protocole — application « Non au harcèlement » (fpdf2 + DejaVu)."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
SH = "/workspace/nah"
URL = "https://hassanijacques-boop.github.io/non-au-harcelement/"
VERSION = "20261027-4"

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
        self.cell(0, 6, "Non au harcèlement — protocole de passation · " + URL + " · v" + VERSION)
        self.set_y(-12)
        self.cell(0, 6, "page %d" % self.page_no(), align="R")


def bandeau(pdf, titre, sous1, sous2):
    pdf.set_fill_color(*IND)
    pdf.rect(0, 0, 210, 34, style="F")
    pdf.set_xy(LM, 7.5)
    pdf.set_font("D", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 9, titre)
    pdf.set_xy(LM, 17)
    pdf.set_font("D", "", 9.6)
    pdf.cell(0, 5, sous1)
    pdf.set_xy(LM, 23)
    pdf.set_font("D", "", 8.4)
    pdf.cell(0, 5, sous2)
    pdf.set_y(40)


def h1(pdf, txt, y=None):
    if y:
        pdf.set_y(y)
    else:
        pdf.ln(1)
    pdf.set_font("D", "B", 14.5)
    pdf.set_text_color(*IND)
    pdf.set_x(LM)
    pdf.multi_cell(W, 7.6, txt, align="L")
    pdf.set_x(LM)
    pdf.ln(1.6)


def h2(pdf, txt, color=INK, avant=2.6):
    if pdf.get_y() > 248:
        pdf.add_page()
    pdf.ln(avant)
    pdf.set_font("D", "B", 10.6)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, 6.0, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)
    pdf.ln(1.0)


def para(pdf, txt, size=9.2, color=INK, lh=5.15):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, titre, txt, color=IND, size=9.1):
    if pdf.get_y() > 264:
        pdf.add_page()
    contenu = ("**" + titre + "** : " + txt) if titre else txt
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.multi_cell(W, 5.15, "•  " + contenu, align="L", markdown=True)
    pdf.set_x(LM)
    pdf.ln(1.2)


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
    pdf.ln(1.6)


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
    """Reproduction de la table officielle : A en lignes, B+C en colonnes."""
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
    wl = 30      # colonne des libellés
    wc = 22.8    # largeur d’une colonne
    hh = 7
    # en-tête
    pdf.set_fill_color(*IND)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("D", "B", 8.4)
    pdf.set_xy(x0, pdf.get_y())
    pdf.cell(wl, hh, "Total A", border=1, fill=True, align="C")
    pdf.cell(wc * 5, hh, "Total B + Total C", border=1, fill=True, align="C")
    pdf.ln()
    pdf.set_x(x0)
    pdf.cell(wl, hh, "", border=1, fill=True)
    pdf.set_font("D", "B", 8)
    for c in cols:
        pdf.cell(wc, hh, c, border=1, fill=True, align="C")
    pdf.ln()
    pdf.set_font("D", "", 8.4)
    for i, lab in enumerate(lignes):
        pdf.set_x(x0)
        pdf.set_fill_color(*IND_L)
        pdf.set_text_color(*INK)
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
    bandeau(pdf, "Fiche de suivi des tablettes",
            "À imprimer et à garder près des tablettes pendant toute la campagne",
            "Une ligne par tablette · cocher au fur et à mesure · l’export est la seule sauvegarde")
    pdf.set_y(42)
    pdf.set_font("D", "B", 9.6)
    pdf.set_text_color(*INK)
    pdf.cell(60, 7, "École : " + "." * 40, border=0)
    pdf.set_x(120)
    pdf.cell(0, 7, "Période : …… / …… / 2026  →  …… / …… / 2026")
    pdf.ln(11)

    cols = [("N°", 10), ("Classe(s) passée(s) sur cette tablette", 74), ("Date", 26),
            ("Export .json fait", 32), ("Importé sur le PC", 32)]
    pdf.set_fill_color(*IND)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("D", "B", 8.2)
    pdf.set_x(LM)
    for nom, w in cols:
        pdf.cell(w, 8, nom, border=1, fill=True, align="C")
    pdf.ln()
    pdf.set_text_color(*INK)
    pdf.set_font("D", "", 9)
    hb = 13.5
    for i in range(1, 11):
        pdf.set_x(LM)
        pdf.cell(10, hb, str(i), border=1, align="C")
        pdf.cell(74, hb, "", border=1)
        pdf.cell(26, hb, "", border=1)
        for k in range(2):
            x = pdf.get_x()
            pdf.cell(32, hb, "", border=1)
            pdf.set_draw_color(150, 155, 170)
            pdf.set_line_width(0.35)
            pdf.rect(x + 2.5, pdf.get_y() + hb / 2 - 3.2, 6.4, 6.4)
        pdf.ln()

    pdf.ln(4)
    pdf.set_draw_color(*LINE)
    pdf.set_font("D", "", 8.4)
    for txt in ["Total des tablettes utilisées : ....................        Total des fichiers importés sur le PC : ....................",
                "Le PC affiche « X tablette(s) » dans l’onglet Données : ce nombre doit être identique aux deux lignes ci-dessus.",
                "Signature de l’adulte responsable : ..................................................        Date : ....... / ....... / 2026"]:
        pdf.set_x(LM)
        pdf.cell(0, 6.5, txt)
        pdf.ln(6.5)

    pdf.ln(2)
    encadre(pdf, "Rappel",
            ["Une tablette qui n’est pas exportée avant que quelqu’un vide l’historique de Chrome perd ses "
             "réponses : il n’y a pas de rattrapage possible.",
             "Le nom du fichier exporté contient la date et l’heure : renommez-le avec le numéro de la "
             "tablette (tablette-3.json) pour vous y retrouver."],
            bg=(254, 242, 242), bord=(254, 202, 202), tc=ROUGE)


pdf = PDF()

# ============================ PAGE 1 — L'ESSENTIEL ============================
pdf.add_page()
bandeau(pdf, "Non au harcèlement",
        "Enquête d’auto-évaluation · école élémentaire CE2-CM2 · année scolaire 2026-2027",
        "Protocole de passation, d’exploitation et de restitution — à l’attention des professeurs, du directeur, du CPC et de l’IEN")

h1(pdf, "Ouvrir l’application", 40)
pdf.set_font("D", "", 9.1)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.multi_cell(108, 5.1,
    "Sur chaque tablette : ouvrir Chrome, taper l’adresse ci-dessous, ou scanner le QR code. Puis, "
    "dans le menu de Chrome (trois points en haut à droite), choisir « Ajouter à l’écran d’accueil » : "
    "l’application s’installe comme une application ordinaire et fonctionne ensuite sans connexion.",
    align="L")
pdf.ln(2)
pdf.set_font("D", "B", 9.0)
pdf.set_text_color(*IND)
pdf.set_x(LM)
pdf.multi_cell(108, 4.6, "hassanijacques-boop.github.io/", align="L")
pdf.set_x(LM)
pdf.multi_cell(108, 4.6, "non-au-harcelement/", align="L")
pdf.ln(1)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(108, 4.5, "Aucun compte · aucun magasin d’applications · aucun paiement · aucune donnée envoyée sur Internet", align="L")
pdf.set_font("D", "B", 8.2)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.multi_cell(108, 4.5, "Version de référence de ce document : " + VERSION, align="L")
pdf.set_font("D", "B", 9.0)
pdf.set_text_color(*VERT)
pdf.set_x(LM)
pdf.multi_cell(108, 4.8, "Code d’accès adulte : 2026 (modifiable dans Réglages)", align="L")
pdf.set_text_color(*INK)

pdf.image(SH + "/qr-code.png", x=138, y=42, w=34)
pdf.set_xy(138, 77)
pdf.set_font("D", "", 7.2)
pdf.set_text_color(*GREY)
pdf.multi_cell(44, 4.0, "À scanner avec l’appareil photo de la tablette", align="C")

pdf.set_y(101)
h1(pdf, "L’essentiel en dix lignes", 108)
para(pdf,
     "La grille d’auto-évaluation officielle est passée sur tablette par tous les élèves du CE2 au CM2, "
     "pendant la période fixée par le guide de passation. L’application calcule elle-même les trois indices "
     "officiels, situe chaque élève dans la table de croisement, produit l’interprétation et le rapport "
     "destiné à la circonscription. L’exploitation des résultats — qui faisait défaut les années "
     "précédentes — est donc automatique et identique pour toutes les classes.")
pdf.ln(1.5)

h2(pdf, "Ce que fait l’application", avant=1)
puce(pdf, "Un résultat par élève", "zone « harcèlement », zone « à surveiller » ou absence de difficulté, selon la table officielle.")
puce(pdf, "Des résultats par classe et par niveau", "les deux CE2 se cumulent sous « CE2 », les trois CM1 sous « CM1 » ; la classe à cours multiple apparaît sous « CM1/CM2 ».")
puce(pdf, "Une interprétation rédigée", "comparée aux repères nationaux du baromètre 2025 (3 % en harcèlement, 13 % à surveiller chez les écoliers).")
puce(pdf, "Un rapport A4 et une synthèse", "pour le conseil des maîtres, la restitution aux familles et la transmission à l’IEN.")
puce(pdf, "La consolidation de plusieurs tablettes", "les réponses de 10 tablettes se réunissent en un seul ensemble, avec contrôle du nombre de tablettes fusionnées.")

encadre(pdf, "Ce que l’application ne fait pas",
        ["Elle n’envoie rien sur Internet : les réponses restent dans la tablette qui les a reçues, et la "
         "consolidation se fait par export de fichier. C’est un choix assumé pour cette année scolaire.",
         "Elle ne remplace aucun acte professionnel : l’entretien avec l’élève, l’information des familles et "
         "le signalement relèvent des adultes, pas de l’outil.",
         "Elle ne modifie pas la grille : les questions sont reproduites à l’identique (voir page 2)."],
        bg=IND_L, bord=(199, 210, 254), tc=IND)

# ======================= PAGE 2 — LE CADRE OFFICIEL =======================
pdf.add_page()
h1(pdf, "Le cadre officiel", 18)
para(pdf, "Cette page est destinée au directeur, au CPC et à l’IEN : elle situe l’outil par rapport aux "
          "textes et vérifie qu’il ne s’en écarte pas.")

h2(pdf, "Textes de référence")
puce(pdf, "Grille d’auto-évaluation — version 2025", "questionnaire élève du CE2 au CM2, 24 questions "
     "graduées de 1 (jamais) à 4 (très souvent), complétées par 9 questions de contexte.")
puce(pdf, "Guide de passation — octobre 2026", "année scolaire 2026-2027 : deux heures banalisées entre "
     "le jeudi 5 novembre et le vendredi 11 décembre 2026 ; passation assurée par le professeur de la classe "
     "dans le premier degré ; exploitation par le professeur puis partage avec le directeur.")
puce(pdf, "Objectifs officiels", "détecter les situations de harcèlement, faciliter la prévention, mobiliser "
     "l’ensemble de la communauté éducative.")

h2(pdf, "Fidélité de l’instrument")
para(pdf, "C’est le point sur lequel un regard extérieur doit être rassurant, et il l’est :")
puce(pdf, "Les 24 questions et les 9 questions de contexte sont reproduites mot pour mot", "aucune "
     "reformulation ne se substitue au texte officiel.")
puce(pdf, "Deux ajouts, tous deux placés sous le texte officiel", "une reformulation « En clair » en "
     "français simple et une lecture à voix haute. Ils répondent à une difficulté locale de lecture et à la "
     "présence d’élèves allophones, sans changer le nombre d’items, leur ordre, l’échelle de réponse ni la "
     "règle de comptage.")
puce(pdf, "Le calcul est celui de la grille", "totaux A, B et C, puis croisement A × (B+C) dans la table "
     "officielle reproduite page 5.")

h2(pdf, "Information des élèves et des familles")
para(pdf, "Le guide prévoit que le professeur lise aux élèves la mention informative du questionnaire. "
          "L’application l’affiche avant la première question : réponses non obligatoires, prénom non "
          "demandé, lecture des réponses par les adultes de l’école pour aider les élèves qui en ont besoin.")
para(pdf, "Destinataires, conformément à la grille : les adultes qui font passer le questionnaire, le "
          "directeur, l’IEN, les adultes chargés de résoudre les situations, les personnes désignées par le "
          "directeur, et les parents ou responsables légaux.")

h2(pdf, "Conservation des données")
puce(pdf, "Questionnaires", "conservés jusqu’à la fin de l’année scolaire, puis détruits dans des "
     "conditions ne permettant pas leur réutilisation.")
puce(pdf, "Questionnaires nominatifs révélant une situation de harcèlement", "conservés trois ans au "
     "maximum, dans des conditions garantissant leur confidentialité, le temps de la résolution.")
puce(pdf, "Fichiers numériques", "la sauvegarde exportée contient les réponses et, le cas échéant, les "
     "prénoms : elle est conservée par le directeur dans les mêmes conditions, sur un support maîtrisé par "
     "l’école. L’export CSV, lui, ne contient aucun prénom.")

encadre(pdf, "Point de vigilance pour la circonscription",
        ["L’outil n’étant adossé à aucun serveur, il n’existe pas de base de données académique : ce sont les "
         "fichiers exportés par l’école qui constituent la trace. Il convient donc de désigner un adulte "
         "responsable de la conservation, et de détruire les fichiers à l’échéance prévue."],
        bg=(255, 251, 235), bord=(253, 230, 138), tc=ORANGE)

# ====================== PAGE 3 — AVANT LA PASSATION ======================
pdf.add_page()
h1(pdf, "Avant la passation : préparer les tablettes", 18)
para(pdf, "Le cas visé ici est celui d’une école de 7 classes (2 CE2, 3 CM1, 1 CM2, 1 CM1-CM2) qui "
          "utilise une dizaine de tablettes circulant entre les classes.")

h2(pdf, "1. Installer l’application sur chaque tablette", avant=2)
num(pdf, 1, "Ouvrir le lien", ["Scanner le QR code de la page 1, ou taper l’adresse. L’application "
                               "fonctionne ensuite hors connexion."])
num(pdf, 2, "Ajouter à l’écran d’accueil", ["Menu de Chrome (trois points) → « Ajouter à l’écran "
                                           "d’accueil ». L’icône apparaît avec les autres applications."])
num(pdf, 3, "Vérifier la version", ["Sur l’écran d’accueil de l’application, en bas : la version doit être "
                                    "« " + VERSION + " ». Si un autre numéro s’affiche, fermer complètement "
                                    "l’application et la rouvrir ; au besoin, supprimer l’icône et la recréer."])
num(pdf, 4, "Vérifier le son", ["Le bouton « Écouter la question » doit être audible. Régler le volume "
                                "avant la séance, pas pendant."])

h2(pdf, "2. Vérifier que les classes sont les bonnes")
para(pdf, "Les sept classes de l’école sont pré-remplies dans l’application : CE2 A, CE2 B, CM1 A, "
          "CM1 B, CM1 C, CM2, CM1/CM2. Aucun réglage n’est nécessaire. Si l’organisation de l’école "
          "change, la liste se modifie dans Espace adulte → Réglages → Classes et effectifs — et cette "
          "modification doit être faite de la même façon sur toutes les tablettes, sinon les élèves ne "
          "choisiront pas la même classe.")

h2(pdf, "3. Étiqueter et suivre les tablettes")
puce(pdf, "Numéroter les tablettes de 1 à 10", "une gommette suffit. Le numéro sert au renommage des "
     "fichiers exportés et au contrôle final.")
puce(pdf, "Utiliser la fiche de suivi (dernière page)", "une ligne par tablette : classe passée, date, "
     "export fait, import fait. C’est ce document qui garantit qu’aucune tablette n’est oubliée.")
puce(pdf, "Une tablette, une classe, une séance", "ce n’est pas une obligation technique — la classe est "
     "enregistrée questionnaire par questionnaire — mais cela simplifie le contrôle.")

h2(pdf, "4. Combien de tablettes par classe ?")
para(pdf, "Un questionnaire demande 10 à 15 minutes (12 en moyenne). Une classe de 25 élèves représente "
          "donc environ 5 heures sur une seule tablette : pour tenir dans les deux heures banalisées, il "
          "faut 2 à 3 tablettes en parallèle. Avec 10 tablettes et 7 classes, la campagne s’étale "
          "naturellement sur plusieurs jours entre le 5 novembre et le 11 décembre.")
para(pdf, "Conseil d’organisation : privilégier des groupes de 8 à 10 élèves par tablette, plutôt qu’une "
          "classe entière sur un seul appareil. Un élève qui attend répond mal.", color=GREY, size=8.9)

# ====================== PAGE 4 — PENDANT LA PASSATION ======================
pdf.add_page()
h1(pdf, "Pendant la séance, pas à pas", 18)
para(pdf, "La séquence est assurée par le professeur de la classe. Compter une quinzaine de minutes de "
          "consignes et de sensibilisation avant la première tablette.", color=GREY, size=8.9)
pdf.ln(1)

num(pdf, 1, "Expliquer avant de lancer", [
    "Rappeler ce qu’est le harcèlement et le cyberharcèlement, que les réponses ne sont pas obligatoires, "
    "que le prénom n’est pas demandé, que les adultes sont là pour aider. Lire la mention informative "
    "affichée par l’application."])
num(pdf, 2, "Chaque élève commence", [
    "Bouton « Je réponds au questionnaire ». L’élève indique sa classe, fille ou garçon, son année de "
    "naissance. Ces trois informations servent uniquement à ranger les réponses.",
    "Une question par écran, toujours dans le même ordre. Le bouton « Écouter la question » la lit à voix "
    "haute : à proposer sans compter, c’est ce qui rend le questionnaire accessible aux élèves qui lisent "
    "difficilement et aux élèves allophones.",
    "La ligne bleue « En clair » reformule la question en français simple, sous le texte officiel : la "
    "question n’est jamais modifiée. L’élève peut revenir en arrière ou passer une question avec « Je "
    "préfère ne pas répondre » — elle n’est alors comptée ni pour ni contre lui."])
num(pdf, 3, "À la fin de chaque élève", [
    "Écran de remerciement avec le numéro 3018. L’élève appuie sur « Élève suivant » : la tablette est "
    "prête pour le camarade, sans rien réinitialiser. La page d’accueil indique le nombre de "
    "questionnaires déjà enregistrés : c’est le compteur de contrôle de la séance."])
num(pdf, 4, "Surveiller les réactions", [
    "Un élève qui pleure, qui se bloque ou qui reste silencieux est déjà une information. Un adulte doit "
    "être disponible pour l’écouter tout de suite. Le guide prévoit que les personnels sociaux et de "
    "santé, le RASED et le psychologue scolaire soient mobilisés à cette occasion."])

y = pdf.get_y() + 1.5
pdf.image(SH + "/shots/crop-question.png", x=LM, y=y, w=46)
pdf.set_xy(LM + 52, y + 1)
pdf.set_font("D", "B", 9.4)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "L’écran de question")
pdf.ln(6)
pdf.set_x(LM + 52)
pdf.set_font("D", "", 8.7)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 52, 4.9,
    "Les quatre réponses sont toujours dans le même ordre et de la même couleur : vert, jaune, orange, "
    "rouge. Un élève se trompe rarement.", align="L")
pdf.ln(2.2)
pdf.set_x(LM + 52)
pdf.multi_cell(W - 52, 4.9,
    "Le prénom est proposé à la fin, une seule fois : un adulte viendra parler à l’élève si ses réponses "
    "montrent qu’il souffre. Il peut rester anonyme.", align="L")

pdf.set_y(max(pdf.get_y(), y + 62) + 3)
encadre(pdf, "À dire aux élèves avant de ranger les tablettes",
        ["La violence, sous toutes ses formes, est inacceptable à l’école comme en dehors. Une moquerie, "
         "une insulte, un coup ne sont jamais « pour rire ».",
         "Tous les adultes de l’école sont disponibles pour écouter, à tout moment de l’année, même si "
         "l’élève n’a pas écrit son prénom. Les noms des adultes référents et des élèves ambassadeurs "
         "peuvent être affichés.",
         "3018 : numéro gratuit, anonyme et confidentiel, 7 jours sur 7 de 9 h à 23 h."],
        bg=(240, 253, 244), bord=(187, 247, 208), tc=VERT)

# ======================= PAGE 5 — LIRE LES RÉSULTATS =======================
pdf.add_page()
h1(pdf, "Après la séance : lire les résultats", 18)
para(pdf, "Espace adulte → code 2026 (modifiable dans Réglages). L’onglet « Vue d’ensemble » donne les "
          "chiffres et l’interprétation ; l’onglet « Rapport » produit le document à imprimer.")
pdf.ln(1.5)

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
pdf.ln(1.5)
para(pdf, "Lecture : un élève qui déclare 8 atteintes ou plus, quel que soit son niveau de mal-être, est "
          "en zone harcèlement. À l’inverse, un élève qui exprime un mal-être important (total A de 5 ou "
          "plus) sans atteinte déclarée est également en zone harcèlement : la souffrance installée fait "
          "présumer des faits que l’élève ne nomme pas.", size=8.9)

h2(pdf, "Comment lire les chiffres")
puce(pdf, "Le pourcentage compte des élèves, pas des faits", "12 % sur 33 élèves, cela fait 4 élèves. "
     "Sur un petit effectif, un élève pèse 3 points : l’application affiche systématiquement cette prudence.")
puce(pdf, "3 % et 13 % sont des repères, pas des objectifs", "ce sont les résultats nationaux de novembre "
     "2025 pour les écoliers du CE2 au CM2. Être au-dessus ne signifie pas « école en échec » : cela "
     "signifie que le travail à mener est identifié.", color=ORANGE)
puce(pdf, "La part « à surveiller » décrit le climat", "quand elle est haute, le problème n’est pas "
     "seulement individuel : il porte sur les relations dans l’école, donc sur les actions collectives.")
puce(pdf, "Les faits graves ne relèvent pas de la prévention", "violence sexuelle, violences physiques, "
     "cyberviolence : ils sont signalés nommément par l’application et appellent un signalement immédiat.",
     color=ROUGE)

encadre(pdf, "Exemple de lecture, de bout en bout",
        ["Un élève répond « souvent » aux questions 3, 7, 8 et « très souvent » à la question 2 : total A = 4. "
         "Il déclare 6 atteintes répétées (questions 11 à 20), aucune atteinte grave : B + C = 6.",
         "Ligne « 3 à 4 », colonne « 5 à 7 » → zone « à surveiller » : la souffrance est réelle et les faits "
         "sont répétés, l’élève doit être revu et écouté, même sans harcèlement au sens de la grille."],
        bg=IND_L, bord=(199, 210, 254), tc=IND, size=8.4)

# ==================== PAGE 6 — CONSOLIDER LES TABLETTES ====================
pdf.add_page()
h1(pdf, "Consolider les résultats des 10 tablettes", 18)
para(pdf, "Chaque tablette conserve ses propres réponses : rien ne se synchronise automatiquement. "
          "La consolidation se fait par fichiers, en trois temps.")
pdf.ln(1)

num(pdf, 1, "Sur chaque tablette, à la fin de sa dernière séance", [
    "Espace adulte → onglet Données → « Sauvegarde complète (.json) ». Le fichier arrive dans les "
    "téléchargements de la tablette.",
    "Le renommer avec le numéro de la tablette (tablette-3.json) et cocher la case « export fait » sur "
    "la fiche de suivi. C’est la seule sauvegarde : une tablette dont l’historique Chrome est vidé perd "
    "tout, sans rattrapage."])
num(pdf, 2, "Sur le PC de référence, qui n’a pas servi à la passation", [
    "Ouvrir la même adresse dans Chrome, puis Espace adulte → Données → « Fusionner plusieurs tablettes » "
    "et sélectionner les dix fichiers en une seule fois. Les doublons sont écartés automatiquement : on "
    "peut réimporter sans risque.",
    "L’onglet Données affiche alors « Tablettes enregistrées » : le nombre doit correspondre au nombre de "
    "tablettes utilisées. S’il en manque une, c’est que son fichier n’a pas été importé — c’est le "
    "contrôle à faire avant tout envoi."])
num(pdf, 3, "Sur ce même PC, compléter et produire les documents", [
    "Réglages → Classes et effectifs : renseigner les effectifs des sept classes. Eux seuls permettent de "
    "calculer les taux de participation, par classe et par niveau. Inutile de le faire sur les tablettes.",
    "Rapport → « Imprimer / Enregistrer en PDF » pour le conseil des maîtres et la circonscription ; "
    "« Copier la synthèse » pour le courrier ou le message à l’IEN."])

h2(pdf, "Ce que montre le tableau de bord")
puce(pdf, "Vue d’ensemble", "les quatre indicateurs, la comparaison au baromètre national, "
     "l’interprétation rédigée, les faits les plus déclarés, et le nombre de tablettes fusionnées.")
puce(pdf, "Par classe, puis par niveau", "les sept classes, et le regroupement CE2 / CM1 / CM2 / CM1-CM2.")
puce(pdf, "Par question", "les 24 questions classées par fréquence : c’est ce qui désigne les thèmes de "
     "prévention à travailler en priorité.")
puce(pdf, "Élèves à recevoir", "les situations classées de la plus préoccupante à la moins préoccupante, "
     "avec les numéros de questions en jeu. Les questionnaires sans prénom restent anonymes et servent à "
     "l’analyse collective.")

encadre(pdf, "À ne pas faire",
        ["Vider l’historique ou les données de Chrome sur une tablette avant l’export.",
         "Changer de tablette en cours de route sans exporter celle qu’on quitte.",
         "Laisser un élève répondre deux fois : il compterait deux fois dans les statistiques.",
         "Consolider sur une tablette qui a servi à la passation alors qu’un PC est disponible : la "
         "confusion entre données locales et données fusionnées est alors inutile."],
        bg=(254, 242, 242), bord=(254, 202, 202), tc=ROUGE)

# ================== PAGE 7 — PRISE EN CHARGE ET LABELLISATION ==================
pdf.add_page()
h1(pdf, "Prise en charge et suite du dispositif", 18)

h2(pdf, "Que faire des élèves repérés", avant=1)
para(pdf, "C’est le point que le guide de passation impose, et celui que la circonscription regardera.")
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
    ("Axe 3 — Former", "Un protocole de passation commun à tous les collègues, réutilisable chaque année, "
     "accessible aux élèves à besoins particuliers (lecture audio, français simple)."),
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
puce(pdf, "5 novembre – 11 décembre 2026", "passation dans les sept classes, sur les dix tablettes.")
puce(pdf, "Décembre 2026", "consolidation sur le PC, conseil des maîtres, restitution aux familles.")
puce(pdf, "Janvier – mai 2027", "actions de prévention ciblées sur les thèmes sortis en tête.")
puce(pdf, "Juin 2027", "seconde passation avec la même application. La comparaison des deux mesures "
     "constitue la preuve qu’un dispositif fonctionne : c’est ce que demandent les dossiers de "
     "labellisation, et ce qui manque le plus souvent.", color=VERT)

h2(pdf, "Checklist avant transmission à la circonscription")
for item in ["Les dix tablettes ont été exportées et la fiche de suivi est complète.",
             "L’onglet Données affiche le nombre attendu de tablettes.",
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

# ========================= PAGE 8 — FICHE DE SUIVI =========================
fiche_suivi(pdf)

out = "/workspace/nah/mode-emploi-non-au-harcelement.pdf"
pdf.output(out)
print("PDF:", out, os.path.getsize(out), "octets,", pdf.page_no(), "pages")
