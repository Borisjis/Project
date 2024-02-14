let search = (new URL(window.location.href)).searchParams

if (search.size > 0) {
    allUsers.push({
        name: search.get("name"),
        email: search.get("email"),
        password: search.get("password"),
    })
    currUser = allUsers.length - 1
    
    window.localStorage.setItem("users", JSON.stringify(allUsers))
    window.localStorage.setItem("current-user", currUser.toString())

    let redirect = (window.location.protocol + window.location.port + window.location.pathname).split("/")
    redirect.splice(redirect.length - 1, 1)
    window.location = redirect.join("/") + "/home"
}