const API = "http://127.0.0.1:8000/"

const analyse = async () => {
    let ip = document.querySelector(".input_ip").value
    console.log(ip)
    const response = await fetch(API, {
        method: 'GET',
        // body : ip,
        headers: {
            'Content-Type': 'application/json'
          },
    })
    data = await response.json()
    console.log(data)

    // return add_result(data)
}


const add_result = (data) => {
    console.log(data)
} 