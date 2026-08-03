const analyzeButton = document.getElementById("analyzeButton");
const urlInput = document.getElementById("urlInput");
const analysisStatus = document.getElementById("analysisStatus");
const threatLevel = document.getElementById("threatLevel");
const riskScore = document.getElementById("riskScore");
analyzeButton.addEventListener("click", () => {

    if (urlInput.value.trim() === "") {
        analysisStatus.textContent = "Please enter a URL.";
        analysisStatus.className = "text-red-400";
        return;
    }

    analysisStatus.textContent = "Analyzing URL...";
    analysisStatus.className = "text-blue-400";

    

});