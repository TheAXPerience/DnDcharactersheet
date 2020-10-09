function addEmptyListeners(table) {
  // empty text => n/a
  const txtInputs = table.find('input[type=text]');
  for (let i = 0; i < txtInputs.length; i++) {
    txtInputs[i].addEventListener('change', function(e) {
      if (e.target.value == '') {
        e.target.value = 'n/a';
      }
    });
  }

  // empty number => 0
  const numInputs = table.find('input[type=number]');
  for (let i = 0; i < numInputs.length; i++) {
    numInputs[i].addEventListener('change', function(e) {
      if (e.target.value == '') {
        e.target.value = 0;
      }
    });
  }
}

function add_as_row(table) {
  let to_add = '<tr>';
  to_add += '<td><input type="text" name="name" value="n/a"></td>';
  to_add += '<td><input type="text" name="hit" value="n/a"></td>';
  to_add += '<td><input type="number" name="range" value=5></td>';
  to_add += '<td><input type="text" name="damage" value="n/a"></td>';
  to_add += '<td><button type="button" name="add" class="add-as-button">Add</button></td>';
  to_add += '</tr>';
  table.append(to_add);

  table.find("button.add-as-button").last().click(function() {
    submit_as_row($(this).parent().parent());
  });
  addEmptyListeners(table);
};

function add_eq_row(table) {
  let to_add = '<tr>';
  to_add += '<td><input type="text" name="name" value="n/a"></td>';
  to_add += '<td><input type="number" name="quantity" value=1></td>';
  to_add += '<td><input type="number" name="weight" value=1></td>';
  to_add += '<td><button type="button" name="add" class="add-eq-button">Add</button></td>';
  to_add += '</tr>';
  table.append(to_add);

  table.find("button.add-eq-button").last().click(function() {
    submit_eq_row($(this).parent().parent());
  });
  addEmptyListeners(table);
};

function add_sp_row(table) {
  let to_add = '<tr>';
  to_add += '<td><input type="checkbox" name="prepared"></td>';
  to_add += '<td><input type="text" name="name" value="n/a"></td>';
  to_add += '<td><input type="number" name="level" value=0></td>';
  to_add += '<td><button type="button" name="add" class="add-sp-button">Add</button></td>';
  to_add += '</tr>';
  table.append(to_add);

  table.find("button.add-sp-button").last().click(function() {
    submit_sp_row($(this).parent().parent());
  });
  addEmptyListeners(table);
};

function getCookie() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function delete_aes(name, url) {
  let submit = {
    'type': 'delete',
    'name': name
  }

  $.ajax({
    url: url,
    type: "POST",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(submit),
    datatype: "text",
    headers: { 'X-CSRFToken': getCookie() },
    success: function(response) {
      alert(response);
    }
  });
}

function submit_as_row(parent) {
  let s = parent.children().first();
  let submit = {
    'type': 'add'
  }

  // name
  submit.name = s.find("input")[0].value;
  s.text(submit.name);
  s = s.next();

  // hit
  submit.hit = s.find("input")[0].value;
  s.text(submit.hit);
  s = s.next();

  // range
  submit.range = s.find("input")[0].value;
  s.text(submit.range + " ft");
  s = s.next();

  // damage
  submit.damage = s.find("input")[0].value;
  s.text(submit.damage);
  s = s.next();

  // delete
  s.html('<button type="button" name="delete" class="delete-as">Delete</button>');
  s.find("button.delete-as").click(function() {
    delete_aes(submit.name, 'submit-as');
    $(this).parent().parent().remove();
  });

  $.ajax({
    url: "submit-as",
    type: "POST",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(submit),
    datatype: "text",
    headers: { 'X-CSRFToken': getCookie() },
    success: function(response) {
      if (response !== 'OK') {
        parent.remove();
      }
      alert(response);
    }
  });
};

