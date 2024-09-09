// Attach the event listener to all existing delete buttons
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission or button action

        // Prompt for password
        const password = prompt('Please enter your password to delete:');

        if (password === null || password === "") {
            alert("Deletion cancelled.");
            return; // Exit if the user cancels the prompt or submits an empty password
        }

        // Replace with actual password validation logic
        if (validatePassword(password)) {
            // If password is correct, proceed with deletion
            const row = this.closest('tr');
            const drugId = row.getAttribute('data-drug-id'); // Use a data attribute for the drug ID

            // Make an AJAX call to delete the item from the backend
            makeDeleteRequest(drugId, row);
        } else {
            alert("Incorrect password. Deletion aborted.");
        }
    });
});

// Dummy password validation function (replace with actual logic)
function validatePassword(password) {
    // Replace this with your actual password validation logic
    return password === "yourCorrectPassword";
}

// Example of an AJAX request function for deletion
function makeDeleteRequest(drugId, row) {
    fetch(`/api/delete_drug/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Handle CSRF token for POST requests
        },
        body: JSON.stringify({ 'drug_id': drugId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            row.remove();
            alert("Drug deleted successfully.");
        } else {
            alert("Failed to delete drug.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while deleting the drug.");
    });
}

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Handle editing functionality
$(document).ready(function () {
    var editModal = document.getElementById("edit-modal");
    var closeEdit = document.getElementsByClassName("close-edit")[0];

    // Open edit modal and populate with existing data
    $(document).on('click', '.edit-button', function () {
        var row = $(this).closest('tr');
        $('#edit-drug-id').val(row.find('td').eq(0).text());
        $('#edit-drug-name').val(row.find('td').eq(1).text());
        $('#edit-manufacturer').val(row.find('td').eq(2).text());
        $('#edit-drug-type').val(row.find('td').eq(3).text());
        $('#edit-quantity').val(row.find('td').eq(4).text());
        $('#edit-expiry-date').val(row.find('td').eq(5).text());
        $('#edit-description').val(row.find('td').eq(6).text());
        $('#edit-batch-no').val(row.find('td').eq(7).text());
        $('#edit-row-index').val(row.index()); // Store the index of the row being edited
        editModal.style.display = "block";
    });

    // Close the edit modal
    closeEdit.onclick = function () {
        editModal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target == editModal) {
            editModal.style.display = "none";
        }
    }

    // Handle form submission
    $('#edit-drug-form').submit(function (event) {
        event.preventDefault();

        var index = $('#edit-row-index').val(); // Get the row index
        var updatedRow = `
            <tr data-drug-id="${$('#edit-drug-id').val()}">
                <td>${$('#edit-drug-id').val()}</td>
                <td>${$('#edit-drug-name').val()}</td>
                <td>${$('#edit-manufacturer').val()}</td>
                <td>${$('#edit-drug-type').val()}</td>
                <td>${$('#edit-quantity').val()}</td>
                <td>${$('#edit-expiry-date').val()}</td>
                <td>${$('#edit-description').val()}</td>
                <td>${$('#edit-batch-no').val()}</td>
                <td>
                    <div class="action-buttons">
                        <button class="edit-button"><i class="fas fa-edit"></i>Edit</button>
                        <button class="delete-btn"><i class="fas fa-minus"></i>Delete</button>
                    </div>
                </td>
            </tr>
        `;

        $('#drug-table-body tr').eq(index).replaceWith(updatedRow); // Replace the old row with the updated row

        editModal.style.display = "none";

        // Make an AJAX call to update the item in the backend
        makeUpdateRequest($('#edit-drug-id').val(), {
            name: $('#edit-drug-name').val(),
            manufacturer: $('#edit-manufacturer').val(),
            drug_type: $('#edit-drug-type').val(),
            quantity: $('#edit-quantity').val(),
            expiry_date: $('#edit-expiry-date').val(),
            description: $('#edit-description').val(),
            batch_no: $('#edit-batch-no').val()
        });
    });
});

// Function to handle update requests
function makeUpdateRequest(drugId, updatedData) {
    fetch(`/api/update_drug/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Handle CSRF token for POST requests
        },
        body: JSON.stringify({ 'drug_id': drugId, ...updatedData })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert("Drug updated successfully.");
        } else {
            alert("Failed to update drug.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while updating the drug.");
    });
}
