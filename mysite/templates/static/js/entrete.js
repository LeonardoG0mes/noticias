// entrete.js

function filtrarNoticias() {
  var filtroSelect = document.getElementById("filtro-select");
  var filtro = filtroSelect.value;

  var containerNoticias = document.getElementsByClassName("container-noticia");
  for (var i = 0; i < containerNoticias.length; i++) {
    var container = containerNoticias[i];
    var subLegenda = container.id;

    if (filtro === "todos" || filtro === subLegenda) {
      container.style.display = "block";
    } else {
      container.style.display = "none";
    }
  }
}
