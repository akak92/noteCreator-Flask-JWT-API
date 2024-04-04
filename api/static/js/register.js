function register(){
    var name = document.getElementById('name').value;
    var last_name = document.getElementById('last_name').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password1').value;
    var re_password = document.getElementById('password2').value;

    var data = {
        'name' : name,
        'last_name' : last_name,
        'username' : username,
        'password' : password,
        're_password' : re_password
    }

    // Send data to backend API
    fetch('/api/v1/register', {
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
            document.getElementById('message').innerText = "Registration succesfull!";
            window.location.href = '/login';
        } else {
            document.getElementById('message').classList.remove('success');
            document.getElementById('message').classList.add('error');
            document.getElementById('message').innerText = "Registration failed. Please try again.";
            window.location.href = '/register'
        }
        document.getElementById('message').style.display = 'block'; // Show message
    })
    .catch(error => {
        console.error('Error:', error);
    });
}