// $(document).ready(function () {
//   $("#botao").click(function () {
//     alert("Seja bem vindo");
//   });
// });

$(document).ready(function () {
  $("#valor").mask("R$ 00,00");
});

$(document).ready(function () {
  $("#sair").click(function () {
    $("#sair").attr("disabled", true);
    $("#sair").text("Sair");
  });
});
