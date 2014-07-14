$.feature('f_blog_admin_edit', function() {
  $('.js-populate-slug').keyup(function() {
    $('.js-slug').val(URLify($(this).val()));
  });

  $('form.js-delete').on('submit', function() {
    return confirm("Are you sure you want to delete this post?");
  });

  $('.js-save').on('click', function(e) {
    e.preventDefault();

    var form = $('form.form-post');

    $.post(form.data('url'), form.serialize());
  });

  $('button.js-publish').on('click', function(e) {
    e.preventDefault();

    var form = $('form.form-post');

    form.append('<input type="hidden" name="publish" value="on">');

    $.post(form.data('url'), form.serialize());
  });

  $('.js-cover-url').on('paste', function(e) {
    var input = $(this);

    setTimeout(function() {
      var url = input.val();
      input.val('');

      $.post(input.data('url'), {'url': url});
    }, 500);
  });
});
