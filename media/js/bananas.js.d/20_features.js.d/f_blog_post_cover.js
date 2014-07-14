$.feature('f_blog_post_cover', function() {
  var update = function() {
    var target = Math.min(800, Math.max(260, $(window).height() - 115));

    $('.cover').height(target);
  };

  update();
  $(window).on('resize', update);
});
