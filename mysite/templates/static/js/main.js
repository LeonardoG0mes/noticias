$(document).ready(function() {
    // Ao clicar no botão "Leia Mais", exibir o conteúdo completo da notícia
    $(".leia-mais").click(function() {
      $(this).prev().slideDown();
      $(this).hide();
    });
  
    // Ao clicar no botão "Comentários", exibir a seção de comentários da notícia
    $(".btn-comentarios").click(function() {
      $(this).parent().next().slideDown();
    });
  
    // Ao clicar no botão "Fechar", esconder o modal de compartilhamento
    $(".fechar-modal").click(function() {
      $(this).parents(".modal").hide();
    });
  
    // Ao clicar no botão "Compartilhar", exibir o modal de compartilhamento
    $(".btn-compartilhar").click(function() {
      $(this).siblings(".modal").show();
    });
  
    // Ao enviar o formulário de comentários, adicionar o novo comentário na seção de comentários
    $(".form-comentario").submit(function(event) {
      event.preventDefault();
      var nome = $(this).find("input[name='nome']").val();
      var comentario = $(this).find("textarea[name='comentario']").val();
      $(this).parents(".comentarios").find(".lista-comentarios").append("<li><strong>" + nome + ":</strong> " + comentario + "</li>");
      $(this).find("input[name='nome'], textarea[name='comentario']").val("");
    });
  });
  