$(function(){
      'use strict';
      $("body").delegate('#empimg', 'change', function () {
          $("#empPreview").attr("src", window.URL.createObjectURL(this.files[0]));
      });
});
