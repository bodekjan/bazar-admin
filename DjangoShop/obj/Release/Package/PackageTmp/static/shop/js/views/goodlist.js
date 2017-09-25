$(function(){
      'use strict';
      $(".remove").click(function () {
          var meId = $(this).attr("id");
          var d = dialog({
              title: 'Message',
              content: 'wakaaaaaaaaaaaaaaaaaaaaa',
              okValue: 'yes',
              ok: function () {
                  location.href = "goodlist.html?method=delete&id=" + meId;
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $("#search").click(function () {
          location.href = "/goodlist?key=" + $("#stext").val() + "&type=" + $("#type-selector").find("option:selected").val();
      });
      $("#type-selector").change(function () {
          location.href = "/goodlist?key=" + $("#stext").val() + "&type=" + $("#type-selector").find("option:selected").val();
      });
});
