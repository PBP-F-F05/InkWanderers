function changePassword() {
    fetch("/account/password_change_by_ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    })

    document.getElementById("form").reset()
    return false
}
document.getElementById("button_change_password").onclick = changePassword