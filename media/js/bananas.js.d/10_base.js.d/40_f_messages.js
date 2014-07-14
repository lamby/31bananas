$.feature('f_messages', function () {
  $.extend({
    message: function (options) {
      options = $.extend({
        'level': 'success',
        'message': '',
        'hide_after': 3000,
      }, options);

      var elem = $('<div class="alert"/>').addClass(
        'alert-' + ((options.level == 'error') ? 'danger' : options.level)
      ).text(options.message);

      $('.alerts').addClass('fixed').append(elem);

      elem.hide().slideDown(function() {
        if (options.hide_after > 0) {
          setTimeout(function() {
            elem.slideUp(function() {
              elem.remove();
            });
          }, options.hide_after);
        }
      });

      return elem;
    }
  });

  $(document).ajaxComplete(function(event, xhr, settings) {
    try {
      data = $.parseJSON(xhr.responseText);
    } catch (e) {
      return;
    }

    $.each(data.__messages__ || [], function() {
      $.message({
        'level': this.level,
        'message': this.message
      });
    });
  });
});
