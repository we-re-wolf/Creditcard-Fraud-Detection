function parseCollectiveData() {
    const collectiveData = document.getElementById("collectiveData").value.trim();
    if (collectiveData) {
        const values = collectiveData.split(',').map(Number);
        if (values.length === 30) {
            const fieldIds = ["Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", 
                              "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", 
                              "V25", "V26", "V27", "V28", "Amount"];
            fieldIds.forEach((id, index) => {
                document.getElementById(id).value = values[index];
            });
        } else {
            alert("Please ensure 30 comma-separated values are provided.");
        }
    }
}
function submitForm() {
    const fieldIds = ["Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", 
                      "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", 
                      "V25", "V26", "V27", "V28", "Amount"];
    
    const data = {};
    fieldIds.forEach(id => {
        data[id] = parseFloat(document.getElementById(id).value);
    });

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText = result.prediction >= 1 
            ? "High likelihood of fraud detected." 
            : "Transaction is likely safe.";
    })
    .catch(error => console.error("Error:", error));
}
