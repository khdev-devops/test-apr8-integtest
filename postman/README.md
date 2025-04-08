# Övning: Från manuell testning till automatiserat systemtest (Postman + Newman)

I denna övning kommer du att testa en webbaserad API-applikation:
- Först **manuellt** (explorativt) i Postman
- Sedan skapa automatiska testfall
- Till sist köra dessa med **Newman** från terminalen

Du tränar på att tänka som en testare: vad vill du verifiera? Hur vet du att något fungerar?

## Förberedelser

Innan du börjar, se till att du har:
- Klonat detta projekt
- Startat appen med `python app/main.py` (från projektets rotkatalog)
- Installerat **Postman**: https://www.postman.com/downloads/

---

## Del 1: Utforska API:et

### 1.1 Skapa en ny samling i Postman

- Lägg till ett `POST /note`-anrop med en JSON-body (välj raw under fliken body) som innehåller ett fält `text`
- Lägg till ett `GET /`-anrop

### 1.2 Prova olika inputs
- Vad händer om du skickar tom text?
- Hur ser svaret ut när du lagt till flera anteckningar?
- Kan du lista ut vilket format datan har?

Reflektera:  
- Vilka problem eller gränsfall hittade du när du testade manuellt?

---

## Del 2: Skriv tester i Postman

I varje request kan du lägga till **testfall** (under `Scripts > Post-response` fliken).

Läs dokumentationen: https://learning.postman.com/docs/writing-scripts/script-references/test-examples/

### 2.1 Lägg till minst 2 testfall per request:
- Ett test som kollar **statuskod**
- Ett test som kollar **innehåll**

Tänk själv – vad vill du att API:et ska svara med?  
- Tips: använd `pm.expect(...)` och `pm.response...`

Fundera:
- Vad testar du egentligen nu?  
- Vad händer om implementationen ändras?

---

## Del 3: Exportera och kör test automatiskt

### Exportera samlingen

I Postman:  
- Klicka på samlingen → "..." → ("More") → "Export"
- Välj v2.1-format

### Installera och kör Newman

Installera Newman om du inte redan har det:

```bash
npm install -g newman
```

Kör din exporterade samling:

```bash
newman run dinfil.postman_collection.json
```

Läs mer:  
https://www.npmjs.com/package/newman

### Reflektera efter körning:
- Vilket av dessa testfall hade kunnat gå sönder om API:et ändrades?
- På vilket sätt är detta ett systemtest?
- Hur skulle du kunna automatisera detta ännu mer?

---

## Extra för den nyfikne

- Skapa ett `testdata.json`-fil och använd variabler i Postman
- Utforska hur du kan logga testresultat som en rapport (`--reporters cli,json`)

---

## Summering

- Del 1: Utforskat API:et manuellt
- Del 2: Lagt till testfall i Postman
- Del 3: Kört tester automatiserat med Newman

Fundera:
- Vad är styrkan i att ha både manuell testning och automatiserade testfall?
- När ska man använda vilket?
- Hur skiljer sig dessa test från integrationstest?
