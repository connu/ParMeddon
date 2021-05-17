function detect()
{
    document.addEventListener("mouseup", function(event) {
        var obj = document.getElementsByClassName('jus')[0].getElementsByClassName('f')[0];
        var sign_btn = document.getElementsByClassName('sign-up')[0]
        var login = document.getElementsByClassName('log-in')[0]


        if (!obj.contains(event.target)) {
            sign_btn.style.display = 'block'
            login.style.display = 'block'
            obj.style.display = 'none'
        }
    });
}




function display_s()
{
    var sign_up_div = document.getElementsByClassName('jus')[0].getElementsByClassName('f')[0]
    sign_up_div.style.display = 'block'
    var sign_btn = document.getElementsByClassName('sign-up')[0]
    var login = document.getElementsByClassName('log-in')[0]
    sign_btn.style.display = 'none'
    login.style.display = 'none'
}


function display_l() {
    var login_div = document.getElementsByClassName('just')[0].getElementsByClassName('l')[0]
    login_div.style.display = 'block'
    var sign_btn = document.getElementsByClassName('sign-up')[0]
    var login = document.getElementsByClassName('log-in')[0]
    sign_btn.style.display = 'none'
    login.style.display = 'none'
}


function detect_l() 
{
    document.addEventListener("mouseup", function(event) {
        var obj = document.getElementsByClassName('jus')[0].getElementsByClassName('f')[0];
        var login = document.getElementsByClassName('log-in')[0]
        var sign = document.getElementsByClassName('sign-up')[0]


        if (!obj.contains(event.target)) {
            login.style.display = 'block'
            sign.style.display = 'block'
            obj.style.display = 'none'
        }
    });
}