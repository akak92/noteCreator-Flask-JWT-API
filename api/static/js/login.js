function login() {
    // Get input values
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Create JSON object
    var data = {
        "username": username,
        "password": password
    };

    // Send data to backend API
    fetch('/api/v1/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) { // Check if response status is OK (status code 200-299)
            document.getElementById('message').classList.remove('error');
            document.getElementById('message').classList.add('success');
            document.getElementById('message').innerText = "Login successful!";
        } else {
            document.getElementById('message').classList.remove('success');
            document.getElementById('message').classList.add('error');
            document.getElementById('message').innerText = "Login failed. Please try again.";
        }
        document.getElementById('message').style.display = 'block'; // Show message
    })
    .catch(error => {
        console.error('Error:', error);
    });
}