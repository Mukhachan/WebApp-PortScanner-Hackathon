const API = ""

const analyse = async (ip) => {
    let response = await fetch(API, {
        method: 'POST',
        body : ip
    })

    console.log(await response.text())

}