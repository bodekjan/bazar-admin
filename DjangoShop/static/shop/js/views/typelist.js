$(function(){
      'use strict';
      $(".remove").click(function () {
          var meId = $(this).attr("id");
          var d = dialog({
              title: 'Message',
              content: 'wakaaaaaaaaaaaaaaaaaaaaa',
              okValue: 'yes',
              ok: function () {
                  location.href = "typelist.html?method=delete&id=" + meId;
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
});
