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
