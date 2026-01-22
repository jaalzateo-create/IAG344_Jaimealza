function downloadPDF () {

    const element = document.querySelector("#pdf-content");
    //console.log("Funcion ok PDF...");
    //alert("funcion PDF...");

    const otp = {
        margin:      [0,0,10,0], // [Arriba, Izquierda, Abajo, Derecha]
        filename:     'Hoja_de_vida_JAIME_ALZATE.pdf',
        Image:        { type: 'jpeg', quality: 1 },
        html2canvas:  { 
            scale: 3,
            useCORS: true,
            scrollY:0
        },
        jsPDF: { unit: 'mm', 
                        format: 'a4', 
                        orientation: 'portrait' 
        }
    }
    html2pdf().set(otp).from(element).save();
}