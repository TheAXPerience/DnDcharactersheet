// event when you press "Submit" under "Create Account"
// Will read the inputs, error if any inputs are empty, and ping the server
// to create the account; error if the username already exists
function submit_create() {
  let inputs = $('#create > input');
  var not_empty = true;
  var str = '';
  inputs.each(function() {
    not_empty = not_empty && ($(this).val() !== '');
    str += $(this).val();
  })
  if (not_empty) {
    location.reload();
  } else {
    $('#create p').text('submit create account: ' + str);
  }
}

function submit_signin() {
  $('#exists p').text('submit sign-in to account');
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
