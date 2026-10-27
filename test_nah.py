import json, sys
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8823/index.html"
SH = "/workspace/nah/shots"
OK, KO = [], []

def verif(nom, cond, detail=""):
    (OK if cond else KO).append(nom + ((" — " + str(detail)) if (detail and not cond) else ""))
    print(("  OK   " if cond else "  ECHEC ") + nom + (("  [" + str(detail) + "]") if detail and not cond else ""))

with sync_playwright() as pw:
    br = pw.chromium.launch(args=["--no-sandbox"])
    ctx = br.new_context(viewport={"width": 820, "height": 1180}, locale="fr-FR")
    p = ctx.new_page()
    errs = []
    p.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
    p.on("console", lambda m: errs.append("CONSOLE " + m.text) if m.type in ("error",) else None)

    p.goto(URL, wait_until="networkidle")
    verif("Page chargée", p.title().startswith("Non au harcèlement"), p.title())
    verif("Accueil : 3 boutons", p.locator("button.btn").count() >= 3, p.locator("button.btn").count())

    # ---------- 1. TABLE DE CROISEMENT OFFICIELLE ----------
    attendu = {}
    for A in range(0, 12):
        for BC in range(0, 15):
            r = 0 if A == 0 else (1 if A <= 2 else (2 if A <= 4 else 3))
            c = 0 if BC == 0 else (1 if BC <= 2 else (2 if BC <= 4 else (3 if BC <= 7 else 4)))
            T = [["rien","rien","surv","surv","harc"],
                 ["rien","rien","surv","surv","harc"],
                 ["surv","surv","surv","surv","harc"],
                 ["harc","harc","harc","harc","harc"]]
            attendu[(A, BC)] = T[r][c]
    tab = p.evaluate("""() => { const o=[]; for (let A=0;A<12;A++) for (let BC=0;BC<15;BC++) o.push([A,BC,statut(A,BC)]); return o; }""")
    mauvais = [(A, BC, s, attendu[(A, BC)]) for A, BC, s in tab if s != attendu[(A, BC)]]
    verif("Table A x (B+C) conforme à la grille officielle (180 combinaisons)", len(mauvais) == 0, mauvais[:5])

    # ---------- 2. PARCOURS ÉLÈVE COMPLET, AU CLIC ----------
    p.click("text=Je réponds au questionnaire")
    verif("Écran identité", "Avant de commencer" in p.inner_text("#app"))
    p.click("text=CM1")
    p.click("text=Une fille")
    verif("Bouton Continuer bloqué tant que l’année manque", p.locator("#btnGo").is_disabled())
    p.click("text=2017")
    verif("Bouton Continuer actif", not p.locator("#btnGo").is_disabled())
    p.click("#btnGo")
    verif("Écran consignes", "Comment répondre" in p.inner_text("#app"))
    p.screenshot(path=SH + "/01-consignes.png")
    p.click("text=Je commence")

    t = p.inner_text("#app")
    verif("Question 1 affichée", "1 / 24" in t, t[:80])
    verif("Texte officiel Q1", "As-tu peur sur le trajet de l’école" in t)
    verif("Reformulation présente", "En clair" in t)
    verif("4 modalités de réponse", p.locator(".opts .opt").count() == 4, p.locator(".opts .opt").count())
    p.screenshot(path=SH + "/02-question.png")

    # répond "Souvent" (3) à toutes les 24 questions
    for i in range(24):
        txt = p.inner_text("#app")
        assert ("%d / 24" % (i + 1)) in txt, txt[:60]
        p.click(".opts .opt.o3")
        p.wait_for_timeout(170)

    verif("Passage aux questions oui/non", "pour en savoir plus" in p.inner_text("#app").lower())
    p.screenshot(path=SH + "/03-oui-non.png")
    for g in range(3):
        n = p.locator(".yesno").count()
        for k in range(n):
            p.locator(".yesno button").nth(k * 2).click()
            p.wait_for_timeout(60)
        p.wait_for_timeout(360)

    verif("Écran prénom", "Tu peux écrire ton prénom" in p.inner_text("#app"))
    p.fill("#pn", "Test")
    p.screenshot(path=SH + "/04-prenom.png")
    p.click("text=Envoyer mes réponses")
    verif("Écran merci", "Merci" in p.inner_text("#app") and "3018" in p.inner_text("#app"))
    p.screenshot(path=SH + "/05-merci.png")

    r = p.evaluate("() => { const r=DB.rep[DB.rep.length-1]; return {n:r.q.length, s:calc(r), fini:r.fini, classe:r.classe}; }")
    verif("Questionnaire enregistré et complet", r["fini"] is True and r["n"] == 24, r)
    verif("A = 7 (Q2 a Q8 repondues 3)", r["s"]["A"] == 7, r["s"])
    verif("B = 10 (Q11 a Q20)", r["s"]["B"] == 10, r["s"])
    verif("C = 4 (Q21 a Q24, seuil 2)", r["s"]["C"] == 4, r["s"])
    verif("BC = 14", r["s"]["BC"] == 14, r["s"])
    verif("Statut harcèlement", r["s"]["statut"] == "harc", r["s"]["statut"])

    # ---------- 3. ESPACE ADULTE : PIN ----------
    p.click("text=Élève suivant")
    p.click("text=Espace adulte (résultats)")
    verif("Écran code", "Espace adulte" in p.inner_text("#app"))
    for c in ["1", "2", "3", "4"]:
        p.click(".pinpad button:text-is('%s')" % c)
    p.wait_for_timeout(400)
    verif("Code faux rejeté", "Code incorrect" in p.inner_text("#app"))
    p.screenshot(path=SH + "/06-code.png")
    for c in ["2", "0", "2", "6"]:
        p.click(".pinpad button:text-is('%s')" % c)
    p.wait_for_timeout(500)
    t = p.inner_text("#app")
    verif("Espace adulte ouvert", "Vue d’ensemble" in t)
    verif("KPI 1 questionnaire", "1" in t)

    # ---------- 4. JEU DE DONNÉES SYNTHÉTIQUE ----------
    jeu = p.evaluate("""() => {
      DB.rep = [];
      const cs = ['CM1','CM2','CE2'];
      function mk(cl, niveau, i) {
        const q = []; for (let k=0;k<24;k++) q.push(1);
        // niveau 0 = RAS, 1 = surveiller, 2 = harcelement
        if (niveau === 1) { q[1]=3; q[2]=3; q[3]=3; q[10]=3; q[11]=3; }
        if (niveau === 2) { q[1]=4; q[2]=4; q[3]=3; q[6]=4; q[7]=3; q[6]=4;
                            q[10]=4; q[12]=4; q[13]=4; q[14]=4; q[16]=3; q[18]=4; q[19]=4; q[20]=4; }
        return {id:'T'+cl+i, ts:'2026-11-05T09:00:00Z', classe:cl, sexe:'fille', annee:'2017',
                q:q, plus:{memes:'oui',aideEleve:'non',aideParent:'oui',aideAdulte:'non',ami:'oui',
                           n3018:'non',auteur:'non',temEcole:'oui',temClasse:'oui'},
                prenom:'', fini:true};
      }
      let n=0;
      for (let c=0;c<3;c++) {                 // 3 classes x 10 eleves
        for (let i=0;i<10;i++) {
          const niv = i<1 ? 2 : (i<4 ? 1 : 0);   // 1 harcelement, 3 surveiller, 6 RAS
          DB.rep.push(mk(cs[c], niv, i));
        }
      }
      // cas graves : un eleve avec attouchements declares
      const g = mk('CM2', 2, 99); g.q[22]=3; g.q[21]=2; g.prenom='EleveGrave'; g.q[18]=4;
      DB.rep.push(g);
      DB.cfg.classesTxt = 'CE2 ; 10\\nCM1 ; 12\\nCM2 ; 11';
      localStorage.setItem('nah_v1', JSON.stringify(DB));
      return DB.rep.length;
    }""")
    verif("Jeu de test injecté (31 questionnaires)", jeu == 31, jeu)
    p.goto(URL, wait_until="networkidle")
    p.click("text=Espace adulte (résultats)")
    for c in ["2", "0", "2", "6"]:
        p.click(".pinpad button:text-is('%s')" % c)
    p.wait_for_timeout(500)

    a = p.evaluate("() => { const a = analyse(); return {n:a.n, harc:a.harc, surv:a.surv, rien:a.rien, tH:a.tauxH, tS:a.tauxS, eff:a.effectif, part:a.part, graves:a.graves, alertes:a.alertes.length}; }")
    verif("31 questionnaires analysés", a["n"] == 31, a)
    verif("4 harcèlement", a["harc"] == 4, a["harc"])
    verif("9 à surveiller", a["surv"] == 9, a["surv"])
    verif("18 sans difficulté", a["rien"] == 18, a["rien"])
    verif("Effectif total 33", a["eff"] == 33, a["eff"])
    verif("Faits graves détectés", a["graves"] >= 1, a["graves"])
    verif("Alertes = harc + surv", a["alertes"] == a["harc"] + a["surv"], a["alertes"])
    p.screenshot(path=SH + "/07-vue-ensemble.png", full_page=True)

    txt = p.inner_text("#app")
    verif("Interprétation générée", "Interprétation" in txt and "repère national" in txt)
    verif("Comparaison baromètre affichée", "baromètre national" in txt)

    # onglets
    for ong in ["Par classe", "Par question", "Élèves à recevoir"]:
        p.click(".tab:text-is('%s')" % ong)
        p.wait_for_timeout(250)
        tt = p.inner_text("#app")
        verif("Onglet %s non vide" % ong, len(tt) > 250, len(tt))
        if ong == "Élèves à recevoir":
            verif("Élève nommé repéré", "EleveGrave" in tt)
            verif("Faits graves signalés en Q", "Q23" in tt)
            p.screenshot(path=SH + "/08-eleves.png", full_page=True)
        if ong == "Par classe":
            verif("Tableau par classe : lignes CE2/CM1/CM2", all(x in tt for x in ["CE2", "CM1", "CM2", "École"]))
            verif("Tableau par classe : taux de participation", "100 %" in tt, tt[:200])
        if ong == "Par question":
            verif("24 barres de questions", p.locator(".bars").first.locator(".bar").count() == 24,
                  p.locator(".bars").first.locator(".bar").count())
            p.screenshot(path=SH + "/09-questions.png", full_page=True)

    # ---------- 5. RAPPORT IMPRIMABLE ----------
    p.click(".tab:text-is('Rapport')")
    p.wait_for_timeout(300)
    p.screenshot(path=SH + "/10-rapport-ecran.png", full_page=True)
    p.emulate_media(media="print")
    p.pdf(path="/workspace/nah/shots/rapport.pdf", format="A4", print_background=True)
    p.emulate_media(media="screen")
    import os
    verif("PDF du rapport généré", os.path.exists("/workspace/nah/shots/rapport.pdf") and
          os.path.getsize("/workspace/nah/shots/rapport.pdf") > 20000,
          os.path.getsize("/workspace/nah/shots/rapport.pdf") if os.path.exists("/workspace/nah/shots/rapport.pdf") else 0)

    # ---------- 6. EXPORT / IMPORT ----------
    p.click(".tab:text-is('Données')")
    p.wait_for_timeout(200)
    verif("Boutons export présents", "Sauvegarde complète" in p.inner_text("#app"))
    with p.expect_download() as dl:
        p.click("text=Sauvegarde complète")
    d = dl.value
    chemin = "/tmp/nah-export.json"
    d.save_as(chemin)
    data = json.load(open(chemin))
    verif("Export JSON : 31 réponses", len(data["rep"]) == 31, len(data["rep"]))
    verif("Export JSON : configuration incluse", data["cfg"]["nom"] != "")

    with p.expect_download() as dl2:
        p.click("text=Tableau anonyme")
    d2 = dl2.value
    d2.save_as("/tmp/nah-export.csv")
    csv = open("/tmp/nah-export.csv", encoding="utf-8-sig").read().strip().split("\n")
    verif("Export CSV : 31 lignes + en-tête", len(csv) == 32, len(csv))
    verif("CSV sans prénom", "EleveGrave" not in open("/tmp/nah-export.csv", encoding="utf-8-sig").read())
    verif("CSV 24 colonnes Q", csv[0].count("Q") == 24, csv[0])

    # fusion : réimport du même fichier = 0 doublon ajouté
    p.set_input_files("#fj", chemin)
    p.wait_for_timeout(600)
    mess = p.evaluate("() => DB.rep.length")
    verif("Réimport du même fichier : aucun doublon", mess == 31, mess)

    # ---------- 7. MOBILE ----------
    ctx2 = br.new_context(viewport={"width": 390, "height": 844}, locale="fr-FR",
                          user_agent="Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36")
    p2 = ctx2.new_page()
    e2 = []
    p2.on("pageerror", lambda e: e2.append(str(e)))
    p2.goto(URL, wait_until="networkidle")
    p2.click("text=Je réponds au questionnaire")
    p2.click("text=CM2")
    p2.click("text=Un garçon")
    p2.click("text=2016")
    p2.click("#btnGo")
    p2.click("text=Je commence")
    p2.wait_for_timeout(300)
    p2.screenshot(path=SH + "/11-mobile-question.png")
    debord = p2.evaluate("() => document.documentElement.scrollWidth > window.innerWidth + 2")
    verif("Mobile : aucun débordement horizontal", not debord)
    verif("Mobile : pas d’erreur JS", len(e2) == 0, e2)

    # ---------- 8. ERREURS ----------
    verif("Aucune erreur JS sur tout le parcours", len(errs) == 0, errs[:4])

    br.close()

print("\n==== %d OK / %d ECHEC ====" % (len(OK), len(KO)))
if KO:
    print("ÉCHECS :")
    for k in KO:
        print("  - " + k)
    sys.exit(1)
