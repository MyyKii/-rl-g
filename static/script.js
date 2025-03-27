// Funktion zum Aktualisieren der Lebenspunkte
function updateStatus() {
    fetch("/status")
        .then(res => res.json())
        .then(data => {
            document.getElementById("leben-player-1").innerText = `Spieler 1: ${data.player_1_hp} HP`;
            document.getElementById("leben-player-2").innerText = `Spieler 2: ${data.player_2_hp} HP`;

            // 🆕 Aktiven Spieler anzeigen
            const activePlayer = data.active_player === 1 ? "Spieler 1" : "Spieler 2";
            document.getElementById("active-player-info").innerText = `Aktiver Spieler: ${activePlayer}`;

            // Optional: Buttons deaktivieren, wenn nicht dran
            document.getElementById("turn_1").disabled = data.active_player !== 1;
            document.getElementById("turn_2").disabled = data.active_player !== 2;

        })
        .catch(err => {
            console.error("Status konnte nicht geladen werden:", err);
        });
}


// Buttons deaktivieren bei Spielende
function disableGame() {
    document.getElementById("roll-btn").disabled = true;
    document.getElementById("lose_hp").disabled = true;
    document.getElementById("add_hp").disabled = true;
}

// Wenn Seite geladen ist...
document.addEventListener("DOMContentLoaded", () => {
    updateStatus();

    // Würfeln
    document.getElementById("roll-btn").addEventListener("click", () => {
        fetch("/roll")
            .then(res => res.json())
            .then(data => {
                document.getElementById("dice-result").innerText = "🎲 Ergebnis: " + data.join(" ");
                updateStatus();
            })
            .catch(error => {
                document.getElementById("dice-result").innerText = "Fehler beim Würfeln 😢";
                console.error("Fehler:", error);
            });
    });

    // HP abziehen
    document.getElementById("lose_hp").addEventListener("click", () => {
        fetch("/lose", { method: "POST" })
            .then(res => res.json())
            .then(data => {
                console.log(data.message);
                updateStatus();
            })
            .catch(err => {
                console.error("Fehler beim HP-Abziehen:", err);
            });
    });

    // HP hinzufügen
    document.getElementById("add_hp").addEventListener("click", () => {
        fetch("/add", { method: "POST" })
            .then(res => res.json())
            .then(data => {
                console.log(data.message);
                updateStatus();
            })
            .catch(err => {
                console.error("Fehler beim HP-Hinzufügen:", err);
            });
    });
});

document.getElementById("restart").addEventListener("click", () => {
    fetch("/restart", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            alert(data.message); // "Spiel wurde neu gestartet"
            updateStatus();

            // Buttons wieder aktivieren
            document.getElementById("roll-btn").disabled = false;
            document.getElementById("lose_hp").disabled = false;
            document.getElementById("add_hp").disabled = false;
        })
        .catch(err => {
            console.error("Fehler beim Neustart:", err);
        });
});

document.getElementById("turn_1").addEventListener("click", () => {
    fetch("/turn_1", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            console.log(data.message);
            updateStatus();
            if (data.status) alert(data.status);
        });
});

document.getElementById("turn_2").addEventListener("click", () => {
    fetch("/turn_2", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            console.log(data.message);
            updateStatus();
            if (data.status) alert(data.status);
        });
});
