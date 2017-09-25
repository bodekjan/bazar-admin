$(function(){
      'use strict';
      $("body").delegate('#typeimg', 'change', function () {
          $("#typePreview").attr("src", window.URL.createObjectURL(this.files[0]));
      });
      $("#backtolist").click(function () {
          location.href = "/typelist?" + getCookie("parentpage");
      });
});
