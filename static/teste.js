$(document).ready(function () {
  $("#botao").click(function () {
    alert("Seja bem vindo");
  });
});


// $(document).ready(function(){
//   $('#valor').mask('R$  ')
// });

$(document).ready(function(){
  $('#sair').change(function(){
    $('#sair').click(function(){
      $('#sair').attr('href','http://127.0.0.1:5000/logout'); 
      $('#sair').html('Sair');
    });
    
     

  });
});