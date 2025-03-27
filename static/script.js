// Funktion zum Aktualisieren der Lebenspunkte
function updateStatus() {
    fetch("/status")
        .then(res => res.json())
        .then(data => {
            document.getElementById("leben-player").innerText = `Dein Leben: ${data.player_hp}`;
            document.getElementById("leben-enemy").innerText = `Gegner: ${data.enemy_hp}`;

            // Spielende prüfen
            if (data.player_hp <= 0) {
                alert("Game Over! Der Gegner hat gewonnen 😢");
                disableGame();
            } else if (data.enemy_hp <= 0) {
                alert("Du hast gewonnen! 🎉");
                disableGame();
            }
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
