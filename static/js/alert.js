// Function to make alert pop up fade after time limit
// Credit: CodeInstitute Course Material

setTimeout(function() {
    let alertBox = document.getElementById('msg');
    let alert = new bootstrap.Alert(alertBox);
    alert.close();
}, 2500)