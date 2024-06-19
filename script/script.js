document.addEventListener("DOMContentLoaded", function() {
    var checkbox = document.getElementById("myonoffswitch");
    var resultatsBruts = document.getElementById("res_brut");
    var resultatsNormaux = document.getElementById("res_map");

    checkbox.addEventListener("change", function() {
        if (checkbox.checked) {
            resultatsBruts.classList.remove("hidden");
            resultatsNormaux.classList.add("hidden");
        } else {
            resultatsBruts.classList.add("hidden");
            resultatsNormaux.classList.remove("hidden");
        }
    });
});

function fetchResults() {
    var checked_alerts = document.querySelectorAll('#alert_filter input[type="checkbox"]:checked');

    var alert_values = [];
    checked_alerts.forEach(function(checkbox) {
        console.log(checkbox.name)
        if (checkbox.name === "urgence")
            alert_values.push("appelUrgence")
        else if (checkbox.name === "accident")
            alert_values.push("appelAssistanceAccident")
        else if (checkbox.name === "panne")
            alert_values.push("appelAssistancePanne")
        else if (checkbox.name === "erreur")
            alert_values.push("erreurAppel")
        else if (checkbox.name === "autre")
            alert_values.push("autre")
});

    var checked_vehicles = document.querySelectorAll('#vehicule_filter input[type="checkbox"]:checked');

// Créer un tableau pour stocker les valeurs des cases à cocher sélectionnées pour les véhicules impliqués
var vehicle_values = [];

// Parcourir les inputs cochés et ajouter leurs valeurs au tableau
checked_vehicles.forEach(function(checkbox) {
    vehicle_values.push(checkbox.name); // Utiliser name ou value en fonction de ce que vous voulez récupérer
});
let test = alert_values.join(',')
console.log({test})
    var date_debut = document.getElementById('dateStart').value;
    var date_fin = document.getElementById('dateEnd').value;
    var url = '/query?type_alerte=' + encodeURIComponent(alert_values.join(',')) +
              '&vehicule_implique=' + encodeURIComponent(vehicle_values.join(',')) +
              '&date_debut=' + encodeURIComponent(date_debut) +
              '&date_fin=' + encodeURIComponent(date_fin);

    fetch('http://localhost:5000'+url)
        .then(response => response.json())
        .then(data => displayResults(data))
        .catch(error => console.error('Error:', error));
}

function displayResults(results) {
    var tableBody = document.getElementById('results_table_body');
    tableBody.innerHTML = ''; // Vide le contenu actuel du tableau

    console.log(results);
    results.forEach(function(row) {
        var tr = document.createElement('tr');

        // Ajoutez des cellules pour chaque colonne de résultat
        var td1 = document.createElement('td');
        td1.textContent = row.uuid;
        tr.appendChild(td1);

        var td2 = document.createElement('td');
        td2.textContent = row.code_postal;
        tr.appendChild(td2);

        var td3 = document.createElement('td');
        td3.textContent = row.coordonnee_lat;
        tr.appendChild(td3);

        var td4 = document.createElement('td');
        td4.textContent = row.coordonnee_long;
        tr.appendChild(td4);

        var td5 = document.createElement('td');
        td5.textContent = row.type_data;
        tr.appendChild(td5);

        var td6 = document.createElement('td');
        td6.textContent = row.type_alerte;
        tr.appendChild(td6);

        var td7 = document.createElement('td');
        td7.textContent = row.type_vehicule;
        tr.appendChild(td7);

        var td8 = document.createElement('td');
        td8.textContent = row.event_date_time;
        tr.appendChild(td8);

        var td9 = document.createElement('td');
        td9.textContent = row.accident_date_time;
        tr.appendChild(td9);

        tableBody.appendChild(tr);
    });
}
