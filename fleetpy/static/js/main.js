document.addEventListener("DOMContentLoaded", function() {
    const rows = document.querySelectorAll(".clickable-row");
    rows.forEach(row => {
        row.addEventListener("click", function() {
            const receiptId = this.dataset.receiptId;
            fetch(`/receipt/${receiptId}/`)
                .then(response => response.text())
                .then(data => {
                    document.getElementById("receiptContainer").innerHTML = data;
                    document.getElementById("receiptModal").style.display = "block";
                });
        });
    });
});

function closeReceiptModal() {
    document.getElementById("receiptModal").style.display = "none";
}
    document.addEventListener('DOMContentLoaded', function () {
        var registerForm = document.getElementById('register-form');

        registerForm.addEventListener('submit', function (event) {
            var isValid = true;

            var username = document.getElementById('username');
        var usernameError = document.getElementById('username-error');
        if (!/^[\w.@+-]+$/.test(username.value) || username.value.length > 150) {
            usernameError.style.display = 'block';
            isValid = false;
        } else {
            usernameError.style.display = 'none';
        }

        var email = document.getElementById('email');
        var emailError = document.getElementById('email-error');
        var emailRegex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(email.value)) {
            emailError.style.display = 'block';
            isValid = false;
        } else {
            emailError.style.display = 'none';
        }

        var phoneNumber = document.getElementById('phone_number');
        var phoneNumberError = document.getElementById('phone-number-error');
        var phoneNumberRegex = /^\d{4}-\d{3}-\d{4}$/;
        if (!phoneNumberRegex.test(phoneNumber.value)) {
            phoneNumberError.style.display = 'block';
            isValid = false;
        } else {
            phoneNumberError.style.display = 'none';
        }

        var password = document.getElementById('password');
        var passwordError = document.getElementById('password-error');
        if (password.value.length < 8 || /^\d+$/.test(password.value) || password.value.toLowerCase() === username.value.toLowerCase() || /password/.test(password.value.toLowerCase())) {
            passwordError.style.display = 'block';
            isValid = false;
        } else {
            passwordError.style.display = 'none';
        }

        var confirmPassword = document.getElementById('confirm_password');
        var confirmPasswordError = document.getElementById('confirm-password-error');
        if (password.value !== confirmPassword.value) {
            confirmPasswordError.style.display = 'block';
            isValid = false;
        } else {
            confirmPasswordError.style.display = 'none';
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});

    