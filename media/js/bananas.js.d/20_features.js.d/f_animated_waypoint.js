$.feature('f_animated_waypoint', function () {
  $('.animated-waypoint').css({opacity: 0}).waypoint(function() {
    $(this).css({opacity: 1}).addClass('animated');
  }, {
    offset: '80%',
    triggerOnce: true
  });
});
