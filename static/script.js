async function predictDisease() {
    const selectedSymptoms = [];
    document.querySelectorAll('#symptom-list input:checked').forEach((checkbox) => {
        selectedSymptoms.push(checkbox.value);
    });

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ symptoms: selectedSymptoms }),
    });

    const data = await response.json();

    // Display predicted disease
    document.getElementById('result').innerText = "Predicted Disease: " + data.prediction;

    // Display vitals comparison
    let vitalsTable = `
        <h2>Patient Vitals vs Normal Ranges</h2>
        <table>
            <tr><th>Vital Sign</th><th>Patient Value</th><th>Normal Range</th></tr>
    `;

    for (const [key, value] of Object.entries(data.vitals)) {
        vitalsTable += `<tr>
            <td>${key}</td>
            <td>${value}</td>
            <td>${data.normal_ranges[key]}</td>
        </tr>`;
    }
    vitalsTable += `</table>`;

    document.getElementById('vitals').innerHTML = vitalsTable;
}
