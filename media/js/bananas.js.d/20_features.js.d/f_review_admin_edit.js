$.feature('f_review_admin_edit', function() {
  $('.js-save').on('click', function(e) {
    e.preventDefault();

    var button = $(this);
    button.button('loading');

    var form = $('.js-edit-form');

    $.post(form.data('url'), form.serialize(), function() {
      button.button('reset');
    });
  });
});

$.feature('f_review_admin_edit', function() {
  var container = $('#images');

  $.get(container.data('url'), function (data) {
    container.html(data.html);
  });

  container.on('submit', '.js-add', function (e) {
    e.preventDefault();

    var form = $(this);

    $.post(form.data('url'), form.serialize, function (data) {
      container.html(data.html);
    });
  });

  container.on('click', '.js-delete', function (e) {
    e.preventDefault();

    var elem = $(this);

    elem.button('loading');

    $.post(elem.data('url'), {}, function (data) {
      container.html(data.html);
    });
  });
});
