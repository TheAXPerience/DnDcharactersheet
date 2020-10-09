// event when you press "Submit" under "Create Account"
// Will read the inputs, error if any inputs are empty, and ping the server
// to create the account; error if the username already exists
function submit_create() {
  let inputs = $('#create > input');
  var not_empty = true;
  inputs.each(function() {
    not_empty = not_empty && ($(this).val() !== '');
  })
  if (not_empty) {
    // get inputs and send to server
    const i = $('#create').find('input');
    let submit = {
      'type': 'login',
      'email': i[0].value,
      'username': i[1].value,
      'password': i[2].value
    }

    $.ajax({
      url: "/signupaccount",
      type: "POST",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(submit),
      datatype: "text",
      headers: { 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value },
      success: function(response) {
        if (response !== 'OK') {
          $('#create p').text(response);
        } else {
          location.reload();
        }
      },
      failure: function(response) {
        $('#create p').text(response);
      }
    });
  } else {
    $('#create p').text('Error: all parameters must not be empty.');
  }
}

function submit_signin() {
  let inputs = $('#exists > input');
  var not_empty = true;
  inputs.each(function() {
    not_empty = not_empty && ($(this).val() !== '');
  })
  if (not_empty) {
    // get inputs and send to server
    const i = $('#exists').find('input')
    let submit = {
      'type': 'login',
      'username': i[0].value,
      'password': i[1].value
    }
    console.log(submit);

    $.ajax({
      url: "/loginaccount",
      type: "POST",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(submit),
      datatype: "text",
      headers: { 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value },
      success: function(response) {
        if (response !== 'OK') {
          $('#exists p').text(response);
        } else {
          location.reload();
        }
      },
      failure: function(response) {
        $('#exists p').text(response);
      }
    });
  } else {
    $('#exists p').text('Error: all parameters must not be empty.');
  }
}

var is_login_active = false;
function toggle_login() {
  if (is_login_active) {
    $('#page-cover').css("opacity", 0.5).fadeOut(250, function() {
      $('#login').css("display", "none");
      $('#create p').text('');
      $('#exists p').text('');
      $('#create > input').each(function() {
        $(this).val('');
      });
      $('#exists > input').each(function() {
        $(this).val('');
      });
    });
  } else {
    $('#page-cover').css("opacity", 0.5).fadeIn(250, function() {
      $('#login').css("display", "block");
    });
  }
  is_login_active = !is_login_active;
}

function logout() {

}

$().ready(function() {
  $('#page-cover').click(function() {
    toggle_login();
  });
  $('.top-user-login').click(function() {
    toggle_login();
  });
  $('.overlay-header').find('button').click(function() {
    toggle_login();
  });
  $('#create').find('button').click(function() {
    submit_create();
  });
  $('#exists').find('button').click(function() {
    submit_signin();
  });
});
