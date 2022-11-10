import http.client
import json

class EcoleDirecteManager:
    def __init__(self, username, password) -> None:
        print("Chargement...")
        self.username = username
        self.password = password
        self.francais = []
        self.francaisClasse = []
        self.maths = []
        self.mathsClasse = []
        self.anglais = []
        self.anglaisClasse = []
        self.espagnol_allemand = []
        self.espagnol_allemandClasse = []
        self.svt = []
        self.svtClasse = []
        self.ph_ch = []
        self.ph_chClasse = []
        self.hi_ge = []
        self.hi_geClasse = []
        self.a_pla = []
        self.a_plaClasse = []
        # self.options = []
        self.login()

    def login(self):
        conn = http.client.HTTPSConnection("api.ecoledirecte.com")
        payload = 'data={"identifiant":'+f'"{self.username}"'+',"motdepasse":'+f'"{self.password}"'+'}'
        headers = {
                    'authority': 'api.ecoledirecte.com',
                    'accept': 'application/json, text/plain, */*',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'sec-gpc': '1',
                    'origin': 'https://www.ecoledirecte.com',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.ecoledirecte.com/',
                    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
                }
        conn.request("POST", "/v3/login.awp", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        self.data = data
        conn.request("POST", "/v3/login.awp", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        self.data = data
        if 'code' in data == 200:
            self.accountData = data['data']['accounts'][0]
            self.token = data['token']
            self.studentId = data['data']['accounts'][0]['id']
            print("La connexion a fonctionnée !")
            print("ECOLE DIRECTE MANAGER - " + self.accountData['prenom'])
            self.ProcessNotes()
            self.ProcessMoyennes()
            self.login()
            return data
        else:
            print("désolé, une erreur a surgi lors de la connexion : " + data['message'] + ", error " + str(data['code']))
            return


    def GetBrutNotes(self):
        conn = http.client.HTTPSConnection("api.ecoledirecte.com")
        payload = 'verbe=get&v=4.19.0&data={"token":"' + self.token + '", "anneeScolaire": ""}'
        headers = {
            'authority': 'api.ecoledirecte.com',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-gpc': '1',
            'origin': 'https://www.ecoledirecte.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.ecoledirecte.com/',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'X-Token': self.token
        }
        conn.request("POST", "/v3/eleves/" + str(self.studentId) + "/notes.awp", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        self.brutNotes = data
        self.allNotes = data['data']['notes']
        return data

    def ProcessNotes(self):
        self.GetBrutNotes()
        for i in self.allNotes:
            if i['moyenneClasse'] != "":
                if i['codeMatiere'] == "FRANC":
                    if i['valeur'] != "Abs":
                        self.francais.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.francaisClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "MATHS":
                    if i['valeur'] != "Abs":
                        self.maths.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.mathsClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "AGL1":
                    if i['valeur'] != "Abs":
                        self.anglais.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.anglaisClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "ESP2":
                    if i['valeur'] != "Abs":
                        self.espagnol_allemand.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.espagnol_allemandClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "ALM2":
                    if i['valeur'] != "Abs":
                        self.espagnol_allemand.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.espagnol_allemandClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "SVT":
                    if i['valeur'] != "Abs":
                        self.svt.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.svtClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "PH-CH":
                    if i['valeur'] != "Abs":
                        self.ph_ch.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.ph_chClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "HI-GE":
                    if i['valeur'] != "Abs":
                        self.hi_ge.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.hi_geClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                elif i['codeMatiere'] == "A-PLA":
                    if i['valeur'] != "Abs":
                        self.a_pla.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                    self.a_plaClasse.append([i['devoir'], float(str(i['moyenneClasse']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])
                # else:
                    # if i['valeur'] != "Abs":
                        # self.options.append([i['devoir'], float(str(i['valeur']).replace(",", ".")) * 20 / float(str(i['noteSur']).replace(",", "."))])

    
    def ProcessMoyennes(self):

        francaisNotes = []
        mathsNotes = []
        anglaisNotes = []
        esp_almNotes = []
        svtNotes = []
        ph_chNotes = []
        hi_geNotes = []
        a_plaNotes = []
        francaisClassNotes = []
        mathsClassNotes = []
        anglaisClassNotes = []
        esp_almClassNotes = []
        svtClassNotes = []
        ph_chClassNotes = []
        hi_geClassNotes = []
        a_plaClassNotes = []

        for i in self.francais:
            francaisNotes.append(i[1])
        for i in self.maths:
            mathsNotes.append(i[1])
        for i in self.anglais:
            anglaisNotes.append(i[1])
        for i in self.espagnol_allemand:
            esp_almNotes.append(i[1])
        for i in self.svt:
            svtNotes.append(i[1])
        for i in self.ph_ch:
            ph_chNotes.append(i[1])
        for i in self.hi_ge:
            hi_geNotes.append(i[1])
        for i in self.a_pla:
            a_plaNotes.append(i[1])
        for i in self.francaisClasse:
            francaisClassNotes.append(i[1])
        for i in self.mathsClasse:
            mathsClassNotes.append(i[1])
        for i in self.anglaisClasse:
            anglaisClassNotes.append(i[1])
        for i in self.espagnol_allemandClasse:
            esp_almClassNotes.append(i[1])
        for i in self.svtClasse:
            svtClassNotes.append(i[1])
        for i in self.ph_chClasse:
            ph_chClassNotes.append(i[1])
        for i in self.hi_geClasse:
            hi_geClassNotes.append(i[1])
        for i in self.a_plaClasse:
            a_plaClassNotes.append(i[1])


        self.francaisAverage = sum(francaisNotes) / len(francaisNotes)
        self.francaisClasseAverage= sum(francaisClassNotes) / len(francaisClassNotes)
        self.mathsAverage = sum(mathsNotes) / len(mathsNotes)
        self.mathsClasseAverage = sum(mathsClassNotes) / len(mathsClassNotes)
        self.anglaisAverage = sum(anglaisNotes) / len(anglaisNotes)
        self.anglaisClasseAverage = sum(anglaisClassNotes) / len(anglaisClassNotes)
        self.espagnol_allemandAverage = sum(esp_almNotes) / len(esp_almNotes)
        self.espagnol_allemandClasseAverage = sum(esp_almClassNotes) / len(esp_almClassNotes)
        self.svtAverage = sum(svtNotes) / len(svtNotes)
        self.svtClasseAverage = sum(svtClassNotes) / len(svtClassNotes)
        self.ph_chAverage = sum(ph_chNotes) / len(ph_chNotes)
        self.ph_chClasseAverage = sum(ph_chClassNotes) / len(ph_chClassNotes)
        self.hi_geAverage = sum(hi_geNotes) / len(hi_geNotes)
        self.hi_geClasseAverage = sum(hi_geClassNotes) / len(hi_geClassNotes)
        self.a_plaAverage = sum(a_plaNotes) / len(a_plaNotes)
        self.a_plaClasseAverage = sum(a_plaClassNotes) / len(a_plaClassNotes)
        
        self.totalAverage = (self.francaisAverage + self.mathsAverage + self.anglaisAverage + self.espagnol_allemandAverage + self.svtAverage + self.ph_chAverage + self.hi_geAverage + self.a_plaAverage) / 8
        self.totalClassAverage = (self.francaisClasseAverage + self.mathsClasseAverage + self.anglaisClasseAverage + self.espagnol_allemandClasseAverage + self.svtClasseAverage + self.ph_chClasseAverage + self.hi_geClasseAverage + self.a_plaClasseAverage) / 8
        
        print("Voici votre moyenne : " + str(manager.totalAverage))
        print("Voici la moyenne de la classe : " + str(manager.totalClassAverage))
