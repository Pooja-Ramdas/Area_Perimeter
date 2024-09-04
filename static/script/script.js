document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the form from submitting immediately

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if(username === '' || password === '') {
        alert('Please fill in all fields');
    } else {
        // Process login here
        alert('Logging in...');
    }
});
