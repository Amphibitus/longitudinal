# 📈 QGIS-Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Status](https://img.shields.io/badge/Status-Experimental-yellow.svg)
![Version](https://img.shields.io/badge/Version-0.8-blue.svg)

**Longitudinal** ist ein spezialisiertes QGIS-Werkzeug zur Erzeugung von Längsschnitten (Profilen) entlang von Linien- und Punktdaten. Es vereinfacht die Visualisierung von Höhenverläufen für Planer, Ingenieure und Vermesser.

---

## 📖 Überblick

Das Plugin generiert präzise Höhenprofile direkt aus deinen GIS-Daten. Ein besonderes Highlight ist die Export-Schnittstelle, die den Sprung vom GIS in die CAD-Welt ermöglicht.

* **Entwickler:** Gerd Dreier (geoplaning GmbH) / [Amphibitus](https://github.com/Amphibitus)
* **Kategorie:** Ingenieurbau / Wasserwirtschaft / Vermessung
* **CAD-Anbindung:** Integrierter **DXF-Export**.

---

## 🖼️ Plugin-Icons & Funktionen

Die folgenden Symbole steuern die Kernfunktionen des Plugins (zu finden im `/icons` Ordner):

| Icon | Name | Funktion |
| :---: | :--- | :--- |
| <img src="icons/longitudinal.png" width="32"> | **Main** | Startet das Hauptfenster für die Längsschnitt-Berechnung. |
| <img src="icons/lines.png" width="32"> | **Lines** | Auswahl und Management der Achslinien (Trassen). |
| <img src="icons/points.png" width="32"> | **Points** | Einbeziehung von Punktdaten (z.B. Schächte oder Messpunkte). |
| <img src="icons/mActionOptions.png" width="32"> | **Options** | Einstellungen für die Profildarstellung und Überhöhung. |
| <img src="icons/mActionHelp.png" width="32"> | **Help** | Öffnet die lokale Hilfe oder das Online-Wiki. |

---

## ✨ Features

* **Profilauswertung:** Erzeugt Längsschnitte basierend auf Liniengeometrien und Punkt-Layern.
* **💾 DXF-Export:** Exportiere deinen fertigen Längsschnitt als **DXF-Datei** zur nahtlosen Weiterverarbeitung in AutoCAD, BricsCAD oder Civil 3D.
* **Zweite Höhenlinie:** Unterstützung für eine zusätzliche Referenzlinie (z. B. Gelände-Oberkante vs. Rohr-Sohle).
* **Dynamische Höhen (v0.8):** Die Höhe der zweiten Profillinie kann interaktiv im Dialog angepasst werden.
* **Skalierbarkeit:** Unterstützung für verschiedene Maßstäbe und vertikale Überhöhungen.

---

## 🛠 Installation

### Über QGIS (Empfohlen)
1. Öffne den QGIS **Erweiterungen-Manager**.
2. Suche nach **"Longitudinal"**.
3. Klicke auf **Installieren**.
   *(Wichtig: Stelle sicher, dass in den Einstellungen "Auch experimentelle Erweiterungen anzeigen" aktiviert ist.)*

### Manuelle Installation
1. Lade dieses Repository als ZIP herunter.
2. Entpacke es in deinen Plugin-Ordner (meist unter `%AppData%\Roaming\QGIS\QGIS3\profiles\default\python\plugins`).
3. Starte QGIS neu.

---

## 🚀 Workflow in Kürze

1. **Achse wählen:** Markiere den Linienlayer, der den Verlauf deines Profils definiert.
2. **Datenquellen:** Wähle die Layer aus, die die Z-Werte (Höhen) liefern.
3. **Generieren:** Erzeuge die Profilgrafik in der Plugin-Vorschau.
4. **Export:** Nutze den Export-Button, um eine **DXF-Datei** für CAD zu erstellen.

---

## 🤝 Support & Feedback

Fehler gefunden? Ideen für neue Features? 
* Erstelle ein **Issue** direkt hier im [GitHub-Repository](https://github.com/Amphibitus/longitudinal/issues).
* Besuche das [Wiki](https://github.com/Amphibitus/longitudinal/wiki) für weitere Details.

---
*Entwickelt von geoplaning GmbH – Engineering-Tools für QGIS.*
