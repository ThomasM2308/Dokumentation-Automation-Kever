import matplotlib.pyplot as plt
import numpy as np

# Betrachtungszeitraum in Monaten (Monat 0 bis 12)
monate = np.array(range(13))

# Daten aus den Texten (auf den Monat heruntergebrochen)
investition_einmalig = 3000.00        # Einmalige Implementierungskosten im Monat 0
kosten_ist_pro_monat = 66000.00 / 12  # 5.500,00 € pro Monat im Ist-Zustand
kosten_ziel_pro_monat = 39646.08 / 12 # ~3.303,84 € pro Monat im Zielzustand (inkl. Betrieb)

# Kumulierte Gesamtkosten über die Monate berechnen
kum_ist = kosten_ist_pro_monat * monate
kum_ziel = investition_einmalig + (kosten_ziel_pro_monat * monate)

# Diagramm erstellen
plt.figure(figsize=(10, 5.5))
plt.plot(monate, kum_ist, marker='o', color='#d9534f', linewidth=2.5, label='Ist-Zustand (Ohne KI-Support)')
plt.plot(monate, kum_ziel, marker='s', color='#5cb85c', linewidth=2.5, label='Ziel-Zustand (Mit KI-Support)')

# Beschriftungen und Layout
plt.title('Kumulierter Kostenverlauf', fontsize=13, fontweight='bold')
plt.xlabel('Zeitraum in Monaten', fontsize=11)
plt.ylabel('Kumulierte Gesamtkosten in €', fontsize=11)
plt.xticks(monate)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='upper left')

# Werte am Jahresende (Monat 12) anzeigen
plt.annotate(f"{kum_ist[-1]:,.0f} €".replace(",", "."), (monate[-1], kum_ist[-1]), textcoords="offset points", xytext=(-25,10), color='#d9534f', fontweight='bold')
plt.annotate(f"{kum_ziel[-1]:,.0f} €".replace(",", "."), (monate[-1], kum_ziel[-1]), textcoords="offset points", xytext=(-25,-20), color='#2e7d32', fontweight='bold')

plt.tight_layout()

# Als PNG speichern
plt.savefig('roi_verlauf_jahr.png', dpi=300)
plt.show()