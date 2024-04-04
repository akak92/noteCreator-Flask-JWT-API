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
            // Parse response body as JSON
            return response.json();
        } else {
            throw new Error('Login failed. Please try again.');
        }
    })
    .then(data => {
        // Extract access token from response
        var accessToken = data.access_token;
        if (!accessToken) {
            throw new Error('Access token not found in response.');
        }

        // Store access token in local storage
        localStorage.setItem('accessToken', accessToken);

        // Fetch panel page
        fetchPanelPage();
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle error
        document.getElementById('message').classList.remove('success');
        document.getElementById('message').classList.add('error');
        document.getElementById('message').innerText = "Login failed. Please try again.";
        document.getElementById('message').style.display = 'block'; // Show message
    });
}

// Function to fetch panel page
function fetchPanelPage() {
    // Retrieve access token from local storage
    var accessToken = localStorage.getItem('accessToken');

    // Check if access token exists
    if (!accessToken) {
        console.error('Access token not found.');
        return;
    }

    // Send GET request to panel page with Authorization header
    fetch('/panel/check', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + accessToken
        }
    })
    .then(response => {
        if (response.ok) {
            // If response is successful, you can handle the response here
            console.log('Panel page fetched successfully');
            console.log(accessToken)
            window.location.href = '/panel'
        } else if (response.status === 401) {
            // Unauthorized, redirect user to login page
            window.location.href = '/login';
        } else {
            throw new Error('Failed to fetch panel page.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle error
    });
}