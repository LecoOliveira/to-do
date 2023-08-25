$('.form-login .sign-up a').click(function () {
    $('.form-login').animate({ height: "toggle", opacity: "toggle" }, "fast");
    $('.form-register').animate({ height: "toggle", opacity: "toggle" }, "slow");
});

$('.form-register .sign-up a').click(function () {
    $('.form-register').animate({ height: "toggle", opacity: "toggle" }, "fast");
    $('.form-login').animate({ height: "toggle", opacity: "toggle" }, "slow");
});


function cadastrar() {
    const userName = document.getElementById('username-input');
    const email = document.getElementById('email-input');
    const pass = document.getElementById('pass-input');

    fetch('http://localhost:8000/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': userName.value,
            'email': email.value,
            'password': pass.value,
        }),
    }).then(res => res.json())
        .then(data => console.log(data))
}

fetch('http://localhost:8000/users/').then(res => res.json())
    .then(data => console.log(data))

function login() {
    const email = document.getElementById('email-login');
    const pass = document.getElementById('pass-login');

    fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'username': email.value,
            'password': pass.value,
        })
    })
        .then(res => res.json())
        .then(data => console.log(data));
}