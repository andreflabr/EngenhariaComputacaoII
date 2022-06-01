$(document).ready(function () {
  $("#name").mask();
  $("#valor").mask("999.999.990.00", { reverse: true });
});

// validação de usuario
$(document).ready(function () {
  $("#usuarioNovo").validate({
    rules: {
      name: {
        required: true,
        minlength: 3,
      },
      lastname: {
        required: true,
        minlength: 3,
      },
      email: {
        required: true,
        email: true,
      },
    },
  });
});

// validação de login
$(document).ready(function () {
  $("#login").validate({
    rules: {
      usuario: {
        required: true,
        email: true,
      },
    },
  });
});
