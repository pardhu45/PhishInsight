const analyzeButton = document.getElementById("analyzeButton");
const urlInput = document.getElementById("urlInput");
const analysisStatus = document.getElementById("analysisStatus");
const threatLevel = document.getElementById("threatLevel");
const riskScore = document.getElementById("riskScore");
if (analyzeButton) {
    analyzeButton.addEventListener("click", () => {

        if (urlInput.value.trim() === "") {
            analysisStatus.textContent = "Please enter a URL.";
            analysisStatus.className = "text-red-400";
            return;
        }

        analysisStatus.textContent = "Analyzing URL...";
        analysisStatus.className = "text-blue-400";

    });
}

const historySearch = document.getElementById("historySearch");
const threatFilter = document.getElementById("threatFilter");

function filterHistory() {

    const searchTerm = historySearch ? historySearch.value.toLowerCase() : "";
    const selectedThreat = threatFilter ? threatFilter.value : "ALL";

    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {

        const url = row.cells[0].textContent.toLowerCase();
        const threatLevel = row.cells[1].textContent.trim();

        const matchesSearch = url.includes(searchTerm);

        const matchesThreat =
            selectedThreat === "ALL" ||
            threatLevel === selectedThreat;

        row.style.display =
            matchesSearch && matchesThreat ? "" : "none";
    });
}

if (historySearch) {
    historySearch.addEventListener("input", filterHistory);
}

if (threatFilter) {
    threatFilter.addEventListener("change", filterHistory);
}


const chartCanvas = document.getElementById("threatChart");

if (chartCanvas && typeof threatDistribution !== "undefined") {

    const labels = threatDistribution.map(item => item[0]);
    const values = threatDistribution.map(item => item[1]);

    new Chart(chartCanvas, {
        type: "bar",

        data: {
            labels: labels,

            datasets: [{
                label: "Scans",
                data: values,
                backgroundColor: labels.map(level => {
                    const colors = {
                        SAFE: "#22c55e",
                        LOW: "#3b82f6",
                        MEDIUM: "#eab308",
                        HIGH: "#f97316",
                        CRITICAL: "#ef4444"
                    };

    return colors[level] || "#64748b";
}),
                borderRadius: 6
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

