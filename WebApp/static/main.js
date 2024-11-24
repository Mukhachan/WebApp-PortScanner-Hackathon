const API = "http://127.0.0.1:8000/"
const analyse = async () => {
    let ip = document.querySelector(".input_ip").value
    let fileInput = document.querySelector(".input__file")
    
    if (fileInput.files.length > 0) {
        const formData = new FormData()
        formData.append('file', fileInput, fileInput.files[0])

        document.querySelector(".progress_animation").style.display = "block"
        try {
            const response = await fetch(API + 'file/', {
                method: 'POST',
                body: formData,
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .finally(() => {
                document.querySelector(".progress_animation").style.display = "none";
            })
            data = await response.json()
            console.log(data)

            return add_result(data)
        } catch (error) {
            console.error(error)
        }
    }
    else if (ip){
        document.querySelector(".progress_animation").style.display = "block"
        const response = await fetch(API+'ip/'+ip, {
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
    else { 
        alert("Инпут не должен быть пустым")
        return 
    }
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
            <div>Сохранить результаты в файл: </div>
            <div><a class="install_pdf" href="${data.pdf_report}" target="__blank">Скачать PDF</a></div>
            <div>|</div>
            <div><a class="genQR" onclick=GenerateQR("${data.pdf_report}")>Создать QR</a></div>
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

const GenerateQR = (text) => {
    document.querySelector(".qrPopup").style.display = 'block'
    // Создание экземпляра QRCode
    var qrcode = new QRCode(document.getElementById("qrcode"), {
        text: text, // Введите здесь текст или URL-адрес, который вы хотите закодировать в QR-код
        width: 256, // Ширина QR-кода в пикселях
        height: 256, // Высота QR-кода в пикселях
        colorDark: "#000", // Цвет кода
        colorLight: "#fff", // Цвет фона
        correctLevel: QRCode.CorrectLevel.H, // уровень исправления ошибок
    });
}

const close_modal = (el) => {
    document.querySelector(".qrPopupInner").innerHTML = null
    document.querySelector(el).style.display = "none"
}