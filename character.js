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
  s.text(submit.range);
  s = s.next();

  // damage
  submit.damage = s.find("input")[0].value;
  s.text(submit.damage);
  s = s.next();

  // delete
  s.html('<button type="button" name="delete" class="delete-as">Delete</button>');
  console.log(submit);
  s.find("button.delete-as").click(function() {
    $(this).parent().parent().remove();
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
  console.log(submit);
  s.find("button.delete-eq").click(function() {
    $(this).parent().parent().remove();
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
  s.html('<button type="button" name="delete" class="delete-eq">Delete</button>');
  console.log(submit);
  s.find("button.delete-eq").click(function() {
    $(this).parent().parent().remove();
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
    $(this).parent().parent().remove();
    // remove from model
  });

  $('.delete-eq').click(function() {
    $(this).parent().parent().remove();
    // remove from model
  });

  $('.delete-sp').click(function() {
    $(this).parent().parent().remove();
    // remove from model
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
        }
      }
    });
});
