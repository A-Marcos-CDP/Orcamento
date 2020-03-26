function getOrc() {
    eel.getDone()
}

function caminho() {
    var direct = document.getElementById("caminho").value
    var way = document.getElementById("saida").value
	eel.direct(direct, way)
}

function showDiv() {
    document.getElementById('iframe').contentWindow.location.reload();
    document.getElementById('pop').style.display = "block";
 }