document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registrationForm');

    registrationForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        let formData = new FormData(registrationForm);

        let response = await fetch(registrationForm.action, {
            method: 'POST',
            body: formData
        });

        let result = await response.json();

        if(result.success) {
            return  window.location.href = "/account/login"
            // Redirect or any other action you'd like to take on success
        } else {
            alert("Registration failed.");
            // Optionally, display the errors. They are available in result.errors
        }
    });
});