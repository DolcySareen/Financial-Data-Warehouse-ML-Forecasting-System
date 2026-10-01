// scripts.js 
function showContent(contentId, elem) {
    // Hide all sections
    const sections = document.querySelectorAll('.content section');
    sections.forEach(function (section) {
        section.classList.remove('active');
    });

    // Show the clicked section
    const activeSection = document.getElementById(contentId);
    activeSection.classList.add('active');

    // Highlight the active menu item
    const links = document.querySelectorAll('.sidebar a');
    links.forEach(function (link) {
        link.classList.remove('active');
    });

    elem.classList.add('active');
}

function updateModelParameters() {
    const modelSelect = document.getElementById("modelSelect");
    const modelParametersGroup = document.getElementById("modelParametersGroup");

    if (modelSelect.value === "classification") {
        modelParametersGroup.innerHTML = `
            <label for="modelParameters">Classification Model Parameters</label>
            <textarea class="form-control" id="modelParameters" rows="4" placeholder="Enter classification parameters"></textarea>
        `;
    } else if (modelSelect.value === "regression") {
        modelParametersGroup.innerHTML = `
            <label for="modelParameters">Regression Model Parameters</label>
            <textarea class="form-control" id="modelParameters" rows="4" placeholder="Enter regression parameters"></textarea>
        `;
    } else if (modelSelect.value === "clustering") {
        modelParametersGroup.innerHTML = `
            <label for="modelParameters">Clustering Model Parameters</label>
            <textarea class="form-control" id="modelParameters" rows="4" placeholder="Enter clustering parameters"></textarea>
        `;
    } else if (modelSelect.value === "forecasting") {
        modelParametersGroup.innerHTML = `
            <label for="modelParameters">Forecasting Model Parameters</label>
            <textarea class="form-control" id="modelParameters" rows="4" placeholder="Enter forecasting parameters"></textarea>
        `;
    }
}

// Function to reset the form
function resetForm() {
    document.getElementById("mlForm").reset();
    updateModelParameters();  // Reset the model parameters dynamically
}

// Function to show/hide data source options based on the selection
function updateDataSourceOptions() {
    const dataSource = document.getElementById("dataSource").value;
    document.getElementById("csvFileUpload").style.display = dataSource === "csv" ? "block" : "none";
    document.getElementById("databaseSettings").style.display = dataSource === "database" ? "block" : "none";
}

function updateSymbols() {
    const assetType = document.getElementById("asset_type").value;
    const stockSymbolSelect = document.getElementById("stock_symbol");

    // Clear existing options
    stockSymbolSelect.innerHTML = '';

    // Fetch symbols based on the selected asset type
    fetch(`/get_symbols?asset_type=${assetType}`)
        .then(response => response.json())
        .then(data => {
            data.symbols.forEach(symbol => {
                const option = document.createElement("option");
                option.value = symbol;
                option.text = symbol;
                stockSymbolSelect.add(option);
            });
        })
        .catch(error => console.error('Error fetching symbols:', error));
}



// Initial setup
document.addEventListener("DOMContentLoaded", function() {
    updateModelParameters();  // Initialize model parameters
    updateDataSourceOptions();  // Initialize data source options
    updateSymbols();  // Initialize symbols based on the default asset type
});

function changeTheme() {
    const theme = document.getElementById('theme').value;

    // Reset all classes
    document.body.classList.remove('light', 'dark', 'dark-light');
    document.querySelector('.sidebar').classList.remove('light', 'dark', 'dark-light');
    document.querySelector('.content').classList.remove('light', 'dark', 'dark-light');
    document.querySelectorAll('.card').forEach(function (card) {
        card.classList.remove('light', 'dark', 'dark-light');
    });
    document.querySelectorAll('.content section').forEach(function (section) {
        section.classList.remove('light', 'dark', 'dark-light');
    });

    // Apply selected theme
    if (theme === 'dark') {
        document.body.classList.add('dark');
        document.querySelector('.sidebar').classList.add('dark');
        document.querySelector('.content').classList.add('dark');
        document.querySelectorAll('.card').forEach(function (card) {
            card.classList.add('dark');
        });
        document.querySelectorAll('.content section').forEach(function (section) {
            section.classList.add('dark');
        });
    } else if (theme === 'light') {
        document.body.classList.add('light');
        document.querySelector('.sidebar').classList.add('light');
        document.querySelector('.content').classList.add('light');
        document.querySelectorAll('.card').forEach(function (card) {
            card.classList.add('light');
        });
        document.querySelectorAll('.content section').forEach(function (section) {
            section.classList.add('light');
        });
    } else if (theme === 'dark-light') {
        document.body.classList.add('dark-light');
        document.querySelector('.sidebar').classList.add('dark-light');
        document.querySelector('.content').classList.add('dark-light');
        document.querySelectorAll('.card').forEach(function (card) {
            card.classList.add('dark-light');
        });
        document.querySelectorAll('.content section').forEach(function (section) {
            section.classList.add('dark-light');
        });
    }
}