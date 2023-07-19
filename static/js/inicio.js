// let user = document.getElementById('user');
// let password = document.getElementById('password');
// let btn = document.getElementById('submit1')

// console.log(user.length)

const largo = () => {
    let user = document.getElementById('user');
    let password = document.getElementById('password');
    let btn = document.getElementById('submit1');

    if ((user.value.length >=6) && (password.value.length >=6)) {
        btn.disabled = false;
    }
    else {
        btn.disabled = true;
    }
};