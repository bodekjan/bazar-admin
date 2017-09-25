$(function(){
      'use strict';
      $("body").delegate('#bannerimg', 'change', function () {
          $("#bannerPreview").attr("src", window.URL.createObjectURL(this.files[0]));
      });
      $("#backtolist").click(function () {
          location.href = "/bannerlist?" + getCookie("parentpage");
      });
});
