const API = "http://127.0.0.1:8000/"
const analyse = async () => {
    let ip = document.querySelector(".input_ip").value
    let file = document.querySelector(".input__file").files[0]

    let params
    
    if (file) {
        params = new URLSearchParams({
            info_type : "file",
            body : file,
        })   
    }
    else if (ip){
        params = new URLSearchParams({
            info_type : "ip",
            body : ip,
        })
    }
    else { 
        alert("Инпут не должен быть пустым")
        return 
    }
    

    document.querySelector(".progress_animation").style.display = "inline-flex"
    const response = await fetch(API+'?'+params, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
          }
    })
    .finally(() => {
        document.querySelector(".progress_animation").style.display = "none";
    })

    data = await response.json()
    console.log(data)

    return add_result(data)
}


const add_result = (data) => {
    let main_block = document.querySelector("#result")
    console.log(data.length)

    let html = '<ul class="ip_blocks">';

    data.ips.forEach(item => {
        html += `
            <li class="ip_block" id="ip-${item.ip}">
                    <div class="ip_block_info">
                        <div class="ip_address" onclick="toggleVisibility('ports-${item.ip}')">
                            ${item.ip}
                        </div>
                        <span>|</span>
                        <div class="ip_location">
                            <div class="ip_country">${item.location.country}, </div>
                            <div class="ip_city"> ${item.location.city}</div>
                        </div>
                        <span>|</span>
                        <div class="ip_os">
                            <div class="ip_os_name">${item.os}</div>
                        </div>
                    </div>
                <ul class="ports" id="ports-${item.ip}" style="display: none;">`;
    
        item.ports.forEach(port => {
            html += `
                <li class="ip_adress_port" id="port_${port.port}">
                    <ul><p>Port: ${port.port}</p>
                        <ol><div class="port_protocol">Протокол: ${port.protocol}</div></ol>
                        <ol><div class="port_service">Служба: ${port.service}</div></ol>
                        <ol><div class="port_message">Комментарий: ${port.message}</div></ol>
                    </ul>
                    

                </li>`;
        });
    
        html += `
                </ul>
            </li>`;
    });
    
    html += '</ul>';
    
    html += `
        <div class="save_res">
            <div>Сохранить результаты в файл</div>
            <div><a href="${data.pdf_report}"></a></div>
        </div>
    `;

    main_block.innerHTML = html;
    
    if (data.length==1) {
        const portId = "ports-"+data[0].ip
        console.log(portId)
        toggleVisibility(portId)
    }
    return true
} 

function toggleVisibility(portId) {
    const portsDiv = document.getElementById(portId);
    if (portsDiv.style.display === "none") {
        portsDiv.style.display = "block";
    } else {
        portsDiv.style.display = "none";
    }
}