$.feature('f_generic_base', function () {
  $('a[href*=#]').click(function (e) {
    e.preventDefault();

    var hash = this.hash;
    var target = $(hash);

    if (target.length === 0) {
      return;
    }

    var top_ = target.offset().top;
    var w_height = $(window).height();
    var d_height = $(document).height();

    $('html, body').animate({
      scrollTop: (top_ > d_height - w_height) ? d_height - w_height : top_,
    }, 600, 'swing', function() {
      window.location.hash = hash;
    });
  });
});