function submit_eq_row(parent) {
  let s = parent.children().first();
  let submit = {
    'type': 'add'
  }

  // name
  submit.name = s.find("input")[0].value;
  s.text(submit.name);
  s = s.next();

  // quantity
  submit.quantity = s.find("input")[0].value;
  s.text(submit.quantity);
  s = s.next();

  // weight
  submit.weight = s.find("input")[0].value;
  s.text(submit.weight);
  s = s.next();

  // delete
  s.html('<button type="button" name="delete" class="delete-eq">Delete</button>');
  s.find("button.delete-eq").click(function() {
    delete_aes(submit.name, 'submit-eq');
    $(this).parent().parent().remove();
  });

  $.ajax({
    url: "submit-eq",
    type: "POST",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(submit),
    datatype: "text",
    headers: { 'X-CSRFToken': getCookie() },
    success: function(response) {
      if (response !== 'OK') {
        parent.remove();
      }
      alert(response);
    }
  });
};

function submit_sp_row(parent) {
  let submit = {
    'type': 'add',
    'prepared': 'false',
    'name': 'n/a',
    'level': 0
  };
  let s = parent.children().first();

  // prepared
  if (s.find("input")[0].checked) {
    s.html('<div class="circle fill"></div>');
    submit.prepared = 'true';
  } else {
    s.html('<div class="circle"></div>');
    submit.prepared = 'false';
  }
  s = s.next();

  // name
  submit.name = s.find("input")[0].value;
  s.text(submit.name);
  s = s.next();

  // level
  submit.level = s.find("input")[0].value;
  s.text(submit.level);
  s = s.next();

  // delete
  s.html('<button type="button" name="delete" class="delete-sp">Delete</button>');
  s.find("button.delete-sp").click(function() {
    delete_aes(submit.name, 'submit-sp');
    $(this).parent().parent().remove();
  });

  $.ajax({
    url: "submit-sp",
    type: "POST",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(submit),
    datatype: "text",
    headers: { 'X-CSRFToken': getCookie() },
    success: function(response) {
      if (response !== 'OK') {
        parent.remove();
      }
      alert(response);
    }
  });
};

$().ready(function() {
  $('#add-as').click(function() {
    add_as_row($(this).closest('table'));
  });

  $('#add-eq').click(function() {
    add_eq_row($(this).closest("table"));
  });

  $('#add-sp').click(function() {
    add_sp_row($(this).closest("table"));
  });

  $('.delete-as').click(function() {
    const name = $(this).parent().parent().find("td")[0].innerHTML;
    delete_aes(name, 'submit-as');
    $(this).parent().parent().remove();
  });

  $('.delete-eq').click(function() {
    const name = $(this).parent().parent().find("td")[0].innerHTML;
    delete_aes(name, 'submit-eq');
    $(this).parent().parent().remove();
  });

  $('.delete-sp').click(function() {
    const name = $(this).parent().parent().find("td")[1].innerHTML;
    delete_aes(name, 'submit-sp');
    $(this).parent().parent().remove();
  });

  $('[contentEditable="true"]').keypress(function(e) {
    let x = event.charCode || event.keyCode;
    if (isNaN(String.fromCharCode(e.which)) && x != 46) e.preventDefault();
    return e.which != 13;
  });

  $('[contentEditable="true"]')
    .focus(function() {
      $(this).data('initialText', $(this).html());
    }).blur(function() {
      if ($(this).data('initialText') !== $(this).html()) {
        /// replace change
        if ($(this).text() === '') {
          $(this).text($(this).data('initialText'));
        } else {
          // submit
          let submit = {
            name: $(this).attr('name'),
            data: $(this).text()
          }
          alert('hi')
          $.ajax({
            url: "submit-edit",
            type: "POST",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(submit),
            datatype: "text",
            headers: { 'X-CSRFToken': getCookie() },
            success: function(response) {
              alert(response);
            }
          });
        }
      }
    });
});
