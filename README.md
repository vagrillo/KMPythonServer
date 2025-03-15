# KMPythonServer
Keyboard  and Mouse http server written in python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**KMPythonServer** è un server leggero scritto in Python che consente il controllo remoto di un computer tramite un'interfaccia web. Trasforma il browser del client in un terminale interattivo, replicando mouse, tastiera e comandi direttamente sul server host.

---

## ✨ Caratteristiche

- **Controllo Remoto via Browser**: Interagisci con il computer host attraverso una pagina web accessibile da qualsiasi dispositivo.
- **Webserver Integrato**: Basato su Flask, istanzia un server web su porta `8071` (configurabile).
- **Supporto per Mouse e Tastiera**: Cattura eventi dal browser e li replica in tempo reale sul server.
- **Interfaccia Minimalistica**: Pagina nera "canvas" per massimizzare la compatibilità e ridurre il carico.
- **Cross-Platform**: Compatibile con Windows, macOS e Linux (dipendenze permessi OS).

---

## 📦 Installazione

### Prerequisiti
- Python 3.8 o superiore
- Pip (Python Package Installer)

### Passaggi
1. Clona la repository:
   ```bash
   git clone https://github.com/yourusername/KMPythonServer.git
   cd KMPythonServer
