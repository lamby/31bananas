$.feature('f_base', function() {
  $(window).scroll(function() {
    $('.navbar-fixed-top').toggleClass(
      'top-nav-collapse',
      $('.navbar').offset().top > 50
    );
  });
});
