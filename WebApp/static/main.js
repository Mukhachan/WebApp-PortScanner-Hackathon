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

    return add_result(data)
}


const add_result = (data) => {
    let main_block = document.querySelector("#result")
    console.log(main_block)
    for (let index = 0; index < data.length; index++) {
        const element = data[index];

        let ip_block = document.createElement("DIV")
        ip_block.

        main_block.appendChild(ip_block)
    }
    
    return true
} 