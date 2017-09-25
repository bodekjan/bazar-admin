$(function(){
      'use strict';
      $(".remove").click(function () {
          var meId = $(this).attr("id");
          var d = dialog({
              title: 'Message',
              content: 'wakaaaaaaaaaaaaaaaaaaaaa',
              okValue: 'yes',
              ok: function () {
                  location.href = "servicelist.html?method=delete&id=" + meId;
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $(".editservice").click(function () {
          var meId = $(this).attr("id");
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addservice?method=edit&id=" + meId;
      });
      $("#addservice").click(function () {
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addservice";
      });
});
