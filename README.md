# 📈 QGIS-Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Version](https://img.shields.io/badge/Version-0.8-blue.svg)

**Longitudinal** ist ein spezialisiertes QGIS-Werkzeug zur Erzeugung von Längsschnitten (Profilen) entlang von Linien- und Punktdaten. Es vereinfacht die Visualisierung von Höhenverläufen für Planer, Ingenieure und Vermesser.

---

## 📖 Überblick

Das Plugin generiert präzise Höhenprofile direkt aus deinen GIS-Daten. Ein besonderes Highlight ist die Export-Schnittstelle, die den nahtlosen Übergang vom GIS in die CAD-Planung ermöglicht.

* **Kategorie:** Ingenieurbau / Wasserwirtschaft / Vermessung
* **CAD-Anbindung:** Integrierter **DXF-Export**.

---

## ✨ Kernfunktionen

* **Profilauswertung:** Erzeugt Längsschnitte basierend auf Liniengeometrien und Punkt-Layern.
* **💾 DXF-Export:** Exportiere den fertigen Längsschnitt als **DXF-Datei** zur Weiterverarbeitung in AutoCAD, BricsCAD oder Civil 3D.
* **Zweite Höhenlinie:** Unterstützung für eine zusätzliche Referenzlinie (z. B. Gelände-Oberkante vs. Rohr-Sohle/Graben-Sohle).
* **Dynamische Höhen (v0.8):** Die Höhe der zweiten Profillinie kann interaktiv im Dialog angepasst werden.
* **Skalierbarkeit:** Unterstützung für verschiedene Maßstäbe und vertikale Überhöhungen.

---

## 🛠 Installation

### Über QGIS (Empfohlen)
1. Öffne den QGIS **Erweiterungen-Manager** (Plugins).
2. Suche nach **"Longitudinal"**.
3. Klicke auf **Installieren**.
   *(Hinweis: Stelle sicher, dass in den Einstellungen "Auch experimentelle Erweiterungen anzeigen" aktiviert ist.)*

### Manuelle Installation
1. Lade dieses Repository als ZIP herunter.
2. Entpacke es in deinen QGIS-Plugin-Ordner:
   `%AppData%\Roaming\QGIS\QGIS3\profiles\default\python\plugins` (Windows-Standardpfad).
3. Starte QGIS neu und aktiviere das Plugin.
